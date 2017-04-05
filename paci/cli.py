"""
paci

Usage:
  paci install [--no-config] [--debug] [--no-cleanup] <package>
  paci update [--no-config] <package>
  paci remove 
  paci hello
  paci --help
  paci --version

Options:
  -h, --help                         Show this screen.
  -v, --version                      Show version.
  -n, --no-config                    Omits the config.
  -d, --debug                        Run in debug mode.
  -c, --no-cleanup                   Don't cleanup the mess.

Examples:
  paci hello
  paci install --no-config

Help:
  For help using this tool, please open an issue on the Github repository:
  ~~TODO~~
"""

import better_exceptions

from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entry point."""
    import cli.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(cli.commands, k) and v:
            module = getattr(cli.commands, k)
            cli.commands = getmembers(module, isclass)
            command = [command[1] for command in cli.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
