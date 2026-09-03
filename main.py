from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (0.1, 0.1, 0.1, 1)

class CalculatorApp(App):
    def build(self):
        self.title = "Kalkulyator"
        
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        self.display = Label(
            text="0",
            font_size='48sp',
            halign='right',
            valign='middle',
            size_hint=(1, 0.25),
            color=(1, 1, 1, 1)
        )
        self.display.bind(size=self.display.setter('text_size'))
        main_layout.add_widget(self.display)
        
        grid = GridLayout(cols=4, spacing=10, size_hint=(1, 0.75))
        
        buttons = [
            ['C', 'DEL', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-', '0', '.', '=']
        ]
        
        for row in buttons:
            for text in row:
                btn = Button(
                    text=text,
                    font_size='28sp',
                    background_normal='',
                    background_color=self.get_button_color(text),
                    color=(1, 1, 1, 1)
                )
                btn.bind(on_press=self.on_button_press)
                grid.add_widget(btn)
                
        main_layout.add_widget(grid)
        return main_layout

    def get_button_color(self, text):
        if text in ['÷', '×', '-', '+', '=']:
            return (0.95, 0.5, 0.1, 1)
        elif text in ['C', 'DEL', '%', '+/-']:
            return (0.3, 0.3, 0.3, 1)
        else:
            return (0.2, 0.2, 0.2, 1)

    def on_button_press(self, instance):
        text = instance.text
        current = self.display.text

        if text == 'C':
            self.display.text = "0"
        elif text == 'DEL':
            if current == "Xato" or len(current) == 1:
                self.display.text = "0"
            else:
                self.display.text = current[:-1]
        elif text == '=':
            try:
                expression = current.replace('÷', '/').replace('×', '*').replace('%', '/100')
                result = eval(expression)
                if isinstance(result, float):
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 8)
                self.display.text = str(result)
            except Exception:
                self.display.text = "Xato"
        elif text == '+/-':
            if current != "0" and current != "Xato":
                if current.startswith('-'):
                    self.display.text = current[1:]
                else:
                    self.display.text = '-' + current
        else:
            if current == "0" or current == "Xato":
                if text in ['÷', '×', '+', '%', '.']:
                    if text != '.':
                        self.display.text = "0" + text
                    else:
                        self.display.text = "0."
                else:
                    self.display.text = text
            else:
                last_char = current[-1]
                operators = ['÷', '×', '-', '+', '.']
                if text in operators and last_char in operators:
                    self.display.text = current[:-1] + text
                else:
                    self.display.text += text

if __name__ == '__main__':
    CalculatorApp().run()