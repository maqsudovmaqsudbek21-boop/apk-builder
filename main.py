from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (0.12, 0.12, 0.12, 1)

class CalculatorApp(App):
    def build(self):
        self.title = "Kalkulyator"
        
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        self.solution = TextInput(
            multiline=False, 
            readonly=True, 
            halign='right', 
            font_size=55,
            background_color=(0.18, 0.18, 0.18, 1),
            foreground_color=(1, 1, 1, 1),
            size_hint=(1, 0.25),
            padding=[10, 20, 10, 10]
        )
        main_layout.add_widget(self.solution)
        
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
                    bg_color = (1, 0.56, 0, 1)
                elif label in ['C', 'DEL', '%']:
                    bg_color = (0.4, 0.4, 0.4, 1)
                else:
                    bg_color = (0.25, 0.25, 0.25, 1)
                
                button = Button(
                    text=label,
                    font_size=32,
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

        if button_text == 'C':
            self.solution.text = ''
        elif button_text == 'DEL':
            self.solution.text = current[:-1]
        elif button_text == '=':
            if current:
                try:
                    expression = current.replace('%', '/100')
                    result = str(eval(expression))
                    if result.endswith('.0'):
                        result = result[:-2]
                    self.solution.text = result
                except Exception:
                    self.solution.text = 'Xato'
        else:
            if current == 'Xato':
                current = ''
            
            operators = ['/', '*', '-', '+']
            if current and (current[-1] in operators) and (button_text in operators):
                self.solution.text = current[:-1] + button_text
            else:
                self.solution.text = current + button_text

if __name__ == '__main__':
    CalculatorApp().run()