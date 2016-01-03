"""
API generator for the BGAPI protocol using the bleapi.xml format.
"""
import sys
import argparse
import xml.dom.minidom

# Map "base" datatypes to struct specifiers
BASE_DATA_TYPE_TO_STRUCT = {
    'int8':   'b',
    'int16':  'h',
    'uint8':  'B',
    'uint16': 'H',
    'uint32': 'I',
    'bd_addr': '6s'
    # uint8array is special
}

# Filled in when processing XML
DATA_TYPE_MAP = {}

class APIParserError(Exception):
    """ An error occurred while parsing the API XML specification. """
    pass

def generate_decodable(prefix, name, param_list_element, output_fp):
    """ Generate a Decodable subclass and return its name. """
    new_cls = '{}_{}'.format(prefix, name)
    output_fp.write("class {}(Decodable):\n".format(new_cls))
    output_fp.write("    decoded_type = namedtuple('{}_type', (\n".format(new_cls))

    struct_format = ""
    ends_with_uint8array = False

    for param_element in param_list_element.getElementsByTagName('param'):
        return_param_name = param_element.getAttribute('name')
        return_param_datatype = param_element.getAttribute('datatype')

        # Build up structure definition.  If a bgapi type has a uint8array,
        # we assume there is only one instance and it ends with the array.
        if return_param_datatype != 'uint8array':
            return_param_type = DATA_TYPE_MAP[return_param_datatype]
            struct_format += return_param_type

        else:
            # Append B for uint8array length
            struct_format += "B"
            ends_with_uint8array = True

        # namedtuple field name
        output_fp.write("        '{}',\n".format(return_param_name))

    output_fp.write("    ))\n") # end namedtuple declaration

    # Generate struct format, if it is not the default
    if struct_format:
        output_fp.write("    decode_struct = Struct('<{}')\n".format(struct_format))

    # Note if we end with a uint8array type.
    if ends_with_uint8array:
        output_fp.write("    ends_with_uint8array = True\n")

    output_fp.write('\n')

    return new_cls


def generate_events_from_class(class_element, output_fp):
    event_list = []

    class_name = class_element.getAttribute('name')
    event_element_list = class_element.getElementsByTagName('event')

    for event_element in event_element_list:
        event_name = '{}_{}'.format(class_name, event_element.getAttribute('name'))
        event_index = int(event_element.getAttribute('index'))

        # Event types from BGAPI commands
        event_typename = generate_decodable('event', event_name, event_element, output_fp)
        event_list.append((event_index, event_typename))

    return event_list

def generate_enums_from_class(class_element, output_fp):
    class_name = class_element.getAttribute('name')
    enums_element_list = class_element.getElementsByTagName('enums')

    for enums_element in enums_element_list:
        enum_typename = enums_element.getAttribute('name')

        output_fp.write('class {}_{}(Enum):\n'.format(class_name, enum_typename))
        for enum_value_element in enums_element.getElementsByTagName('enum'):
            # Some enum value names have a prefix the same as the type itself, e.g.,
            # <enums name="bonding_key">
            #     ...
            #     <enum name="bonding_key_ltk" value="0x01"/>
            #     <enum name="bonding_key_masterid" value="0x40"/>
            # </enums>
            # Strip out the duplicates.
            enum_value_name = enum_value_element.getAttribute('name')
            if enum_value_name.startswith(enum_typename + '_'):
                enum_value_name = enum_value_name[len(enum_typename) + 1:]

            # 'value' could be hex or decimal
            enum_value = enum_value_element.getAttribute('value')
            output_fp.write('    {} = {}\n'.format(enum_value_name, enum_value))

        output_fp.write('\n')

def generate_commands_from_class(class_element, output_fp):
    command_list = []

    class_name = class_element.getAttribute('name')
    class_index = int(class_element.getAttribute('index'))
    command_element_list = class_element.getElementsByTagName('command')

    for command_element in command_element_list:
        command_index = int(command_element.getAttribute("index"))
        command_name = "{}_{}".format(class_name, command_element.getAttribute('name'))

        # Command types
        params_element_list = command_element.getElementsByTagName('params')

        if not params_element_list:
            continue

        command_param_list = params_element_list[0].getElementsByTagName('param')

        struct_spec = ""
        ends_with_uint8array = False

        command_cls_name = "command_{}".format(command_name)
        command_field_list = []
        for param_element in command_param_list:
            param_name = param_element.getAttribute('name')
            param_datatype = param_element.getAttribute('datatype')
            # param_type = param_element.getAttribute('type')

            command_field_list.append(param_name)

            # Build up structure definition.  If a bgapi type has a uint8array,
            # we assume there is only one instance and it ends with the array.
            if param_datatype != 'uint8array':
                param_type = DATA_TYPE_MAP[param_datatype]
                struct_spec += param_type

            else:
                # Append B for uint8array length
                struct_spec += "B"
                ends_with_uint8array = True

        output_fp.write("class {0}(namedtuple('{0}', '{1}')):\n".format(command_cls_name, ' '.join(command_field_list)))
        # Performance; don't create instance dict
        output_fp.write("   __slots__ = ()\n")
        output_fp.write("   _id = (0, {}, {})\n".format(class_index, command_index))
        output_fp.write("   _struct = Struct('<{}')\n".format(struct_spec))
        output_fp.write("   _ends_with_uint8array = {}\n".format("True" if ends_with_uint8array else "False"))
        output_fp.write("\n")

        # Return types from BGAPI commands
        return_field_list = command_element.getElementsByTagName('returns')
        if not return_field_list:
            continue

        response_cls = generate_decodable('response', command_name, return_field_list[0], output_fp)
        command_list.append((command_index, command_cls_name, response_cls))

    return command_list

