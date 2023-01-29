from kivymd.app import MDApp
from kivymd.app import Builder
from kivymd.app import FpsMonitoring
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDIcon


class Login(MDApp):
    def build(self):
        FpsMonitoring().fps_monitor_start()
        return Builder.load_file('properties.kv')


if __name__ == '__main__':
    Login().run()
