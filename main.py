from kivymd.app import MDApp
from kivymd.app import Builder
from kivymd.app import FpsMonitoring
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from jsonmanager import JsonManager


class LoginScreen(Screen):
    ...


class SignUpScreen(Screen):
    ...


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
        self.__file_js: dict = JsonManager().load_file()  # mantém sempre atualizado
        if self.__file_js['user'] == self.__ID.user.text \
           and self.__file_js['email'] == self.__ID.gmail.text \
           and self.__file_js['pass'] == self.__ID.pw.text:
            self.__ID.not_access.text = ''
            print('Accesso permitido!')
        else:
            self.__ID.not_access.text = 'invalid information'

    # SingUp
    def verify_sign(self):
        self.__DOMAIN: tuple = ('@gmail.com', '@outlook.com')
        
        # Avisos
        if not self.__ID.gmail_crt.error:
            if not any(domain in self.__ID.gmail_crt.text for domain in self.__DOMAIN):
                print(self.__ID.gmail_crt.text)
                self.__ID.gmail_crt.error = True
                self.__ID.gmail_crt.helper_text = 'Incorrect domain'
                self.__ID.gmail_crt.helper_text_mode= 'on_error'
            else:
                self.__ID.gmail_crt.helper_text = ''

        if self.__ID.user_crt.error:
            if len(self.__ID.user_crt.text) <= 31:
                self.__ID.user_crt.helper_text = 'why such a big name?'
                self.__ID.user_crt.helper_text_mode= 'on_error'                
            if len(self.__ID.user_crt.text) == 0:
                self.__ID.user_crt.helper_text = 'type something'
                self.__ID.user_crt.helper_text_mode = 'on_error'

        if not self.__ID.pw_crt.error and self.__ID.pw_crt.text < 8:
            self.__ID.pw_crt.helper_text = 'Your password must be greater than 8'
            self.__ID.pw_crt.helper_text_mode = 'on_error'

        if not self.__ID.pw_crt_vrf.error and self.__ID.pw_crt_vrf.text < 8:
            self.__ID.pw_crt_vrf.helper_text = 'Your password must be greater than 8'
            self.__ID.pw_crt_vrf.helper_text_mode = 'on_error'

        if not self.__ID.pw_crt_vrf.error or not self.__ID.pw_crt.error:
            if not self.__ID.pw_crt_vrf.text == self.__ID.pw_crt.text:
                self.__ID.pw_crt.helper_text = 'Passwords must be the same'
                self.__ID.pw_crt_vrf.helper_text = 'Passwords must be the same'
                self.__ID.pw_crt_vrf.helper_text_mode = 'on_error'
                self.__ID.pw_crt.helper_text_mode = 'on_error'
        
        if not self.__ID.gmail_crt.error and not self.__ID.user_crt.error and\
           not self.__ID.pw_crt.error and not self.__ID.pw_crt_vrf.error:
               print('registrado')


if __name__ == '__main__':
    Cadastro().run()
