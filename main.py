from kivymd.app import MDApp
from kivymd.app import FpsMonitoring


class Login(MDApp):
    FpsMonitoring().fps_monitor_start()
    


if __name__ == '__main__':
    app = Login()
    app.run()
