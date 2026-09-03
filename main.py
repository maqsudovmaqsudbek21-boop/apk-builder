from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        self.title = "Kalkulyator"
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Displey ekrani
        self.display = TextInput(
            multiline=False,
            readonly=True,
            halign='right',
            font_size=45,
            background_color=(0.15, 0.15, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            size_hint=(1, 0.25)
        )
        main_layout.add_widget(self.display)
        
        # Tugmalar joylashuvi
        buttons = [
            ['C', 'DEL', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-', '0', '.', '=']
        ]
        
        grid_layout = GridLayout(cols=4, spacing=8, size_hint=(1, 0.75))
        
        for row in buttons:
            for label in row:
                button = Button(
                    text=label,
                    font_size=28,
                    background_normal='',
                    background_color=self.get_button_color(label)
                )
                button.bind(on_press=self.on_button_press)
                grid_layout.add_widget(button)
                
        main_layout.add_widget(grid_layout)
        return main_layout

    def get_button_color(self, label):
        if label in ['/', '*', '-', '+', '=']:
            return (0.95, 0.55, 0.0, 1)  # To'q sariq (operatsiyalar)
        elif label in ['C', 'DEL', '%', '+/-']:
            return (0.5, 0.5, 0.5, 1)   # Kulrang (maxsus tugmalar)
        else:
            return (0.25, 0.25, 0.25, 1) # To'q kulrang (raqamlar)

    def on_button_press(self, instance):
        text = instance.text
        current = self.display.text

        if current == "Xato":
            current = ""

        if text == 'C':
            self.display.text = ""
        elif text == 'DEL':
            self.display.text = current[:-1]
        elif text == '=':
            if current:
                try:
                    # Amallarni hisoblash
                    result = str(eval(current))
                    if result.endswith('.0'):
                        result = result[:-2]
                    self.display.text = result
                except Exception:
                    self.display.text = "Xato"
        elif text == '+/-':
            if current:
                if current.startswith('-'):
                    self.display.text = current[1:]
                else:
                    self.display.text = '-' + current
        else:
            # Ketma-ket operatorlar kiritilishini oldini olish
            operators = ['/', '*', '-', '+', '%']
            if current and current[-1] in operators and text in operators:
                self.display.text = current[:-1] + text
            else:
                self.display.text = current + text


if __name__ == '__main__':
    CalculatorApp().run()