from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
import pandas as pd
data = pd.read_csv("Fixed_MasksWithFeatures_5_8_2021.csv")
data = data.assign(score = 0)

answerList = ['', '', '', '', '', '', '']
count = 0
topStr = ''

class StartMenu(Screen):
    pass


class MainWindow(Screen):
    def clk(self, button):
        answerList[0] = button.text
        if button.text == 'Disposable':
            answerList[1] = 'none'
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
    def clk(self, button):
        global topStr
        for item in answerList:
            item = item.lower()
        for i, row in data.iterrows():
            if row[13] == answerList[0]:  # disposability
                data.at[i, 'score'] += 4
            if answerList[0] == 'reusable':  # pass if disposable
                if answerList[1] in str(row[10]):  # material
                    data.at[i, 'score'] += 1
            if answerList[2] in str(row[8]):  # size
                data.at[i, 'score'] += 1
            if row[12] == answerList[3]:  # gender
                data.at[i, 'score'] += 1
            if row[9] == answerList[4]:  # color
                data.at[i, 'score'] += 1
            if row[11] == answerList[5]:  # filtertype
                data.at[i, 'score'] += 3
            if row[14] == answerList[6]:  # earloops
                data.at[i, 'score'] += 1
        data.sort_values(by = 'score', ascending=False, inplace=True)




class NinthWindow(Screen):
    label_text = StringProperty()
    global topStr
    label_text = topStr
    def clk(self, button):
        global topStr
        n = 0
        for i, row in data.iterrows():
            topStr += '\nhttps://www.amazon.com' + data.at[i, 'link']
            n += 1
            if n >= 10:
                break
        print(topStr)

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
