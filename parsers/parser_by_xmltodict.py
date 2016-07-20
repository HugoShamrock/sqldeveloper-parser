#!/usr/bin/env python3

try:
    from parsers.parser import parser as parent_parser
except:
    from parser import parser as parent_parser

import xmltodict


class parser(parent_parser):

    def get_db_system_id(self):
        preferences = self.open_read_parse(self.fn_preferences)
        return preferences['ide:preferences']['value']['@v']

    def get_connections(self):
        connections = self.open_read_parse(self.fn_connections)
        for reference in connections['References']['Reference']:
            print(reference['@name'])
            for parameter in reference['RefAddresses']['StringRefAddr']:
                print('\t', parameter['@addrType'], '=', parameter['Contents'])

    def open_read_parse(self, filename):
        with open(filename, mode='r', encoding='utf-8') as f:
            return xmltodict.parse(f.read())
