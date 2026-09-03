from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.title = "Kalkulyator"
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.display = TextInput(
            multiline=False,
            readonly=True,
            halign='right',
            font_size='48sp',
            background_color=(0.12, 0.12, 0.12, 1),
            foreground_color=(1, 1, 1, 1),
            size_hint=(1, 0.25)
        )
        main_layout.add_widget(self.display)
        
        buttons_layout = GridLayout(cols=4, spacing=8, size_hint=(1, 0.75))
        
        buttons = [
            'C', 'DEL', '%', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '+/-', '0', '.', '='
        ]
        
        for button_text in buttons:
            if button_text in ['/', '*', '-', '+', '=']:
                bg_color = (0.95, 0.55, 0.08, 1)
            elif button_text in ['C', 'DEL', '%', '+/-']:
                bg_color = (0.4, 0.4, 0.4, 1)
            else:
                bg_color = (0.2, 0.2, 0.2, 1)
                
            btn = Button(
                text=button_text,
                font_size='28sp',
                background_normal='',
                background_color=bg_color,
                color=(1, 1, 1, 1)
            )
            btn.bind(on_press=self.on_button_press)
            buttons_layout.add_widget(btn)
            
        main_layout.add_widget(buttons_layout)
        return main_layout

    def on_button_press(self, instance):
        text = instance.text
        current = self.display.text
        
        if current == 'Xato':
            current = ''
            self.display.text = ''

        if text == 'C':
            self.display.text = ''
        elif text == 'DEL':
            self.display.text = current[:-1]
        elif text == '=':
            if current:
                try:
                    result = str(eval(current))
                    if result.endswith('.0'):
                        result = result[:-2]
                    self.display.text = result
                except Exception:
                    self.display.text = 'Xato'
        elif text == '+/-':
            if current:
                if current.startswith('-'):
                    self.display.text = current[1:]
                else:
                    self.display.text = '-' + current
        elif text == '%':
            if current:
                try:
                    val = float(current) / 100
                    res = str(val)
                    if res.endswith('.0'):
                        res = res[:-2]
                    self.display.text = res
                except Exception:
                    self.display.text = 'Xato'
        else:
            self.display.text += text

if __name__ == '__main__':
    CalculatorApp().run()