from kivymd.app import MDApp
from kivymd.app import Builder
from kivymd.app import FpsMonitoring
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from jsonmanager import JsonManager


class LoginScreen(Screen):...


class SignUpScreen(Screen):...


class Cadastro(MDApp):
    def build(self):
        # FpsMonitoring().fps_monitor_start()
        Window.minimum_height, Window.minimum_width = 600, 500
        self.screen_manager = ScreenManager()
        self.login_screen = LoginScreen(name='login')
        self.signup_screen = SignUpScreen(name='signup')
        self.screen_manager.add_widget(self.login_screen)
        self.screen_manager.add_widget(self.signup_screen)
        self.__FILE = Builder.load_file('properties_login.kv')
        self.__ID = self.__FILE.ids
        return self.__FILE

    def on_start(self):
        self.theme_cls.theme_style = 'Dark'

    # metódo geral
    def change_theme(self):
        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'
            self.__ID.fg_pass.color = '#2096f2'
            self.__ID.not_access.color = (1, 0, 0, 1)
        else:
            self.theme_cls.theme_style = 'Light'
            Window.clearcolor = (234, 234, 234, 1)
            self.__ID.fg_pass.color = '#2096f2'
            self.__ID.not_access.color = (1, 0, 0, 1)

    # Login
    def access(self):
        self.__file_js: dict = JsonManager().load_file()  # sempre manter atualizado
        if self.__file_js['user'] == self.__ID.user.text \
           and self.__file_js['email'] == self.__ID.gmail.text \
           and self.__file_js['pass'] == self.__ID.pw.text:
            self.__ID.not_access.text = ''
            print('Accesso permitido!')
        else:
            self.__ID.not_access.text = 'invalid information'

    def verify_sign(self):
        print(self.__ID.gmail_crt.error)


if __name__ == '__main__':
    Cadastro().run()
