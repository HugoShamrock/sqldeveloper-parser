#!/usr/bin/env python3

try:
    from parsers.parser import parser as parent_parser
except:
    from parser import parser as parent_parser

from lxml import etree


class parser(parent_parser):

    def get_db_system_id(self):
        preferences = etree.parse(self.fn_preferences)
        return preferences.xpath('//value[@n="db.system.id"]')[0].attrib['v']

    def get_connections(self):
        connections = etree.parse(self.fn_connections)
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

    def prt_connections(self):  # obsolete
        connections = etree.parse(self.fn_connections)
        for reference in connections.xpath('//Reference'):
            print(reference.attrib['name'])
            for parameter in reference.xpath('./RefAddresses/StringRefAddr'):
                print('\t', parameter.attrib['addrType'], '=', parameter.xpath('./Contents')[0].text)
