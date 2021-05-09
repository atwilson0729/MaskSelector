from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.core.window import Window
import pandas as pd

data = pd.read_csv("Fixed_MasksWithFeatures_5_8_2021.csv")
data = data.assign(score=0)
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

answerList = ['', '', '', '', '', '', '']
weightingList = [1, 1, 1, 1, 1, 1, 1]
count = 0
topStr = ''
darkMode = [True, False]
Window.clearcolor = (.2, .2, .2, .2)


Builder.load_string('''
<SelectableLabel>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size
<RV>:
    viewclass: 'SelectableLabel'
    SelectableRecycleBoxLayout:
        padding: "15dp", "360dp", "15dp", "15dp"
        default_size: 60, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        spacing: dp(12)
        multiselect: True
        touch_multiselect: True
''')


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(df[['link', 'rating']].head(20))}]


class TestApp(App):
    def build(self):
        return RV()


class StartMenu(Screen):

    def theme(self, button):
        if darkMode[0]:
            darkMode[0] = False
            Window.clearcolor = (.9, .9, .9, 1)

        elif not darkMode[0]:
            darkMode[0] = True
            Window.clearcolor = (.2, .2, .2, .2)


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


class SeventhWindowDisposability(Screen):
    def clk(self, button):
        disposability = int(button.text)
        weightingList[0] = disposability


class SeventhWindowMaterial(Screen):
    def clk(self, button):
        material = int(button.text)
        weightingList[1] = material


class SeventhWindowSize(Screen):
    def clk(self, button):
        size = int(button.text)
        weightingList[2] = size


class SeventhWindowGender(Screen):
    def clk(self, button):
        gender = int(button.text)
        weightingList[3] = gender


class SeventhWindowColor(Screen):
    def clk(self, button):
        color = int(button.text)
        weightingList[4] = color


class SeventhWindowFilterType(Screen):
    def clk(self, button):
        filterType = int(button.text)
        weightingList[5] = filterType


class SeventhWindowEarLoops(Screen):
    def clk(self, button):
        loops = int(button.text)
        weightingList[6] = loops


class EighthWindow(Screen):
    def clk(self, button):
        global topStr
        for item in answerList:
            item = item.lower()
        for i, row in data.iterrows():
            if row[13] == answerList[0]:  # disposability
                data.at[i, 'score'] += weightingList[0]
            if answerList[0] == 'reusable':  # pass if disposable
                if answerList[1] in str(row[10]):  # material
                    data.at[i, 'score'] += weightingList[1]
            if answerList[2] in str(row[8]):  # size
                data.at[i, 'score'] += weightingList[2]
            if row[12] == answerList[3]:  # gender
                data.at[i, 'score'] += weightingList[3]
            if row[9] == answerList[4]:  # color
                data.at[i, 'score'] += weightingList[4]
            if row[11] == answerList[5]:  # filtertype
                data.at[i, 'score'] += weightingList[5]
            if row[14] == answerList[6]:  # earloops
                data.at[i, 'score'] += weightingList[6]
        data.sort_values(by='score', ascending=False, inplace=True)


# fixedData = list(data)
df = pd.DataFrame(data)


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
        print('Please give us your feedback at jcampb32@uncc.edu, above are the links for the masks')

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
    TestApp().run()
