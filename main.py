from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Mobil ekran ko'rinishi uchun foni to'q rangga o'tkazamiz
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class CalculatorApp(App):
    def build(self):
        self.title = 'Kalkulyator'
        
        # Asosiy konteyner
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Natija va kiritish ekrani
        self.display = TextInput(
            multiline=False,
            readonly=True,
            halign='right',
            font_size=48,
            size_hint=(1, 0.25),
            background_color=(0.18, 0.18, 0.18, 1),
            foreground_color=(1, 1, 1, 1),
            padding=[10, 20, 10, 10]
        )
        main_layout.add_widget(self.display)
        
        # Tugmalar ro'yxati
        buttons = [
            ['C', '()', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['⌫', '0', '.', '=']
        ]
        
        # Tugmalar tori
        grid = GridLayout(cols=4, spacing=10, size_hint=(1, 0.75))
        
        for row in buttons:
            for label in row:
                # Tugmalar rangini ajratish
                if label in ['÷', '×', '-', '+', '=']:
                    bg_color = (0.95, 0.53, 0.08, 1)  # Olovrang (operatsiyalar)
                elif label in ['C', '()', '%', '⌫']:
                    bg_color = (0.3, 0.3, 0.3, 1)     # To'q kulrang (maxsus)
                else:
                    bg_color = (0.2, 0.2, 0.2, 1)     # Raqamlar
                
                btn = Button(
                    text=label,
                    font_size=28,
                    background_normal='',
                    background_color=bg_color,
                    color=(1, 1, 1, 1)
                )
                btn.bind(on_press=self.on_button_click)
                grid.add_widget(btn)
                
        main_layout.add_widget(grid)
        return main_layout

    def on_button_click(self, instance):
        text = instance.text
        current = self.display.text

        if current == 'Xato':
            current = ''

        if text == 'C':
            self.display.text = ''
        elif text == '⌫':
            self.display.text = current[:-1]
        elif text == '=':
            if current:
                try:
                    # Matematik belgilarni Python belgilari bilan almashtirish
                    expr = current.replace('÷', '/').replace('×', '*').replace('%', '/100')
                    result = str(eval(expr))
                    
                    # Natija butun son bo'lsa, nuqta va nolni olib tashlash
                    if result.endswith('.0'):
                        result = result[:-2]
                        
                    self.display.text = result
                except Exception:
                    self.display.text = 'Xato'
        elif text == '()':
            open_count = current.count('(')
            close_count = current.count(')')
            if open_count == close_count or current.endswith(('+', '-', '×', '÷')):
                self.display.text += '('
            else:
                self.display.text += ')'
        else:
            self.display.text += text

if __name__ == '__main__':
    CalculatorApp().run()