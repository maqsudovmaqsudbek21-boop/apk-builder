from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class CalculatorApp(App):
    def build(self):
        self.title = 'Kalkulyator'
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.display = Label(
            text='0',
            font_size='48sp',
            halign='right',
            valign='middle',
            size_hint=(1, 0.25),
            color=(1, 1, 1, 1)
        )
        self.display.bind(size=self.display.setter('text_size'))
        main_layout.add_widget(self.display)
        
        grid = GridLayout(cols=4, spacing=8, size_hint=(1, 0.75))
        
        buttons = [
            'C', 'DEL', '%', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '+/-', '0', '.', '='
        ]
        
        for btn_text in buttons:
            btn = Button(
                text=btn_text,
                font_size='24sp',
                background_normal='',
                background_color=self.get_btn_color(btn_text)
            )
            btn.bind(on_press=self.on_button_press)
            grid.add_widget(btn)
            
        main_layout.add_widget(grid)
        return main_layout

    def get_btn_color(self, text):
        if text in ['/', '*', '-', '+', '=']:
            return (0.9, 0.5, 0.1, 1)
        elif text in ['C', 'DEL', '%', '+/-']:
            return (0.5, 0.5, 0.5, 1)
        else:
            return (0.2, 0.2, 0.2, 1)

    def on_button_press(self, instance):
        text = instance.text
        current = self.display.text

        if text == 'C':
            self.display.text = '0'
        elif text == 'DEL':
            if len(current) > 1 and current != 'Xato':
                self.display.text = current[:-1]
            else:
                self.display.text = '0'
        elif text == '=':
            try:
                result = str(eval(current))
                if result.endswith('.0'):
                    result = result[:-2]
                self.display.text = result
            except Exception:
                self.display.text = 'Xato'
        elif text == '+/-':
            if current != '0' and current != 'Xato':
                if current.startswith('-'):
                    self.display.text = current[1:]
                else:
                    self.display.text = '-' + current
        elif text == '%':
            try:
                val = float(current) / 100
                self.display.text = str(val)
            except Exception:
                self.display.text = 'Xato'
        else:
            if current == '0' or current == 'Xato':
                if text in ['/', '*', '+']:
                    self.display.text = '0' + text
                elif text == '.':
                    self.display.text = '0.'
                else:
                    self.display.text = text
            else:
                if text in ['/', '*', '-', '+'] and current[-1] in ['/', '*', '-', '+']:
                    self.display.text = current[:-1] + text
                else:
                    self.display.text += text

if __name__ == '__main__':
    CalculatorApp().run()