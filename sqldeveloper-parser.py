#!/usr/bin/env python3

# http://stackoverflow.com/questions/1032721/does-anybody-know-what-encrypting-technique-is-jdeveloper-sql-developer-using-to
# http://blog.pythonaro.com/2012/08/encrypting-and-decrypting-sqldeveloper.html
# https://github.com/maaaaz/sqldeveloperpassworddecryptor
# http://stackoverflow.com/questions/5093002/finding-elements-by-attribute-with-lxml

CONFIG_PATH = '/home/pm/.sqldeveloper/system4.1.2.20.64/'
FN_CONNECTIONS = '{CP}o.jdeveloper.db.connection.12.2.1.0.42.151001.541/connections.xml'.format(CP=CONFIG_PATH)
FN_PREFERENCES = '{CP}o.sqldeveloper.12.2.0.20.64/product-preferences.xml'.format(CP=CONFIG_PATH)

[print(i) for i in (FN_CONNECTIONS, FN_PREFERENCES)]

if __name__ == '__main__':

    from parsers.parser import parser
    p = parser(fn_connections=FN_CONNECTIONS, fn_preferences=FN_PREFERENCES)
    print(p.db_system_id)

    from parsers.parser_by_lxml import parser
    p = parser(fn_connections=FN_CONNECTIONS, fn_preferences=FN_PREFERENCES)
    print(p.db_system_id)

    from parsers.parser_by_xmltodict import parser
    p = parser(fn_connections=FN_CONNECTIONS, fn_preferences=FN_PREFERENCES)
    print(p.db_system_id)
