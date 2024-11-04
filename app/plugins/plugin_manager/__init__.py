import sys
import logging
from app.commands import Command

class PluginManager(Command):
    def __init__(self):
        self.history_plugin = None

    def register_history_plugin(self, plugin):
        self.history_plugin = plugin

    def record_calculation(self, calculation, result):
        if self.history_plugin:
            self.history_plugin.add_to_history(calculation, result)
        else:
            print("History plugin not registered.")