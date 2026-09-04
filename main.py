from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        self.title = 'Kalkulyator'
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Natijalar ko'rinadigan ekran
        self.solution = TextInput(
            multiline=False,
            readonly=True,
            halign='right',
            font_size=45,
            size_hint=(1, 0.25),
            background_color=(0.12, 0.12, 0.12, 1),
            foreground_color=(1, 1, 1, 1),
            padding=[10, 20, 10, 20]
        )
        main_layout.add_widget(self.solution)
        
        # Tugmalar ro'yxati
        buttons = [
            ['C', 'DEL', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['00', '0', '.', '=']
        ]
        
        grid_layout = GridLayout(cols=4, spacing=10)
        
        for row in buttons:
            for label in row:
                btn = Button(
                    text=label,
                    font_size=28,
                    background_normal='',
                    background_color=self.get_btn_color(label)
                )
                btn.bind(on_press=self.on_button_press)
                grid_layout.add_widget(btn)
                
        main_layout.add_widget(grid_layout)
        return main_layout

    def get_btn_color(self, label):
        if label in ['/', '*', '-', '+', '=']:
            return (0.9, 0.5, 0.1, 1)  # Operatorlar uchun to'q sariq
        elif label in ['C', 'DEL', '%']:
            return (0.4, 0.4, 0.4, 1)  # Maxsus tugmalar uchun kulrang
        return (0.2, 0.2, 0.2, 1)      # Raqamlar uchun to'q kulrang

    def on_button_press(self, instance):
        text = instance.text
        current = self.solution.text

        if current == 'Xato':
            current = ''

        if text == 'C':
            self.solution.text = ''
        elif text == 'DEL':
            self.solution.text = current[:-1]
        elif text == '=':
            if current:
                try:
                    expr = current.replace('%', '/100')
                    res = eval(expr)
                    if isinstance(res, float) and res.is_integer():
                        res = int(res)
                    self.solution.text = str(res)
                except Exception:
                    self.solution.text = 'Xato'
        else:
            self.solution.text = current + text


if __name__ == '__main__':
    CalculatorApp().run()