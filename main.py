from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class CalculatorApp(App):
    def build(self):
        self.icon = ''
        self.title = 'Kalkulyator'
        
        # Asosiy konteyner
        root = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Displey
        self.display = Label(
            text='0',
            font_size='50sp',
            halign='right',
            valign='center',
            size_hint_y=0.25,
            color=(1, 1, 1, 1)
        )
        self.display.bind(size=self.display.setter('text_size'))
        root.add_widget(self.display)
        
        # Tugmalar katakchasi
        grid = GridLayout(cols=4, spacing=10, size_hint_y=0.75)
        
        buttons = [
            'C', '+/-', '%', '÷',
            '7', '8', '9', '×',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '⌫', '='
        ]
        
        for btn_text in buttons:
            button = Button(
                text=btn_text,
                font_size='28sp',
                background_normal='',
                bold=True
            )
            
            # Tugmalar rangini sozlash
            if btn_text in ['÷', '×', '-', '+', '=']:
                button.background_color = (0.95, 0.55, 0.08, 1) # Zargaldoq
                button.color = (1, 1, 1, 1)
            elif btn_text in ['C', '+/-', '%', '⌫']:
                button.background_color = (0.6, 0.6, 0.6, 1) # Kulrang
                button.color = (0, 0, 0, 1)
            else:
                button.background_color = (0.2, 0.2, 0.2, 1) # To'q kulrang
                button.color = (1, 1, 1, 1)
                
            button.bind(on_press=self.on_button_press)
            grid.add_widget(button)
            
        root.add_widget(grid)
        return root

    def on_button_press(self, instance):
        text = instance.text
        current = self.display.text
        
        if current == 'Xato':
            current = '0'

        if text == 'C':
            self.display.text = '0'
            
        elif text == '⌫':
            if len(current) > 1:
                self.display.text = current[:-1]
            else:
                self.display.text = '0'
                
        elif text == '=':
            try:
                expr = current.replace('÷', '/').replace('×', '*')
                result = str(eval(expr))
                # Butun son bo'lsa .0 ni olib tashlash
                if result.endswith('.0'):
                    result = result[:-2]
                self.display.text = result
            except Exception:
                self.display.text = 'Xato'
                
        elif text == '+/-':
            if current != '0':
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
            if current == '0' and text not in ['.', '÷', '×', '-', '+']:
                self.display.text = text
            else:
                self.display.text = current + text

if __name__ == '__main__':
    CalculatorApp().run()