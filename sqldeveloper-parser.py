#!/usr/bin/env python3

# http://stackoverflow.com/questions/6677424/how-do-i-import-variable-packages-in-python-like-using-variable-variables-i
# https://github.com/kumzugloom/sqldeveloperpassworddecryptor # inspiration for the future

FILENAME_CONNECTIONS = '/home/pm/.sqldeveloper/system4.1.2.20.64/o.jdeveloper.db.connection.12.2.1.0.42.151001.541/connections.xml'
FILENAME_PREFERENCES = '/home/pm/.sqldeveloper/system4.1.2.20.64/o.sqldeveloper.12.2.0.20.64/product-preferences.xml'
PARSER_NAME = 'parser_by_lxml'  # 'parser' | 'parser_by_lxml' | 'parser_by_xmltodict'
VERSION = 4  # 3 | 4


def decrypt_connections(version, parsed_data):
    decrypt = getattr(__import__('decryptors.decryptor_{}'.format(version), fromlist=['']), 'decrypt')
    for connection in parsed_data.connections:
        connection['parameters']['.password'] = decrypt(
            connection['parameters']['password'],
            parsed_data.db_system_id,
        )
    return parsed_data.connections


def parse_data(parser_name):
    parser = getattr(__import__('parsers.{}'.format(parser_name), fromlist=['parser']), 'parser')
    return parser(
        filename_connections=FILENAME_CONNECTIONS,
        filename_preferences=FILENAME_PREFERENCES,
    )

if __name__ == '__main__':
    print('#', 'version={}'.format(VERSION), '++', 'parser_name={}'.format(PARSER_NAME))
    parsed_data = parse_data(parser_name=PARSER_NAME)
    decrypted_connections = decrypt_connections(version=VERSION, parsed_data=parsed_data)
    # from pprint import pprint;pprint(decrypted_connections)
    [print(c['parameters']['.password'], '\t', c['name']) for c in decrypted_connections]
