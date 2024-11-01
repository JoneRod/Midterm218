import sys
from app.commands import Command
import logging


class SubtractCommand(Command):
    def execute(self, params=None):
        if len(params) == 2:
            a, b = params
            print(f'{a} - {b} = {int(a) - int(b)}')
        print(params)