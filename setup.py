from cx_Freeze import setup, Executable
import os
import sys

__version__ = '1.0.0'

include_files = ['config.ini']
packages = ['os', 'configparser', 'discord', 'asyncio']

setup(
    name = "Kick All Bot",
    description='Kicks all members of the server (except the command sender and the bot)',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'include_msvcr': True,
}},
executables = [Executable('bot.py')]
)
