# """
# loadplugin.py
# +++++++++++++++++++++++++++++++++++
# Загружает плагины программы из папки plugins корневой директории программы.

import os
import sys
import traceback

from main import __version__
from . manifest import Manifest


def load_plugin(app):
    #"""Загружает, верифицирует и запускает плагины."""

    plugins_path = \
        '{}/Libs/plugins'.format(os.path.split(os.path.abspath(sys.argv[0]))[0])
    app.started_plugins = {}

    if not os.path.exists(plugins_path):
        os.mkdir(plugins_path)
        open('{}/__init__.py'.format(plugins_path), 'w').write('')
        open('{}/README.rst'.format(plugins_path), 'w').write(
            'This directory for plugins of Program\n'
            '--------------------------------------\n')
    if not os.path.exists('{}/plugins_list.list'.format(plugins_path)):
        open('{}/plugins_list.list'.format(plugins_path), 'w').write(
            str(list()))

    plugin_list = \
        eval(open('{}/plugins_list.list'.format(plugins_path)).read())

    for name in os.listdir(plugins_path):
        if name.startswith('__init__.'):
            continue

        path = os.path.join(plugins_path, name)

        if not os.path.isdir(path):
            continue
        try:
            manifest = Manifest(os.path.join(path, 'manifest.txt'))
            application_version = __version__.split()[0]

            app.started_plugins[name] = \
                {
                    'plugin-name': manifest['plugin-name'],
                    'plugin-desc': manifest['plugin-desc'],
                    'plugin-package': manifest['plugin-package'],
                    'plugin-version': manifest['plugin-version'],
                    'plugin-author': manifest['plugin-author'],
                    'plugin-mail': manifest['plugin-mail'],
                    'app-version-min': manifest['app-version-min'],
                    'app-version-max': manifest['app-version-max'],
                    'app-version': application_version
                }

            # Запускаем плагин, если он присутствует в списке активированых.
            if name in plugin_list:
                exec(open(os.path.join(path, '__init__.py')).read(),
                     {'app': app, 'path': path})
        except Exception:
            raise Exception(traceback.format_exc())