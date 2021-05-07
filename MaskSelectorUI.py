from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import pandas as pd
data = pd.read_csv("MasksWithFeatures_4_20_2021_225.csv")
data = data.assign(score = 0)

answerList = ['', '', '', '', '', '', '']

count = 0

class StartMenu(Screen):
    pass


class MainWindow(Screen):
    def clk(self, button):
        answerList[0] = button.text
        print(answerList)


class SecondWindow(Screen):
    def clk(self, button):
        answerList[1] = button.text
        print(answerList)


class ThirdWindow(Screen):
    def clk(self, button):
        answerList[2] = button.text
        print(answerList)


class FourthWindow(Screen):
    def clk(self, button):
        answerList[3] = button.text
        print(answerList)


class FifthWindow(Screen):
    def clk(self, button):
        answerList[4] = button.text
        print(answerList)


class SixthWindow(Screen):
    def clk(self, button):
        answerList[5] = button.text
        print(answerList)


class SeventhWindow(Screen):
    def clk(self, button):
        answerList[6] = button.text
        print(answerList)


class EighthWindow(Screen):
    pass


class NinthWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
