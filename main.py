from time import sleep
from kivymd.app import MDApp
from kivymd.app import Builder
from kivymd.app import FpsMonitoring
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from jsonmanager import JsonManager


class Cadastro(MDApp):
    def build(self):
        # FpsMonitoring().fps_monitor_start()
        self.theme_cls.theme_style = 'Dark'
        Window.minimum_height = 600
        Window.minimum_width = 500
        self.__file_builder = Builder.load_file('properties_login.kv')
        return self.__file_builder

    def on_start(self):
        self.theme_cls.theme_style = 'Dark'

    def change_theme(self):
        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'
            self.__file_builder.ids.fg_pass.color = '#2096f2'
            self.__file_builder.ids.not_acess.color = (1, 0, 0, 1)
        else:
            self.theme_cls.theme_style = 'Light'
            Window.clearcolor = (234,234,234,1)
            self.__file_builder.ids.fg_pass.color = '#2096f2'
            self.__file_builder.ids.not_acess.color = (1, 0, 0, 1)

    def acess(self):
        self.__file_js: dict = JsonManager().load_file()
        if self.__file_js['user'] == self.__file_builder.ids.user.text \
           and self.__file_js['email'] == self.__file_builder.ids.gmail.text \
           and self.__file_js['pass'] == self.__file_builder.ids.pw.text:
            self.__file_builder.ids.not_acess.text = ''
            print('Acesso permitido!')
        else:
            self.__file_builder.ids.not_acess.text = 'invalid information'


if __name__ == '__main__':
    Cadastro().run()
