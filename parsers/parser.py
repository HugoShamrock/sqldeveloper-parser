#!/usr/bin/env python3


class parser():

    def __init__(self, filename_connections, filename_preferences):
        self.filename_connections = filename_connections
        self.filename_preferences = filename_preferences
        self.db_system_id = self.get_db_system_id()
        self.connections = self.get_connections()

    def get_db_system_id(self):
        return ''

    def get_connections(self):
        return []
