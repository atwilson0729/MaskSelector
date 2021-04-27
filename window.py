from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class ThirdWindow(Screen):
    pass


class FourthWindow(Screen):
    pass


class FifthWindow(Screen):
    pass


class SixthWindow(Screen):
    pass


class SeventhWindow(Screen):
    pass


class EighthWindow(Screen):
    pass


class NinthWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MaskSelectorApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MaskSelectorApp().run()
