from kivymd.app import MDApp
from kivymd.app import Builder
from kivymd.app import FpsMonitoring
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen


class Cadastro(MDApp, Screen):
    def build(self):
        FpsMonitoring().fps_monitor_start()
        self.theme_cls.theme_style = 'Dark'
        Window.minimum_height = 600
        Window.minimum_width = 500
        self.__FILE = Builder.load_file('properties_login.kv')
        return self.__FILE

    def on_start(self):
        self.theme_cls.theme_style = 'Dark'

    def change_theme(self):
        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'
            self.__FILE.ids.fg_pass.color = '#2096f2'
        else:
            self.theme_cls.theme_style = 'Light'
            Window.clearcolor = (234,234,234,1)
            self.__FILE.ids.fg_pass.color = '#2096f2'


if __name__ == '__main__':
    Cadastro().run()
