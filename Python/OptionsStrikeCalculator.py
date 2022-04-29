import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

import CondorCalc

class MyGrid(Widget):
    strikearray = []
    atmstraddle = ObjectProperty(None)
    currentprice = ObjectProperty(None)
    longcall = ObjectProperty(None)

    def btn(self):
        try:
            strikearray = CondorCalc.shortCondorCalc(float(self.atmstraddle.text), float(self.currentprice.text))

            self.longput.text = strikearray[1]
            self.shortput.text = strikearray[2]
            self.shortcall.text = strikearray[3]
            self.longcall.text = strikearray[4]
        except ValueError:
            print("You must provide the straddle price and equity price")





class StrikeCalculator(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    StrikeCalculator().run()
