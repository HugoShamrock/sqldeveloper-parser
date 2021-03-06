#!/usr/bin/env python3

# http://stackoverflow.com/questions/5093002/finding-elements-by-attribute-with-lxml

try:
    from parsers.parser import parser as parent_parser
except:
    from parser import parser as parent_parser

from lxml import etree


class parser(parent_parser):

    def get_db_system_id(self):
        preferences = etree.parse(self.filename_preferences)
        return preferences.xpath('//value[@n="db.system.id"]')[0].attrib['v']

    def get_connections(self):
        connections = etree.parse(self.filename_connections)
        return [
            {
                'name': reference.attrib['name'],
                'parameters':
                {
                    parameter.attrib['addrType']: parameter.xpath('./Contents')[0].text
                    for parameter in reference.xpath('./RefAddresses/StringRefAddr')
                }
            }
            for reference in connections.xpath('//Reference')
        ]
