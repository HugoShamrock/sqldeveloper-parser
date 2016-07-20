#!/usr/bin/env python3


class parser():

    def __init__(self, fn_connections, fn_preferences):
        self.fn_connections = fn_connections
        self.fn_preferences = fn_preferences
        self.db_system_id = self.get_db_system_id()
        self.connections = self.get_connections()

    def get_db_system_id(self):
        return

    def get_connections(self):
        return
