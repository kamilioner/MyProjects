import kivy
kivy.require("1.9.2")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class CalcGridLayout(GridLayout):

    def calculate(self, calc):
        if calc:
            try:
                self.display.text = str(eval(calc))
            except Exception:
                self.display.text = "Error"

class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()

calcApp = CalculatorApp()
calcApp.run()