import os
import sys
import traceback

# from kivy.config import ConfigParser
# from kivy.utils import get_color_from_hex
#
# prog_path = os.path.split(os.path.abspath(sys.argv[0]))[0]
#
# # Если файл настроек отсутствует.
# if not os.path.exists('{}/program.ini'.format(prog_path)):
#     theme = 'default'
# else:
#     config = ConfigParser()
#     config.read('{}/program.ini'.format(prog_path))
#     theme = config.get('General', 'theme')
#
# # -----------------------УСТАНОВКА ЦВЕТОВОЙ ТЕМЫ---------------------------
# config_theme = ConfigParser()
# config_theme.read('{}/Data/themes/{theme}/{theme}.ini'.format(
#     prog_path, theme=theme))
#
# alpha = \
#     get_color_from_hex(config_theme.get('color', 'alpha'))
# title_program_color = \
#     get_color_from_hex(config_theme.get('color', 'title_program_color'))
# list_color = \
#     get_color_from_hex(config_theme.get('color', 'list_color'))
# tab_text_color = \
#     get_color_from_hex(config_theme.get('color', 'tab_text_color'))
# text_color = \
#     get_color_from_hex(config_theme.get('color', 'text_color'))
# tab_indicator_color = \
#     get_color_from_hex(config_theme.get('color', 'tab_indicator_color'))
# floating_button_color = \
#     get_color_from_hex(config_theme.get('color', 'floating_button_color'))
# floating_button_down_color = \
#     get_color_from_hex(config_theme.get('color', 'floating_button_down_color'))
# floating_button_color_end_call = \
#     get_color_from_hex(config_theme.get('color', 'floating_button_color_end_call'))
# floating_button_down_color_end_call = \
#     get_color_from_hex(config_theme.get('color', 'floating_button_down_color_end_call'))
#
# text_color = config_theme.get('color', 'text_color')
# underline_rst_color = config_theme.get('color', 'underline_rst_color')
# text_key_color = config_theme.get('color', 'text_key_color')
# text_link_color = config_theme.get('color', 'text_link_color')
#
#