def generate_api_from_document(document, output_fp):
    # Header; imports
    output_fp.write(
        "\"\"\" bgasync.api - BGAPI classes, constants, and utility functions. \"\"\"\n"
        "# This file is auto-generated. Edit at your own risk!\n"
        "from struct import Struct\n"
        "from collections import namedtuple\n"
        "from enum import Enum\n"
        # We take over everything from apibase.
        "from .apibase import *\n"
        "\n")

    # TODO: Check API level / device name ("ble")

    # Datatypes
    data_type_list = document.getElementsByTagName("datatype")
    for datatype_element in data_type_list:
        base_datatype_name = datatype_element.getAttribute("base")
        # Special case - uint8array is handled differently.
        if base_datatype_name != "uint8array":
            datatype_name = datatype_element.getAttribute("name")
            DATA_TYPE_MAP[datatype_name] = BASE_DATA_TYPE_TO_STRUCT[base_datatype_name]

    # Classes
    class_list = []
    class_element_list = document.getElementsByTagName('class')

    for class_element in class_element_list:
        class_index = int(class_element.getAttribute("index"))
        class_name = class_element.getAttribute("name")

        # Events
        event_list = generate_events_from_class(class_element, output_fp)

        # Commands
        command_list = generate_commands_from_class(class_element, output_fp)

        # Enumerations
        generate_enums_from_class(class_element, output_fp)

        # End classes
        output_fp.write("\n")

        class_list.append((class_index, class_name, command_list, event_list))

    # Map class ID to name.  Useful for logging.
    output_fp.write("CLASS_NAME_MAP = {\n")
    for class_index, class_name, command_list, event_list in class_list:
        output_fp.write("    {}: '{}',\n".format(class_index, class_name))
    output_fp.write("}\n\n")

    # Map the tuple (class_id, event_id) to the appropriate Decodable type
    # corresponding to a received BGAPI event.
    output_fp.write("EVENT_TYPE_MAP = {\n")
    for class_index, class_name, command_list, event_list in class_list:
        for event_index, event_typename in event_list:
            output_fp.write("    ({}, {}): {},\n".format(class_index, event_index, event_typename))
    output_fp.write("}\n\n")

    # Map the tuple (class_id, command_id) to the appropriate Decodable type
    # corresponding to a received BGAPI command response.
    output_fp.write("COMMAND_RETURN_TYPE_MAP = {\n")
    for class_index, class_name, command_list, event_list in class_list:
        for command_index, _, response_cls in command_list:
            output_fp.write("    ({}, {}): {},\n".format(class_index, command_index, response_cls))
    output_fp.write("}\n\n")

    # Create a mixin class for dispatching decoded events individually
    output_fp.write("class EventDecoderMixin(object):\n")
    output_fp.write("    def __init__(self):\n")
    # Event table
    output_fp.write("        self.event_type_map = {\n")
    for class_index, class_name, command_list, event_list in class_list:
        for event_index, event_typename in event_list:
            output_fp.write("            ({}, {}): self.handle_{},\n".format(class_index, event_index, event_typename))
    output_fp.write("        }\n\n")
    # Event dispatch methods
    for class_index, class_name, command_list, event_list in class_list:
        for event_index, event_typename in event_list:
            output_fp.write("    def handle_{}(self, event):\n".format(event_typename))
            output_fp.write("        pass\n")
    # Event dispatch
    output_fp.write("    def handle_event(self, event_id, event):\n")
    output_fp.write("        try:\n")
    output_fp.write("            method = self.event_type_map[event_id]\n")
    output_fp.write("            method(event)\n")
    output_fp.write("        except KeyError:\n")
    output_fp.write("            ## Unsupported event (log? handle_unsupported_event()?\n")
    output_fp.write("            pass\n\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("api_xml_path", help="Path to XML file describing BGAPI")

    args = parser.parse_args()

    with open(args.api_xml_path, "rb") as api_xml_fp:
        output_fp = sys.stdout

        document = xml.dom.minidom.parse(api_xml_fp)
        generate_api_from_document(document, output_fp)

if __name__ == "__main__":
    main()
