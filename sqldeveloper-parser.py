#!/usr/bin/env python3

# http://stackoverflow.com/questions/1032721/does-anybody-know-what-encrypting-technique-is-jdeveloper-sql-developer-using-to
# http://blog.pythonaro.com/2012/08/encrypting-and-decrypting-sqldeveloper.html
# https://github.com/maaaaz/sqldeveloperpassworddecryptor
# http://stackoverflow.com/questions/5093002/finding-elements-by-attribute-with-lxml
# http://stackoverflow.com/questions/6677424/how-do-i-import-variable-packages-in-python-like-using-variable-variables-i


CONFIG_PATH = '/home/pm/.sqldeveloper/system4.1.2.20.64/'
FN_CONNECTIONS = '{CP}o.jdeveloper.db.connection.12.2.1.0.42.151001.541/connections.xml'.format(CP=CONFIG_PATH)
FN_PREFERENCES = '{CP}o.sqldeveloper.12.2.0.20.64/product-preferences.xml'.format(CP=CONFIG_PATH)

PARSERS = ('parser', 'parser_by_lxml', 'parser_by_xmltodict')

[print(i) for i in (FN_CONNECTIONS, FN_PREFERENCES)]

if __name__ == '__main__':

    for module in PARSERS:
        parser = getattr(__import__('parsers.{}'.format(module), fromlist=['parser']), 'parser')
        print(parser)
        p = parser(fn_connections=FN_CONNECTIONS, fn_preferences=FN_PREFERENCES)
        print(p.db_system_id)
        if p.connections:
            print(len(p.connections))
            for connection in p.connections[:5]:
                print(connection['name'], '\t', connection['parameters']['password'])
            print('...')
