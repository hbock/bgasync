# This file is auto-generated. Edit at your own risk!
from struct import Struct
from collections import namedtuple
from enum import Enum
from .apibase import encode_command
from .apibase import Decodable

class event_system_boot(Decodable):
    decoded_type = namedtuple('event_system_boot_type', (
        'major',
        'minor',
        'patch',
        'build',
        'll_version',
        'protocol_version',
        'hw',
    ))
    decode_struct = Struct('<HHHHHBB')

class event_system_debug(Decodable):
    decoded_type = namedtuple('event_system_debug_type', (
        'data',
    ))
    decode_struct = Struct('<B')
    ends_with_uint8array = True

class event_system_endpoint_watermark_rx(Decodable):
    decoded_type = namedtuple('event_system_endpoint_watermark_rx_type', (
        'endpoint',
        'data',
    ))
    decode_struct = Struct('<BB')

class event_system_endpoint_watermark_tx(Decodable):
    decoded_type = namedtuple('event_system_endpoint_watermark_tx_type', (
        'endpoint',
        'data',
    ))
    decode_struct = Struct('<BB')

class event_system_script_failure(Decodable):
    decoded_type = namedtuple('event_system_script_failure_type', (
        'address',
        'reason',
    ))
    decode_struct = Struct('<HH')

class event_system_no_license_key(Decodable):
    decoded_type = namedtuple('event_system_no_license_key_type', (
    ))

class command_system_reset(namedtuple('command_system_reset', 'boot_in_dfu')):
   __slots__ = ()
   _id = (0, 0, 0)
   _struct = Struct('<B')
   _ends_with_uint8array = False

class command_system_hello(namedtuple('command_system_hello', '')):
   __slots__ = ()
   _id = (0, 0, 1)
   _struct = Struct('<')
   _ends_with_uint8array = False

class response_system_hello(Decodable):
    decoded_type = namedtuple('response_system_hello_type', (
    ))

class command_system_address_get(namedtuple('command_system_address_get', '')):
   __slots__ = ()
   _id = (0, 0, 2)
   _struct = Struct('<')
   _ends_with_uint8array = False

class response_system_address_get(Decodable):
    decoded_type = namedtuple('response_system_address_get_type', (
        'address',
    ))
    decode_struct = Struct('<6s')

class command_system_reg_write(namedtuple('command_system_reg_write', 'address value')):
   __slots__ = ()
   _id = (0, 0, 3)
   _struct = Struct('<HB')
   _ends_with_uint8array = False

