from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CalculatorApp(App):
    def build(self):
        self.title = "Kalkulyator"
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.display = TextInput(
            multiline=False,
            readonly=True,
            halign='right',
            font_size='48sp',
            size_hint_y=0.25,
            background_color=(0.12, 0.12, 0.12, 1),
            foreground_color=(1, 1, 1, 1)
        )
        main_layout.add_widget(self.display)
        
        buttons = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '⌫', '=']
        ]
        
        grid = GridLayout(cols=4, spacing=8, size_hint_y=0.75)
        
        for row in buttons:
            for char in row:
                if char in ['/', '*', '-', '+', '=']:
                    bg_color = (0.95, 0.55, 0.08, 1)
                elif char in ['C', '(', ')', '⌫']:
                    bg_color = (0.35, 0.35, 0.35, 1)
                else:
                    bg_color = (0.2, 0.2, 0.2, 1)
                
                btn = Button(
                    text=char,
                    font_size='28sp',
                    background_normal='',
                    background_color=bg_color,
                    color=(1, 1, 1, 1)
                )
                btn.bind(on_press=self.on_button_press)
                grid.add_widget(btn)
                
        main_layout.add_widget(grid)
        return main_layout

    def on_button_press(self, instance):
        text = instance.text
        current = self.display.text
        
        if current == "Xatolik":
            current = ""
            
        if text == 'C':
            self.display.text = ""
        elif text == '⌫':
            self.display.text = current[:-1]
        elif text == '=':
            try:
                if not current:
                    return
                result = str(eval(current))
                if result.endswith('.0'):
                    result = result[:-2]
                self.display.text = result
            except Exception:
                self.display.text = "Xatolik"
        else:
            self.display.text = current + text

if __name__ == '__main__':
    CalculatorApp().run()