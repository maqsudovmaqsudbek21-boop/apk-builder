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
            font_size=45,
            size_hint=(1, 0.25),
            background_normal='',
            background_color=(0.15, 0.15, 0.15, 1),
            foreground_color=(1, 1, 1, 1)
        )
        main_layout.add_widget(self.display)
        
        buttons = [
            ['C', 'DEL', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['00', '0', '.', '=']
        ]
        
        grid_layout = GridLayout(cols=4, spacing=8, size_hint=(1, 0.75))
        
        for row in buttons:
            for label in row:
                if label in ['C', 'DEL']:
                    bg_color = (0.85, 0.25, 0.25, 1)
                elif label in ['/', '*', '-', '+', '=']:
                    bg_color = (0.2, 0.6, 0.9, 1)
                elif label == '%':
                    bg_color = (0.4, 0.4, 0.4, 1)
                else:
                    bg_color = (0.25, 0.25, 0.25, 1)
                
                btn = Button(
                    text=label,
                    font_size=28,
                    bold=True,
                    background_normal='',
                    background_color=bg_color,
                    color=(1, 1, 1, 1)
                )
                btn.bind(on_press=self.on_button_press)
                grid_layout.add_widget(btn)
                
        main_layout.add_widget(grid_layout)
        return main_layout

    def on_button_press(self, instance):
        text = instance.text
        current = self.display.text
        
        if current == "Xato":
            current = ""
            
        if text == 'C':
            self.display.text = ''
        elif text == 'DEL':
            self.display.text = current[:-1]
        elif text == '=':
            if not current:
                return
            try:
                expression = current.replace('%', '/100')
                result = eval(expression)
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                self.display.text = str(result)
            except Exception:
                self.display.text = 'Xato'
        else:
            operators = ['/', '*', '-', '+', '.']
            if text in operators and current and current[-1] in operators:
                self.display.text = current[:-1] + text
            else:
                self.display.text = current + text


if __name__ == '__main__':
    CalculatorApp().run()