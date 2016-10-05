#!/usr/bin/env python3

# http://stackoverflow.com/questions/6677424/how-do-i-import-variable-packages-in-python-like-using-variable-variables-i
# https://github.com/kumzugloom/sqldeveloperpassworddecryptor # inspiration for the future
# https://github.com/nd-net/sqldeveloperpassworddecryptor # inspiration for the future

from pprint import pprint as pp

# FILENAME_CONNECTIONS = '~/.sqldeveloper/system4.1.2.20.64/o.jdeveloper.db.connection.12.2.1.0.42.151001.541/connections.xml'
FILENAME_CONNECTIONS = '~/.sqldeveloper/system4.1.5.21.78/o.jdeveloper.db.connection.12.2.1.0.42.151001.541/connections.xml'
# FILENAME_PREFERENCES = '~/.sqldeveloper/system4.1.2.20.64/o.sqldeveloper.12.2.0.20.64/product-preferences.xml'
FILENAME_PREFERENCES = '~/.sqldeveloper/system4.1.5.21.78/o.sqldeveloper.12.2.0.21.78/product-preferences.xml'
PARSER_NAME = 'parser_by_lxml'  # 'parser' | 'parser_by_lxml' | 'parser_by_xmltodict'
VERSION = 4  # 3 | 4


def decrypt_connections(version, parsed_data):
    decrypt = getattr(__import__('decryptors.decryptor_{}'.format(version), fromlist=['']), 'decrypt')
    for connection in parsed_data.connections:
        try:
            connection['parameters']['.password'] = decrypt(
                connection['parameters']['password'],
                parsed_data.db_system_id,
            )
        except:
            connection['parameters']['.password'] = None
    return parsed_data.connections


def parse_data(parser_name):
    parser = getattr(__import__('parsers.{}'.format(parser_name), fromlist=['parser']), 'parser')
    return parser(
        filename_connections=FILENAME_CONNECTIONS,
        filename_preferences=FILENAME_PREFERENCES,
    )


def pp_header(parsed_data, decrypted_connections):
    print('#', 'version={}'.format(VERSION), '++', 'parser_name={}'.format(PARSER_NAME))


def pp_passwords(parsed_data, decrypted_connections):
    [print(c['parameters']['.password'], '\t', c['name']) for c in decrypted_connections]


def pp_pass(parsed_data, decrypted_connections):
    for c in decrypted_connections:
        try:
            sid = c['parameters']['sid']
        except:
            sid = '**{}**'.format(c['parameters']['customUrl'])
        print('pass insert company/{}/{}/{}/{}\t#\t{}'.format(
            c['parameters']['RaptorConnectionType'],
            c['parameters']['hostname'],
            sid,
            c['parameters']['user'],
            c['parameters']['.password'],
        ))


def pp_version3(parsed_data, decrypted_connections):
    # select * from sys.link$ order by host, userid, password, owner#
    # decrypt = getattr(__import__('decryptors.decryptor_3', fromlist=['']), 'decrypt')
    # print(decrypt('05x', ''))
    pass


def pp_validate_names(parsed_data, decrypted_connections):
    for c in decrypted_connections:
        try:
            name1 = '{name}'.format(name=c['name'])
            name2 = '{hostname}@{sid}@{user}'.format(**c['parameters'])
            if name1.split()[0] != name2:
                print(name1, name2)
                # pp(c)
        except:
            try:
                customUrl = c['parameters']['customUrl']
                customUrl = customUrl.replace('jdbc:oracle:thin:@', '')
                customUrl = customUrl.replace('jdbc:mysql://', '')
                customUrl = customUrl.replace('jdbc:jtds:sqlserver://', '')
                customUrl = customUrl.replace(':1521/', '@')
                customUrl = customUrl.replace(':3306/', '@')
                customUrl = customUrl.replace(':1433/', '@')
                name2 = '{customUrl}@{user}'.format(customUrl=customUrl, user=c['parameters']['user'])
                if name1.split()[0] != name2:
                    print(name1, name2)
                    # pp(c)
            except:
                pp(c)


def main():
    parsed_data = parse_data(parser_name=PARSER_NAME)
    decrypted_connections = decrypt_connections(version=VERSION, parsed_data=parsed_data)
    # pp_header(parsed_data, decrypted_connections)
    pp(decrypted_connections)
    # pp_passwords(parsed_data, decrypted_connections)
    # pp_pass(parsed_data, decrypted_connections)
    # pp_version3(parsed_data, decrypted_connections)
    # pp_validate_names(parsed_data, decrypted_connections)


if __name__ == '__main__':
    main()
