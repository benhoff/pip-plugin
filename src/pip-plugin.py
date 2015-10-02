import re
import sys
import pip
import asyncio

from simpleyapsy import IPlugin


def install(packages):
    loop = asyncio.get_event_loop()
    if not isinstance(packages, list):
        packages = list(packages)
    if hasattr(sys, 'real_prefix'):
        install_packages = [('install', x) for x in packages]
    else:
        install_packages = [('install', '--user', x) for x in packages]

    # TODO: add in error handeling
    loop.run_in_executor(None, pip.main, install_packages)


# TODO: change to Regex Plugin or similar
class PipPlugin(IPlugin):
    def __init__(self):
        super().__init__()
        self.name = 'pip-plugin'
        self.matches = [re.compile('install')]

    def __call__(self, packages):
        if not isinstance(packages, list):
            packages = list(packages)
        errors = []
        install(packages)

        return errors
