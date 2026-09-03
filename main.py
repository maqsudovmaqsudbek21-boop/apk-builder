from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        self.title = 'Kalkulyator'
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.solution = TextInput(
            multiline=False,
            readonly=True,
            halign='right',
            font_size=45,
            size_hint=(1, 0.25),
            background_color=(0.12, 0.12, 0.12, 1),
            foreground_color=(1, 1, 1, 1)
        )
        main_layout.add_widget(self.solution)
        
        buttons = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-', '0', '.', '=']
        ]
        
        grid_layout = GridLayout(cols=4, spacing=8, size_hint=(1, 0.75))
        
        for row in buttons:
            for label in row:
                if label in ['/', '*', '-', '+', '=']:
                    bg_color = (0.95, 0.5, 0.08, 1)
                elif label in ['C', '⌫', '%', '+/-']:
                    bg_color = (0.5, 0.5, 0.5, 1)
                else:
                    bg_color = (0.25, 0.25, 0.25, 1)
                    
                button = Button(
                    text=label,
                    font_size=28,
                    background_normal='',
                    background_color=bg_color,
                    color=(1, 1, 1, 1)
                )
                button.bind(on_press=self.on_button_press)
                grid_layout.add_widget(button)
                
        main_layout.add_widget(grid_layout)
        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if current == 'Xato':
            current = ''

        if button_text == 'C':
            self.solution.text = ''
        elif button_text == '⌫':
            self.solution.text = current[:-1]
        elif button_text == '=':
            if current:
                try:
                    res = str(eval(current))
                    if res.endswith('.0'):
                        res = res[:-2]
                    self.solution.text = res
                except Exception:
                    self.solution.text = 'Xato'
        elif button_text == '+/-':
            if current:
                if current.startswith('-'):
                    self.solution.text = current[1:]
                else:
                    self.solution.text = '-' + current
        elif button_text == '%':
            if current:
                try:
                    val = float(eval(current)) / 100
                    res = str(val)
                    if res.endswith('.0'):
                        res = res[:-2]
                    self.solution.text = res
                except Exception:
                    self.solution.text = 'Xato'
        else:
            operators = ['/', '*', '-', '+', '.']
            if current and button_text in operators and current[-1] in operators:
                return
            self.solution.text = current + button_text


if __name__ == '__main__':
    CalculatorApp().run()