import sys
from app.commands import Command
import logging


class MultiplyCommand(Command):
    def __init__(self, plugin_manager=None):
        self.plugin_manager = plugin_manager

    def execute(self, params=None):
        if len(params) == 2:
            a, b = params
            print(f'{a} x {b} = {int(a) * int(b)}')

            if self.plugin_manager:
                self.plugin_manager.record_calculation(f'{a} + {b}', result)
            else:
                logging.warning("PluginManager not found. Calculation not recorded.")

        print(params)