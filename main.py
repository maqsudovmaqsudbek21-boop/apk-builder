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
            size_hint_y=0.25,
            background_color=(0.95, 0.95, 0.95, 1),
            foreground_color=(0, 0, 0, 1)
        )
        main_layout.add_widget(self.display)
        
        buttons = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', 'DEL', '=']
        ]
        
        grid = GridLayout(cols=4, spacing=8)
        
        for row in buttons:
            for label in row:
                if label in ['/', '*', '-', '+', '=']:
                    bg_color = (0.2, 0.6, 0.9, 1)
                elif label in ['C', 'DEL']:
                    bg_color = (0.9, 0.3, 0.3, 1)
                else:
                    bg_color = (0.25, 0.25, 0.25, 1)
                    
                button = Button(
                    text=label,
                    font_size=30,
                    background_normal='',
                    background_color=bg_color,
                    color=(1, 1, 1, 1)
                )
                button.bind(on_press=self.on_button_press)
                grid.add_widget(button)
                
        main_layout.add_widget(grid)
        return main_layout

    def on_button_press(self, instance):
        text = instance.text
        
        if text == 'C':
            self.display.text = ''
        elif text == 'DEL':
            self.display.text = self.display.text[:-1]
        elif text == '=':
            try:
                expression = self.display.text
                result = str(eval(expression))
                self.display.text = result
            except Exception:
                self.display.text = 'Xato'
        else:
            if self.display.text == 'Xato':
                self.display.text = ''
            self.display.text += text


if __name__ == '__main__':
    CalculatorApp().run()