class response_system_reg_write(Decodable):
    decoded_type = namedtuple('response_system_reg_write_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_system_reg_read(namedtuple('command_system_reg_read', 'address')):
   __slots__ = ()
   _id = (0, 0, 4)
   _struct = Struct('<H')
   _ends_with_uint8array = False

class response_system_reg_read(Decodable):
    decoded_type = namedtuple('response_system_reg_read_type', (
        'address',
        'value',
    ))
    decode_struct = Struct('<HB')

class command_system_get_counters(namedtuple('command_system_get_counters', '')):
   __slots__ = ()
   _id = (0, 0, 5)
   _struct = Struct('<')
   _ends_with_uint8array = False

class response_system_get_counters(Decodable):
    decoded_type = namedtuple('response_system_get_counters_type', (
        'txok',
        'txretry',
        'rxok',
        'rxfail',
        'mbuf',
    ))
    decode_struct = Struct('<BBBBB')

class command_system_get_connections(namedtuple('command_system_get_connections', '')):
   __slots__ = ()
   _id = (0, 0, 6)
   _struct = Struct('<')
   _ends_with_uint8array = False

class response_system_get_connections(Decodable):
    decoded_type = namedtuple('response_system_get_connections_type', (
        'maxconn',
    ))
    decode_struct = Struct('<B')

class command_system_read_memory(namedtuple('command_system_read_memory', 'address length')):
   __slots__ = ()
   _id = (0, 0, 7)
   _struct = Struct('<IB')
   _ends_with_uint8array = False

class response_system_read_memory(Decodable):
    decoded_type = namedtuple('response_system_read_memory_type', (
        'address',
        'data',
    ))
    decode_struct = Struct('<IB')
    ends_with_uint8array = True

class command_system_get_info(namedtuple('command_system_get_info', '')):
   __slots__ = ()
   _id = (0, 0, 8)
   _struct = Struct('<')
   _ends_with_uint8array = False

class response_system_get_info(Decodable):
    decoded_type = namedtuple('response_system_get_info_type', (
        'major',
        'minor',
        'patch',
        'build',
        'll_version',
        'protocol_version',
        'hw',
    ))
    decode_struct = Struct('<HHHHHBB')

class command_system_endpoint_tx(namedtuple('command_system_endpoint_tx', 'endpoint data')):
   __slots__ = ()
   _id = (0, 0, 9)
   _struct = Struct('<BB')
   _ends_with_uint8array = True

class response_system_endpoint_tx(Decodable):
    decoded_type = namedtuple('response_system_endpoint_tx_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_system_whitelist_append(namedtuple('command_system_whitelist_append', 'address address_type')):
   __slots__ = ()
   _id = (0, 0, 10)
   _struct = Struct('<6sB')
   _ends_with_uint8array = False

class response_system_whitelist_append(Decodable):
    decoded_type = namedtuple('response_system_whitelist_append_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_system_whitelist_remove(namedtuple('command_system_whitelist_remove', 'address address_type')):
   __slots__ = ()
   _id = (0, 0, 11)
   _struct = Struct('<6sB')
   _ends_with_uint8array = False

class response_system_whitelist_remove(Decodable):
    decoded_type = namedtuple('response_system_whitelist_remove_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_system_whitelist_clear(namedtuple('command_system_whitelist_clear', '')):
   __slots__ = ()
   _id = (0, 0, 12)
   _struct = Struct('<')
   _ends_with_uint8array = False

class response_system_whitelist_clear(Decodable):
    decoded_type = namedtuple('response_system_whitelist_clear_type', (
    ))

class command_system_endpoint_rx(namedtuple('command_system_endpoint_rx', 'endpoint size')):
   __slots__ = ()
   _id = (0, 0, 13)
   _struct = Struct('<BB')
   _ends_with_uint8array = False

class response_system_endpoint_rx(Decodable):
    decoded_type = namedtuple('response_system_endpoint_rx_type', (
        'result',
        'data',
    ))
    decode_struct = Struct('<HB')
    ends_with_uint8array = True

class command_system_endpoint_set_watermarks(namedtuple('command_system_endpoint_set_watermarks', 'endpoint rx tx')):
   __slots__ = ()
   _id = (0, 0, 14)
   _struct = Struct('<BBB')
   _ends_with_uint8array = False

class response_system_endpoint_set_watermarks(Decodable):
    decoded_type = namedtuple('response_system_endpoint_set_watermarks_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class system_endpoints(Enum):
    endpoint_api = 0
    endpoint_test = 1
    endpoint_script = 2
    endpoint_usb = 3
    endpoint_uart0 = 4
    endpoint_uart1 = 5


class event_flash_ps_key(Decodable):
    decoded_type = namedtuple('event_flash_ps_key_type', (
        'key',
        'value',
    ))
    decode_struct = Struct('<HB')
    ends_with_uint8array = True

class command_flash_ps_defrag(namedtuple('command_flash_ps_defrag', '')):
   __slots__ = ()
   _id = (0, 1, 0)
   _struct = Struct('<')
   _ends_with_uint8array = False

class response_flash_ps_defrag(Decodable):
    decoded_type = namedtuple('response_flash_ps_defrag_type', (
    ))

class command_flash_ps_dump(namedtuple('command_flash_ps_dump', '')):
   __slots__ = ()
   _id = (0, 1, 1)
   _struct = Struct('<')
   _ends_with_uint8array = False

class response_flash_ps_dump(Decodable):
    decoded_type = namedtuple('response_flash_ps_dump_type', (
    ))

class command_flash_ps_erase_all(namedtuple('command_flash_ps_erase_all', '')):
   __slots__ = ()
   _id = (0, 1, 2)
   _struct = Struct('<')
   _ends_with_uint8array = False

class response_flash_ps_erase_all(Decodable):
    decoded_type = namedtuple('response_flash_ps_erase_all_type', (
    ))

class command_flash_ps_save(namedtuple('command_flash_ps_save', 'key value')):
   __slots__ = ()
   _id = (0, 1, 3)
   _struct = Struct('<HB')
   _ends_with_uint8array = True

class response_flash_ps_save(Decodable):
    decoded_type = namedtuple('response_flash_ps_save_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_flash_ps_load(namedtuple('command_flash_ps_load', 'key')):
   __slots__ = ()
   _id = (0, 1, 4)
   _struct = Struct('<H')
   _ends_with_uint8array = False

class response_flash_ps_load(Decodable):
    decoded_type = namedtuple('response_flash_ps_load_type', (
        'result',
        'value',
    ))
    decode_struct = Struct('<HB')
    ends_with_uint8array = True

class command_flash_ps_erase(namedtuple('command_flash_ps_erase', 'key')):
   __slots__ = ()
   _id = (0, 1, 5)
   _struct = Struct('<H')
   _ends_with_uint8array = False

class response_flash_ps_erase(Decodable):
    decoded_type = namedtuple('response_flash_ps_erase_type', (
    ))

class command_flash_erase_page(namedtuple('command_flash_erase_page', 'page')):
   __slots__ = ()
   _id = (0, 1, 6)
   _struct = Struct('<B')
   _ends_with_uint8array = False

class response_flash_erase_page(Decodable):
    decoded_type = namedtuple('response_flash_erase_page_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_flash_write_words(namedtuple('command_flash_write_words', 'address words')):
   __slots__ = ()
   _id = (0, 1, 7)
   _struct = Struct('<HB')
   _ends_with_uint8array = True

class response_flash_write_words(Decodable):
    decoded_type = namedtuple('response_flash_write_words_type', (
    ))


class event_attributes_value(Decodable):
    decoded_type = namedtuple('event_attributes_value_type', (
        'connection',
        'reason',
        'handle',
        'offset',
        'value',
    ))
    decode_struct = Struct('<BBHHB')
    ends_with_uint8array = True

class event_attributes_user_read_request(Decodable):
    decoded_type = namedtuple('event_attributes_user_read_request_type', (
        'connection',
        'handle',
        'offset',
        'maxsize',
    ))
    decode_struct = Struct('<BHHB')

class event_attributes_status(Decodable):
    decoded_type = namedtuple('event_attributes_status_type', (
        'handle',
        'flags',
    ))
    decode_struct = Struct('<HB')

class command_attributes_write(namedtuple('command_attributes_write', 'handle offset value')):
   __slots__ = ()
   _id = (0, 2, 0)
   _struct = Struct('<HBB')
   _ends_with_uint8array = True

class response_attributes_write(Decodable):
    decoded_type = namedtuple('response_attributes_write_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_attributes_read(namedtuple('command_attributes_read', 'handle offset')):
   __slots__ = ()
   _id = (0, 2, 1)
   _struct = Struct('<HH')
   _ends_with_uint8array = False

class response_attributes_read(Decodable):
    decoded_type = namedtuple('response_attributes_read_type', (
        'handle',
        'offset',
        'result',
        'value',
    ))
    decode_struct = Struct('<HHHB')
    ends_with_uint8array = True

class command_attributes_read_type(namedtuple('command_attributes_read_type', 'handle')):
   __slots__ = ()
   _id = (0, 2, 2)
   _struct = Struct('<H')
   _ends_with_uint8array = False

class response_attributes_read_type(Decodable):
    decoded_type = namedtuple('response_attributes_read_type_type', (
        'handle',
        'result',
        'value',
    ))
    decode_struct = Struct('<HHB')
    ends_with_uint8array = True

class command_attributes_user_read_response(namedtuple('command_attributes_user_read_response', 'connection att_error value')):
   __slots__ = ()
   _id = (0, 2, 3)
   _struct = Struct('<BBB')
   _ends_with_uint8array = True

class response_attributes_user_read_response(Decodable):
    decoded_type = namedtuple('response_attributes_user_read_response_type', (
    ))

class command_attributes_user_write_response(namedtuple('command_attributes_user_write_response', 'connection att_error')):
   __slots__ = ()
   _id = (0, 2, 4)
   _struct = Struct('<BB')
   _ends_with_uint8array = False

class response_attributes_user_write_response(Decodable):
    decoded_type = namedtuple('response_attributes_user_write_response_type', (
    ))

class attributes_attribute_change_reason(Enum):
    write_request = 0
    write_command = 1
    write_request_user = 2

class attributes_attribute_status_flag(Enum):
    notify = 1
    indicate = 2


class event_connection_status(Decodable):
    decoded_type = namedtuple('event_connection_status_type', (
        'connection',
        'flags',
        'address',
        'address_type',
        'conn_interval',
        'timeout',
        'latency',
        'bonding',
    ))
    decode_struct = Struct('<BB6sBHHHB')

class event_connection_version_ind(Decodable):
    decoded_type = namedtuple('event_connection_version_ind_type', (
        'connection',
        'vers_nr',
        'comp_id',
        'sub_vers_nr',
    ))
    decode_struct = Struct('<BBHH')

class event_connection_feature_ind(Decodable):
    decoded_type = namedtuple('event_connection_feature_ind_type', (
        'connection',
        'features',
    ))
    decode_struct = Struct('<BB')
    ends_with_uint8array = True

class event_connection_raw_rx(Decodable):
    decoded_type = namedtuple('event_connection_raw_rx_type', (
        'connection',
        'data',
    ))
    decode_struct = Struct('<BB')
    ends_with_uint8array = True

class event_connection_disconnected(Decodable):
    decoded_type = namedtuple('event_connection_disconnected_type', (
        'connection',
        'reason',
    ))
    decode_struct = Struct('<BH')

class command_connection_disconnect(namedtuple('command_connection_disconnect', 'connection')):
   __slots__ = ()
   _id = (0, 3, 0)
   _struct = Struct('<B')
   _ends_with_uint8array = False

class response_connection_disconnect(Decodable):
    decoded_type = namedtuple('response_connection_disconnect_type', (
        'connection',
        'result',
    ))
    decode_struct = Struct('<BH')

class command_connection_get_rssi(namedtuple('command_connection_get_rssi', 'connection')):
   __slots__ = ()
   _id = (0, 3, 1)
   _struct = Struct('<B')
   _ends_with_uint8array = False

class response_connection_get_rssi(Decodable):
    decoded_type = namedtuple('response_connection_get_rssi_type', (
        'connection',
        'rssi',
    ))
    decode_struct = Struct('<Bb')

class command_connection_update(namedtuple('command_connection_update', 'connection interval_min interval_max latency timeout')):
   __slots__ = ()
   _id = (0, 3, 2)
   _struct = Struct('<BHHHH')
   _ends_with_uint8array = False

class response_connection_update(Decodable):
    decoded_type = namedtuple('response_connection_update_type', (
        'connection',
        'result',
    ))
    decode_struct = Struct('<BH')

class command_connection_version_update(namedtuple('command_connection_version_update', 'connection')):
   __slots__ = ()
   _id = (0, 3, 3)
   _struct = Struct('<B')
   _ends_with_uint8array = False

class response_connection_version_update(Decodable):
    decoded_type = namedtuple('response_connection_version_update_type', (
        'connection',
        'result',
    ))
    decode_struct = Struct('<BH')

class command_connection_channel_map_get(namedtuple('command_connection_channel_map_get', 'connection')):
   __slots__ = ()
   _id = (0, 3, 4)
   _struct = Struct('<B')
   _ends_with_uint8array = False

class response_connection_channel_map_get(Decodable):
    decoded_type = namedtuple('response_connection_channel_map_get_type', (
        'connection',
        'map',
    ))
    decode_struct = Struct('<BB')
    ends_with_uint8array = True

class command_connection_channel_map_set(namedtuple('command_connection_channel_map_set', 'connection map')):
   __slots__ = ()
   _id = (0, 3, 5)
   _struct = Struct('<BB')
   _ends_with_uint8array = True

class response_connection_channel_map_set(Decodable):
    decoded_type = namedtuple('response_connection_channel_map_set_type', (
        'connection',
        'result',
    ))
    decode_struct = Struct('<BH')

class command_connection_features_get(namedtuple('command_connection_features_get', 'connection')):
   __slots__ = ()
   _id = (0, 3, 6)
   _struct = Struct('<B')
   _ends_with_uint8array = False

class response_connection_features_get(Decodable):
    decoded_type = namedtuple('response_connection_features_get_type', (
        'connection',
        'result',
    ))
    decode_struct = Struct('<BH')

class command_connection_get_status(namedtuple('command_connection_get_status', 'connection')):
   __slots__ = ()
   _id = (0, 3, 7)
   _struct = Struct('<B')
   _ends_with_uint8array = False

class response_connection_get_status(Decodable):
    decoded_type = namedtuple('response_connection_get_status_type', (
        'connection',
    ))
    decode_struct = Struct('<B')

class command_connection_raw_tx(namedtuple('command_connection_raw_tx', 'connection data')):
   __slots__ = ()
   _id = (0, 3, 8)
   _struct = Struct('<BB')
   _ends_with_uint8array = True

class response_connection_raw_tx(Decodable):
    decoded_type = namedtuple('response_connection_raw_tx_type', (
        'connection',
    ))
    decode_struct = Struct('<B')

class connection_connstatus(Enum):
    connected = 1
    encrypted = 2
    completed = 4
    parameters_change = 8


class event_attclient_indicated(Decodable):
    decoded_type = namedtuple('event_attclient_indicated_type', (
        'connection',
        'attrhandle',
    ))
    decode_struct = Struct('<BH')

class event_attclient_procedure_completed(Decodable):
    decoded_type = namedtuple('event_attclient_procedure_completed_type', (
        'connection',
        'result',
        'chrhandle',
    ))
    decode_struct = Struct('<BHH')

class event_attclient_group_found(Decodable):
    decoded_type = namedtuple('event_attclient_group_found_type', (
        'connection',
        'start',
        'end',
        'uuid',
    ))
    decode_struct = Struct('<BHHB')
    ends_with_uint8array = True

class event_attclient_attribute_found(Decodable):
    decoded_type = namedtuple('event_attclient_attribute_found_type', (
        'connection',
        'chrdecl',
        'value',
        'properties',
        'uuid',
    ))
    decode_struct = Struct('<BHHBB')
    ends_with_uint8array = True

class event_attclient_find_information_found(Decodable):
    decoded_type = namedtuple('event_attclient_find_information_found_type', (
        'connection',
        'chrhandle',
        'uuid',
    ))
    decode_struct = Struct('<BHB')
    ends_with_uint8array = True

class event_attclient_attribute_value(Decodable):
    decoded_type = namedtuple('event_attclient_attribute_value_type', (
        'connection',
        'atthandle',
        'type',
        'value',
    ))
    decode_struct = Struct('<BHBB')
    ends_with_uint8array = True

class event_attclient_read_multiple_response(Decodable):
    decoded_type = namedtuple('event_attclient_read_multiple_response_type', (
        'connection',
        'handles',
    ))
    decode_struct = Struct('<BB')
    ends_with_uint8array = True

class command_attclient_find_by_type_value(namedtuple('command_attclient_find_by_type_value', 'connection start end uuid value')):
   __slots__ = ()
   _id = (0, 4, 0)
   _struct = Struct('<BHHHB')
   _ends_with_uint8array = True

class response_attclient_find_by_type_value(Decodable):
    decoded_type = namedtuple('response_attclient_find_by_type_value_type', (
        'connection',
        'result',
    ))
    decode_struct = Struct('<BH')

class command_attclient_read_by_group_type(namedtuple('command_attclient_read_by_group_type', 'connection start end uuid')):
   __slots__ = ()
   _id = (0, 4, 1)
   _struct = Struct('<BHHB')
   _ends_with_uint8array = True

class response_attclient_read_by_group_type(Decodable):
    decoded_type = namedtuple('response_attclient_read_by_group_type_type', (
        'connection',
        'result',
    ))
    decode_struct = Struct('<BH')

class command_attclient_read_by_type(namedtuple('command_attclient_read_by_type', 'connection start end uuid')):
   __slots__ = ()
   _id = (0, 4, 2)
   _struct = Struct('<BHHB')
   _ends_with_uint8array = True

class response_attclient_read_by_type(Decodable):
    decoded_type = namedtuple('response_attclient_read_by_type_type', (
        'connection',
        'result',
    ))
    decode_struct = Struct('<BH')

class command_attclient_find_information(namedtuple('command_attclient_find_information', 'connection start end')):
   __slots__ = ()
   _id = (0, 4, 3)
   _struct = Struct('<BHH')
   _ends_with_uint8array = False

class response_attclient_find_information(Decodable):
    decoded_type = namedtuple('response_attclient_find_information_type', (
        'connection',
        'result',
    ))
    decode_struct = Struct('<BH')

class command_attclient_read_by_handle(namedtuple('command_attclient_read_by_handle', 'connection chrhandle')):
   __slots__ = ()
   _id = (0, 4, 4)
   _struct = Struct('<BH')
   _ends_with_uint8array = False

class response_attclient_read_by_handle(Decodable):
    decoded_type = namedtuple('response_attclient_read_by_handle_type', (
        'connection',
        'result',
    ))
    decode_struct = Struct('<BH')

class command_attclient_attribute_write(namedtuple('command_attclient_attribute_write', 'connection atthandle data')):
   __slots__ = ()
   _id = (0, 4, 5)
   _struct = Struct('<BHB')
   _ends_with_uint8array = True

class response_attclient_attribute_write(Decodable):
    decoded_type = namedtuple('response_attclient_attribute_write_type', (
        'connection',
        'result',
    ))
    decode_struct = Struct('<BH')

class command_attclient_write_command(namedtuple('command_attclient_write_command', 'connection atthandle data')):
   __slots__ = ()
   _id = (0, 4, 6)
   _struct = Struct('<BHB')
   _ends_with_uint8array = True

class response_attclient_write_command(Decodable):
    decoded_type = namedtuple('response_attclient_write_command_type', (
        'connection',
        'result',
    ))
    decode_struct = Struct('<BH')

class command_attclient_indicate_confirm(namedtuple('command_attclient_indicate_confirm', 'connection')):
   __slots__ = ()
   _id = (0, 4, 7)
   _struct = Struct('<B')
   _ends_with_uint8array = False

class response_attclient_indicate_confirm(Decodable):
    decoded_type = namedtuple('response_attclient_indicate_confirm_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_attclient_read_long(namedtuple('command_attclient_read_long', 'connection chrhandle')):
   __slots__ = ()
   _id = (0, 4, 8)
   _struct = Struct('<BH')
   _ends_with_uint8array = False

class response_attclient_read_long(Decodable):
    decoded_type = namedtuple('response_attclient_read_long_type', (
        'connection',
        'result',
    ))
    decode_struct = Struct('<BH')

class command_attclient_prepare_write(namedtuple('command_attclient_prepare_write', 'connection atthandle offset data')):
   __slots__ = ()
   _id = (0, 4, 9)
   _struct = Struct('<BHHB')
   _ends_with_uint8array = True

class response_attclient_prepare_write(Decodable):
    decoded_type = namedtuple('response_attclient_prepare_write_type', (
        'connection',
        'result',
    ))
    decode_struct = Struct('<BH')

class command_attclient_execute_write(namedtuple('command_attclient_execute_write', 'connection commit')):
   __slots__ = ()
   _id = (0, 4, 10)
   _struct = Struct('<BB')
   _ends_with_uint8array = False

class response_attclient_execute_write(Decodable):
    decoded_type = namedtuple('response_attclient_execute_write_type', (
        'connection',
        'result',
    ))
    decode_struct = Struct('<BH')

class command_attclient_read_multiple(namedtuple('command_attclient_read_multiple', 'connection handles')):
   __slots__ = ()
   _id = (0, 4, 11)
   _struct = Struct('<BB')
   _ends_with_uint8array = True

class response_attclient_read_multiple(Decodable):
    decoded_type = namedtuple('response_attclient_read_multiple_type', (
        'connection',
        'result',
    ))
    decode_struct = Struct('<BH')

class attclient_attribute_value_types(Enum):
    attribute_value_type_read = 0
    attribute_value_type_notify = 1
    attribute_value_type_indicate = 2
    attribute_value_type_read_by_type = 3
    attribute_value_type_read_blob = 4
    attribute_value_type_indicate_rsp_req = 5


class event_sm_smp_data(Decodable):
    decoded_type = namedtuple('event_sm_smp_data_type', (
        'handle',
        'packet',
        'data',
    ))
    decode_struct = Struct('<BBB')
    ends_with_uint8array = True

class event_sm_bonding_fail(Decodable):
    decoded_type = namedtuple('event_sm_bonding_fail_type', (
        'handle',
        'result',
    ))
    decode_struct = Struct('<BH')

class event_sm_passkey_display(Decodable):
    decoded_type = namedtuple('event_sm_passkey_display_type', (
        'handle',
        'passkey',
    ))
    decode_struct = Struct('<BI')

class event_sm_passkey_request(Decodable):
    decoded_type = namedtuple('event_sm_passkey_request_type', (
        'handle',
    ))
    decode_struct = Struct('<B')

class event_sm_bond_status(Decodable):
    decoded_type = namedtuple('event_sm_bond_status_type', (
        'bond',
        'keysize',
        'mitm',
        'keys',
    ))
    decode_struct = Struct('<BBBB')

class command_sm_encrypt_start(namedtuple('command_sm_encrypt_start', 'handle bonding')):
   __slots__ = ()
   _id = (0, 5, 0)
   _struct = Struct('<BB')
   _ends_with_uint8array = False

class response_sm_encrypt_start(Decodable):
    decoded_type = namedtuple('response_sm_encrypt_start_type', (
        'handle',
        'result',
    ))
    decode_struct = Struct('<BH')

class command_sm_set_bondable_mode(namedtuple('command_sm_set_bondable_mode', 'bondable')):
   __slots__ = ()
   _id = (0, 5, 1)
   _struct = Struct('<B')
   _ends_with_uint8array = False

class response_sm_set_bondable_mode(Decodable):
    decoded_type = namedtuple('response_sm_set_bondable_mode_type', (
    ))

class command_sm_delete_bonding(namedtuple('command_sm_delete_bonding', 'handle')):
   __slots__ = ()
   _id = (0, 5, 2)
   _struct = Struct('<B')
   _ends_with_uint8array = False

class response_sm_delete_bonding(Decodable):
    decoded_type = namedtuple('response_sm_delete_bonding_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_sm_set_parameters(namedtuple('command_sm_set_parameters', 'mitm min_key_size io_capabilities')):
   __slots__ = ()
   _id = (0, 5, 3)
   _struct = Struct('<BBB')
   _ends_with_uint8array = False

class response_sm_set_parameters(Decodable):
    decoded_type = namedtuple('response_sm_set_parameters_type', (
    ))

class command_sm_passkey_entry(namedtuple('command_sm_passkey_entry', 'handle passkey')):
   __slots__ = ()
   _id = (0, 5, 4)
   _struct = Struct('<BI')
   _ends_with_uint8array = False

class response_sm_passkey_entry(Decodable):
    decoded_type = namedtuple('response_sm_passkey_entry_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_sm_get_bonds(namedtuple('command_sm_get_bonds', '')):
   __slots__ = ()
   _id = (0, 5, 5)
   _struct = Struct('<')
   _ends_with_uint8array = False

class response_sm_get_bonds(Decodable):
    decoded_type = namedtuple('response_sm_get_bonds_type', (
        'bonds',
    ))
    decode_struct = Struct('<B')

class command_sm_set_oob_data(namedtuple('command_sm_set_oob_data', 'oob')):
   __slots__ = ()
   _id = (0, 5, 6)
   _struct = Struct('<B')
   _ends_with_uint8array = True

class response_sm_set_oob_data(Decodable):
    decoded_type = namedtuple('response_sm_set_oob_data_type', (
    ))

class sm_bonding_key(Enum):
    ltk = 0x01
    addr_public = 0x02
    addr_static = 0x04
    irk = 0x08
    edivrand = 0x10
    csrk = 0x20
    masterid = 0x40

class sm_io_capability(Enum):
    displayonly = 0
    displayyesno = 1
    keyboardonly = 2
    noinputnooutput = 3
    keyboarddisplay = 4


class event_gap_scan_response(Decodable):
    decoded_type = namedtuple('event_gap_scan_response_type', (
        'rssi',
        'packet_type',
        'sender',
        'address_type',
        'bond',
        'data',
    ))
    decode_struct = Struct('<bB6sBBB')
    ends_with_uint8array = True

class event_gap_mode_changed(Decodable):
    decoded_type = namedtuple('event_gap_mode_changed_type', (
        'discover',
        'connect',
    ))
    decode_struct = Struct('<BB')

class command_gap_set_privacy_flags(namedtuple('command_gap_set_privacy_flags', 'peripheral_privacy central_privacy')):
   __slots__ = ()
   _id = (0, 6, 0)
   _struct = Struct('<BB')
   _ends_with_uint8array = False

class response_gap_set_privacy_flags(Decodable):
    decoded_type = namedtuple('response_gap_set_privacy_flags_type', (
    ))

class command_gap_set_mode(namedtuple('command_gap_set_mode', 'discover connect')):
   __slots__ = ()
   _id = (0, 6, 1)
   _struct = Struct('<BB')
   _ends_with_uint8array = False

class response_gap_set_mode(Decodable):
    decoded_type = namedtuple('response_gap_set_mode_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_gap_discover(namedtuple('command_gap_discover', 'mode')):
   __slots__ = ()
   _id = (0, 6, 2)
   _struct = Struct('<B')
   _ends_with_uint8array = False

class response_gap_discover(Decodable):
    decoded_type = namedtuple('response_gap_discover_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_gap_connect_direct(namedtuple('command_gap_connect_direct', 'address addr_type conn_interval_min conn_interval_max timeout latency')):
   __slots__ = ()
   _id = (0, 6, 3)
   _struct = Struct('<6sBHHHH')
   _ends_with_uint8array = False

class response_gap_connect_direct(Decodable):
    decoded_type = namedtuple('response_gap_connect_direct_type', (
        'result',
        'connection_handle',
    ))
    decode_struct = Struct('<HB')

class command_gap_end_procedure(namedtuple('command_gap_end_procedure', '')):
   __slots__ = ()
   _id = (0, 6, 4)
   _struct = Struct('<')
   _ends_with_uint8array = False

class response_gap_end_procedure(Decodable):
    decoded_type = namedtuple('response_gap_end_procedure_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_gap_connect_selective(namedtuple('command_gap_connect_selective', 'conn_interval_min conn_interval_max timeout latency')):
   __slots__ = ()
   _id = (0, 6, 5)
   _struct = Struct('<HHHH')
   _ends_with_uint8array = False

class response_gap_connect_selective(Decodable):
    decoded_type = namedtuple('response_gap_connect_selective_type', (
        'result',
        'connection_handle',
    ))
    decode_struct = Struct('<HB')

class command_gap_set_filtering(namedtuple('command_gap_set_filtering', 'scan_policy adv_policy scan_duplicate_filtering')):
   __slots__ = ()
   _id = (0, 6, 6)
   _struct = Struct('<BBB')
   _ends_with_uint8array = False

class response_gap_set_filtering(Decodable):
    decoded_type = namedtuple('response_gap_set_filtering_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_gap_set_scan_parameters(namedtuple('command_gap_set_scan_parameters', 'scan_interval scan_window active')):
   __slots__ = ()
   _id = (0, 6, 7)
   _struct = Struct('<HHB')
   _ends_with_uint8array = False

class response_gap_set_scan_parameters(Decodable):
    decoded_type = namedtuple('response_gap_set_scan_parameters_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_gap_set_adv_parameters(namedtuple('command_gap_set_adv_parameters', 'adv_interval_min adv_interval_max adv_channels')):
   __slots__ = ()
   _id = (0, 6, 8)
   _struct = Struct('<HHB')
   _ends_with_uint8array = False

class response_gap_set_adv_parameters(Decodable):
    decoded_type = namedtuple('response_gap_set_adv_parameters_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_gap_set_adv_data(namedtuple('command_gap_set_adv_data', 'set_scanrsp adv_data')):
   __slots__ = ()
   _id = (0, 6, 9)
   _struct = Struct('<BB')
   _ends_with_uint8array = True

class response_gap_set_adv_data(Decodable):
    decoded_type = namedtuple('response_gap_set_adv_data_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_gap_set_directed_connectable_mode(namedtuple('command_gap_set_directed_connectable_mode', 'address addr_type')):
   __slots__ = ()
   _id = (0, 6, 10)
   _struct = Struct('<6sB')
   _ends_with_uint8array = False

class response_gap_set_directed_connectable_mode(Decodable):
    decoded_type = namedtuple('response_gap_set_directed_connectable_mode_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class gap_address_type(Enum):
    public = 0
    random = 1

class gap_discoverable_mode(Enum):
    non_discoverable = 0
    limited_discoverable = 1
    general_discoverable = 2
    broadcast = 3
    user_data = 4

class gap_connectable_mode(Enum):
    non_connectable = 0
    directed_connectable = 1
    undirected_connectable = 2
    scannable_connectable = 3

class gap_discover_mode(Enum):
    discover_limited = 0
    discover_generic = 1
    discover_observation = 2

class gap_ad_types(Enum):
    ad_type_none = 0
    ad_type_flags = 1
    ad_type_services_16bit_more = 2
    ad_type_services_16bit_all = 3
    ad_type_services_32bit_more = 4
    ad_type_services_32bit_all = 5
    ad_type_services_128bit_more = 6
    ad_type_services_128bit_all = 7
    ad_type_localname_short = 8
    ad_type_localname_complete = 9
    ad_type_txpower = 10

class gap_advertising_policy(Enum):
    adv_policy_all = 0
    adv_policy_whitelist_scan = 1
    adv_policy_whitelist_connect = 2
    adv_policy_whitelist_all = 3

class gap_scan_policy(Enum):
    all = 0
    whitelist = 1


class event_hardware_io_port_status(Decodable):
    decoded_type = namedtuple('event_hardware_io_port_status_type', (
        'timestamp',
        'port',
        'irq',
        'state',
    ))
    decode_struct = Struct('<IBBB')

class event_hardware_soft_timer(Decodable):
    decoded_type = namedtuple('event_hardware_soft_timer_type', (
        'handle',
    ))
    decode_struct = Struct('<B')

class event_hardware_adc_result(Decodable):
    decoded_type = namedtuple('event_hardware_adc_result_type', (
        'input',
        'value',
    ))
    decode_struct = Struct('<Bh')

class command_hardware_io_port_config_irq(namedtuple('command_hardware_io_port_config_irq', 'port enable_bits falling_edge')):
   __slots__ = ()
   _id = (0, 7, 0)
   _struct = Struct('<BBB')
   _ends_with_uint8array = False

class response_hardware_io_port_config_irq(Decodable):
    decoded_type = namedtuple('response_hardware_io_port_config_irq_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_hardware_set_soft_timer(namedtuple('command_hardware_set_soft_timer', 'time handle single_shot')):
   __slots__ = ()
   _id = (0, 7, 1)
   _struct = Struct('<IBB')
   _ends_with_uint8array = False

class response_hardware_set_soft_timer(Decodable):
    decoded_type = namedtuple('response_hardware_set_soft_timer_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_hardware_adc_read(namedtuple('command_hardware_adc_read', 'input decimation reference_selection')):
   __slots__ = ()
   _id = (0, 7, 2)
   _struct = Struct('<BBB')
   _ends_with_uint8array = False

class response_hardware_adc_read(Decodable):
    decoded_type = namedtuple('response_hardware_adc_read_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_hardware_io_port_config_direction(namedtuple('command_hardware_io_port_config_direction', 'port direction')):
   __slots__ = ()
   _id = (0, 7, 3)
   _struct = Struct('<BB')
   _ends_with_uint8array = False

class response_hardware_io_port_config_direction(Decodable):
    decoded_type = namedtuple('response_hardware_io_port_config_direction_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_hardware_io_port_config_function(namedtuple('command_hardware_io_port_config_function', 'port function')):
   __slots__ = ()
   _id = (0, 7, 4)
   _struct = Struct('<BB')
   _ends_with_uint8array = False

class response_hardware_io_port_config_function(Decodable):
    decoded_type = namedtuple('response_hardware_io_port_config_function_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_hardware_io_port_config_pull(namedtuple('command_hardware_io_port_config_pull', 'port tristate_mask pull_up')):
   __slots__ = ()
   _id = (0, 7, 5)
   _struct = Struct('<BBB')
   _ends_with_uint8array = False

class response_hardware_io_port_config_pull(Decodable):
    decoded_type = namedtuple('response_hardware_io_port_config_pull_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_hardware_io_port_write(namedtuple('command_hardware_io_port_write', 'port mask data')):
   __slots__ = ()
   _id = (0, 7, 6)
   _struct = Struct('<BBB')
   _ends_with_uint8array = False

class response_hardware_io_port_write(Decodable):
    decoded_type = namedtuple('response_hardware_io_port_write_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_hardware_io_port_read(namedtuple('command_hardware_io_port_read', 'port mask')):
   __slots__ = ()
   _id = (0, 7, 7)
   _struct = Struct('<BB')
   _ends_with_uint8array = False

class response_hardware_io_port_read(Decodable):
    decoded_type = namedtuple('response_hardware_io_port_read_type', (
        'result',
        'port',
        'data',
    ))
    decode_struct = Struct('<HBB')

class command_hardware_spi_config(namedtuple('command_hardware_spi_config', 'channel polarity phase bit_order baud_e baud_m')):
   __slots__ = ()
   _id = (0, 7, 8)
   _struct = Struct('<BBBBBB')
   _ends_with_uint8array = False

class response_hardware_spi_config(Decodable):
    decoded_type = namedtuple('response_hardware_spi_config_type', (
        'result',
    ))
    decode_struct = Struct('<H')

class command_hardware_spi_transfer(namedtuple('command_hardware_spi_transfer', 'channel data')):
   __slots__ = ()
   _id = (0, 7, 9)
   _struct = Struct('<BB')
   _ends_with_uint8array = True

class response_hardware_spi_transfer(Decodable):
    decoded_type = namedtuple('response_hardware_spi_transfer_type', (
        'result',
        'channel',
        'data',
    ))
    decode_struct = Struct('<HBB')
    ends_with_uint8array = True

class command_hardware_i2c_read(namedtuple('command_hardware_i2c_read', 'address stop length')):
   __slots__ = ()
   _id = (0, 7, 10)
   _struct = Struct('<BBB')
   _ends_with_uint8array = False

class response_hardware_i2c_read(Decodable):
    decoded_type = namedtuple('response_hardware_i2c_read_type', (
        'result',
        'data',
    ))
    decode_struct = Struct('<HB')
    ends_with_uint8array = True

class command_hardware_i2c_write(namedtuple('command_hardware_i2c_write', 'address stop data')):
   __slots__ = ()
   _id = (0, 7, 11)
   _struct = Struct('<BBB')
   _ends_with_uint8array = True

class response_hardware_i2c_write(Decodable):
    decoded_type = namedtuple('response_hardware_i2c_write_type', (
        'written',
    ))
    decode_struct = Struct('<B')

class command_hardware_set_txpower(namedtuple('command_hardware_set_txpower', 'power')):
   __slots__ = ()
   _id = (0, 7, 12)
   _struct = Struct('<B')
   _ends_with_uint8array = False

class response_hardware_set_txpower(Decodable):
    decoded_type = namedtuple('response_hardware_set_txpower_type', (
    ))

class command_hardware_timer_comparator(namedtuple('command_hardware_timer_comparator', 'timer channel mode comparator_value')):
   __slots__ = ()
   _id = (0, 7, 13)
   _struct = Struct('<BBBH')
   _ends_with_uint8array = False

class response_hardware_timer_comparator(Decodable):
    decoded_type = namedtuple('response_hardware_timer_comparator_type', (
        'result',
    ))
    decode_struct = Struct('<H')


class command_test_phy_tx(namedtuple('command_test_phy_tx', 'channel length type')):
   __slots__ = ()
   _id = (0, 8, 0)
   _struct = Struct('<BBB')
   _ends_with_uint8array = False

class response_test_phy_tx(Decodable):
    decoded_type = namedtuple('response_test_phy_tx_type', (
    ))

class command_test_phy_rx(namedtuple('command_test_phy_rx', 'channel')):
   __slots__ = ()
   _id = (0, 8, 1)
   _struct = Struct('<B')
   _ends_with_uint8array = False

class response_test_phy_rx(Decodable):
    decoded_type = namedtuple('response_test_phy_rx_type', (
    ))

class command_test_phy_end(namedtuple('command_test_phy_end', '')):
   __slots__ = ()
   _id = (0, 8, 2)
   _struct = Struct('<')
   _ends_with_uint8array = False

class response_test_phy_end(Decodable):
    decoded_type = namedtuple('response_test_phy_end_type', (
        'counter',
    ))
    decode_struct = Struct('<H')

class command_test_phy_reset(namedtuple('command_test_phy_reset', '')):
   __slots__ = ()
   _id = (0, 8, 3)
   _struct = Struct('<')
   _ends_with_uint8array = False

class response_test_phy_reset(Decodable):
    decoded_type = namedtuple('response_test_phy_reset_type', (
    ))

class command_test_get_channel_map(namedtuple('command_test_get_channel_map', '')):
   __slots__ = ()
   _id = (0, 8, 4)
   _struct = Struct('<')
   _ends_with_uint8array = False

class response_test_get_channel_map(Decodable):
    decoded_type = namedtuple('response_test_get_channel_map_type', (
        'channel_map',
    ))
    decode_struct = Struct('<B')
    ends_with_uint8array = True

class command_test_debug(namedtuple('command_test_debug', 'input')):
   __slots__ = ()
   _id = (0, 8, 5)
   _struct = Struct('<B')
   _ends_with_uint8array = True

class response_test_debug(Decodable):
    decoded_type = namedtuple('response_test_debug_type', (
        'output',
    ))
    decode_struct = Struct('<B')
    ends_with_uint8array = True


CLASS_NAME_MAP = {
    0: 'system',
    1: 'flash',
    2: 'attributes',
    3: 'connection',
    4: 'attclient',
    5: 'sm',
    6: 'gap',
    7: 'hardware',
    8: 'test',
}

EVENT_TYPE_MAP = {
    (0, 0): event_system_boot,
    (0, 1): event_system_debug,
    (0, 2): event_system_endpoint_watermark_rx,
    (0, 3): event_system_endpoint_watermark_tx,
    (0, 4): event_system_script_failure,
    (0, 5): event_system_no_license_key,
    (1, 0): event_flash_ps_key,
    (2, 0): event_attributes_value,
    (2, 1): event_attributes_user_read_request,
    (2, 2): event_attributes_status,
    (3, 0): event_connection_status,
    (3, 1): event_connection_version_ind,
    (3, 2): event_connection_feature_ind,
    (3, 3): event_connection_raw_rx,
    (3, 4): event_connection_disconnected,
    (4, 0): event_attclient_indicated,
    (4, 1): event_attclient_procedure_completed,
    (4, 2): event_attclient_group_found,
    (4, 3): event_attclient_attribute_found,
    (4, 4): event_attclient_find_information_found,
    (4, 5): event_attclient_attribute_value,
    (4, 6): event_attclient_read_multiple_response,
    (5, 0): event_sm_smp_data,
    (5, 1): event_sm_bonding_fail,
    (5, 2): event_sm_passkey_display,
    (5, 3): event_sm_passkey_request,
    (5, 4): event_sm_bond_status,
    (6, 0): event_gap_scan_response,
    (6, 1): event_gap_mode_changed,
    (7, 0): event_hardware_io_port_status,
    (7, 1): event_hardware_soft_timer,
    (7, 2): event_hardware_adc_result,
}

COMMAND_RETURN_TYPE_MAP = {
    (0, 1): response_system_hello,
    (0, 2): response_system_address_get,
    (0, 3): response_system_reg_write,
    (0, 4): response_system_reg_read,
    (0, 5): response_system_get_counters,
    (0, 6): response_system_get_connections,
    (0, 7): response_system_read_memory,
    (0, 8): response_system_get_info,
    (0, 9): response_system_endpoint_tx,
    (0, 10): response_system_whitelist_append,
    (0, 11): response_system_whitelist_remove,
    (0, 12): response_system_whitelist_clear,
    (0, 13): response_system_endpoint_rx,
    (0, 14): response_system_endpoint_set_watermarks,
    (1, 0): response_flash_ps_defrag,
    (1, 1): response_flash_ps_dump,
    (1, 2): response_flash_ps_erase_all,
    (1, 3): response_flash_ps_save,
    (1, 4): response_flash_ps_load,
    (1, 5): response_flash_ps_erase,
    (1, 6): response_flash_erase_page,
    (1, 7): response_flash_write_words,
    (2, 0): response_attributes_write,
    (2, 1): response_attributes_read,
    (2, 2): response_attributes_read_type,
    (2, 3): response_attributes_user_read_response,
    (2, 4): response_attributes_user_write_response,
    (3, 0): response_connection_disconnect,
    (3, 1): response_connection_get_rssi,
    (3, 2): response_connection_update,
    (3, 3): response_connection_version_update,
    (3, 4): response_connection_channel_map_get,
    (3, 5): response_connection_channel_map_set,
    (3, 6): response_connection_features_get,
    (3, 7): response_connection_get_status,
    (3, 8): response_connection_raw_tx,
    (4, 0): response_attclient_find_by_type_value,
    (4, 1): response_attclient_read_by_group_type,
    (4, 2): response_attclient_read_by_type,
    (4, 3): response_attclient_find_information,
    (4, 4): response_attclient_read_by_handle,
    (4, 5): response_attclient_attribute_write,
    (4, 6): response_attclient_write_command,
    (4, 7): response_attclient_indicate_confirm,
    (4, 8): response_attclient_read_long,
    (4, 9): response_attclient_prepare_write,
    (4, 10): response_attclient_execute_write,
    (4, 11): response_attclient_read_multiple,
    (5, 0): response_sm_encrypt_start,
    (5, 1): response_sm_set_bondable_mode,
    (5, 2): response_sm_delete_bonding,
    (5, 3): response_sm_set_parameters,
    (5, 4): response_sm_passkey_entry,
    (5, 5): response_sm_get_bonds,
    (5, 6): response_sm_set_oob_data,
    (6, 0): response_gap_set_privacy_flags,
    (6, 1): response_gap_set_mode,
    (6, 2): response_gap_discover,
    (6, 3): response_gap_connect_direct,
    (6, 4): response_gap_end_procedure,
    (6, 5): response_gap_connect_selective,
    (6, 6): response_gap_set_filtering,
    (6, 7): response_gap_set_scan_parameters,
    (6, 8): response_gap_set_adv_parameters,
    (6, 9): response_gap_set_adv_data,
    (6, 10): response_gap_set_directed_connectable_mode,
    (7, 0): response_hardware_io_port_config_irq,
    (7, 1): response_hardware_set_soft_timer,
    (7, 2): response_hardware_adc_read,
    (7, 3): response_hardware_io_port_config_direction,
    (7, 4): response_hardware_io_port_config_function,
    (7, 5): response_hardware_io_port_config_pull,
    (7, 6): response_hardware_io_port_write,
    (7, 7): response_hardware_io_port_read,
    (7, 8): response_hardware_spi_config,
    (7, 9): response_hardware_spi_transfer,
    (7, 10): response_hardware_i2c_read,
    (7, 11): response_hardware_i2c_write,
    (7, 12): response_hardware_set_txpower,
    (7, 13): response_hardware_timer_comparator,
    (8, 0): response_test_phy_tx,
    (8, 1): response_test_phy_rx,
    (8, 2): response_test_phy_end,
    (8, 3): response_test_phy_reset,
    (8, 4): response_test_get_channel_map,
    (8, 5): response_test_debug,
}

class EventDecoderMixin(object):
    def __init__(self):
        self.event_type_map = {
            (0, 0): self.handle_event_system_boot,
            (0, 1): self.handle_event_system_debug,
            (0, 2): self.handle_event_system_endpoint_watermark_rx,
            (0, 3): self.handle_event_system_endpoint_watermark_tx,
            (0, 4): self.handle_event_system_script_failure,
            (0, 5): self.handle_event_system_no_license_key,
            (1, 0): self.handle_event_flash_ps_key,
            (2, 0): self.handle_event_attributes_value,
            (2, 1): self.handle_event_attributes_user_read_request,
            (2, 2): self.handle_event_attributes_status,
            (3, 0): self.handle_event_connection_status,
            (3, 1): self.handle_event_connection_version_ind,
            (3, 2): self.handle_event_connection_feature_ind,
            (3, 3): self.handle_event_connection_raw_rx,
            (3, 4): self.handle_event_connection_disconnected,
            (4, 0): self.handle_event_attclient_indicated,
            (4, 1): self.handle_event_attclient_procedure_completed,
            (4, 2): self.handle_event_attclient_group_found,
            (4, 3): self.handle_event_attclient_attribute_found,
            (4, 4): self.handle_event_attclient_find_information_found,
            (4, 5): self.handle_event_attclient_attribute_value,
            (4, 6): self.handle_event_attclient_read_multiple_response,
            (5, 0): self.handle_event_sm_smp_data,
            (5, 1): self.handle_event_sm_bonding_fail,
            (5, 2): self.handle_event_sm_passkey_display,
            (5, 3): self.handle_event_sm_passkey_request,
            (5, 4): self.handle_event_sm_bond_status,
            (6, 0): self.handle_event_gap_scan_response,
            (6, 1): self.handle_event_gap_mode_changed,
            (7, 0): self.handle_event_hardware_io_port_status,
            (7, 1): self.handle_event_hardware_soft_timer,
            (7, 2): self.handle_event_hardware_adc_result,
        }

    def handle_event_system_boot(self, event):
        pass
    def handle_event_system_debug(self, event):
        pass
    def handle_event_system_endpoint_watermark_rx(self, event):
        pass
    def handle_event_system_endpoint_watermark_tx(self, event):
        pass
    def handle_event_system_script_failure(self, event):
        pass
    def handle_event_system_no_license_key(self, event):
        pass
    def handle_event_flash_ps_key(self, event):
        pass
    def handle_event_attributes_value(self, event):
        pass
    def handle_event_attributes_user_read_request(self, event):
        pass
    def handle_event_attributes_status(self, event):
        pass
    def handle_event_connection_status(self, event):
        pass
    def handle_event_connection_version_ind(self, event):
        pass
    def handle_event_connection_feature_ind(self, event):
        pass
    def handle_event_connection_raw_rx(self, event):
        pass
    def handle_event_connection_disconnected(self, event):
        pass
    def handle_event_attclient_indicated(self, event):
        pass
    def handle_event_attclient_procedure_completed(self, event):
        pass
    def handle_event_attclient_group_found(self, event):
        pass
    def handle_event_attclient_attribute_found(self, event):
        pass
    def handle_event_attclient_find_information_found(self, event):
        pass
    def handle_event_attclient_attribute_value(self, event):
        pass
    def handle_event_attclient_read_multiple_response(self, event):
        pass
    def handle_event_sm_smp_data(self, event):
        pass
    def handle_event_sm_bonding_fail(self, event):
        pass
    def handle_event_sm_passkey_display(self, event):
        pass
    def handle_event_sm_passkey_request(self, event):
        pass
    def handle_event_sm_bond_status(self, event):
        pass
    def handle_event_gap_scan_response(self, event):
        pass
    def handle_event_gap_mode_changed(self, event):
        pass
    def handle_event_hardware_io_port_status(self, event):
        pass
    def handle_event_hardware_soft_timer(self, event):
        pass
    def handle_event_hardware_adc_result(self, event):
        pass
    def handle_event(self, event_id, event):
        try:
            method = self.event_type_map[event_id]
            method(event)
        except KeyError:
            ## Unsupported event (log? handle_unsupported_event()?
            pass

