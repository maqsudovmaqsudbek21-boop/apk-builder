from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (0.12, 0.12, 0.12, 1)

class CalculatorApp(App):
    def build(self):
        self.title = 'Kalkulyator'
        
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        self.display = TextInput(
            multiline=False,
            readonly=True,
            halign='right',
            font_size=42,
            background_normal='',
            background_color=(0.2, 0.2, 0.2, 1),
            foreground_color=(1, 1, 1, 1),
            size_hint=(1, 0.25),
            padding=[10, 20, 10, 20]
        )
        main_layout.add_widget(self.display)
        
        buttons = [
            ['C', 'DEL', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['00', '0', '.', '=']
        ]
        
        grid_layout = GridLayout(cols=4, spacing=10, size_hint=(1, 0.75))
        
        for row in buttons:
            for label in row:
                if label in ['/', '*', '-', '+', '=']:
                    bg_color = (0.95, 0.55, 0.08, 1)
                elif label in ['C', 'DEL', '%']:
                    bg_color = (0.5, 0.5, 0.5, 1)
                else:
                    bg_color = (0.3, 0.3, 0.3, 1)
                
                btn = Button(
                    text=label,
                    font_size=28,
                    background_normal='',
                    background_color=bg_color,
                    color=(1, 1, 1, 1)
                )
                btn.bind(on_press=self.on_button_press)
                grid_layout.add_widget(btn)
                
        main_layout.add_widget(grid_layout)
        return main_layout

    def on_button_press(self, instance):
        current = self.display.text
        button_text = instance.text

        if current == 'Xato':
            current = ''

        if button_text == 'C':
            self.display.text = ''
        elif button_text == 'DEL':
            self.display.text = current[:-1]
        elif button_text == '=':
            if current:
                try:
                    expression = current.replace('%', '/100')
                    result = str(eval(expression))
                    if result.endswith('.0'):
                        result = result[:-2]
                    self.display.text = result
                except Exception:
                    self.display.text = 'Xato'
        else:
            self.display.text = current + button_text

if __name__ == '__main__':
    CalculatorApp().run()