from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex


class CalculatorApp(App):
    def build(self):
        self.title = "Kalkulyator"

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.display = Label(
            text="0",
            font_size='48sp',
            halign='right',
            valign='middle',
            size_hint=(1, 0.25),
            color=get_color_from_hex('#FFFFFF')
        )
        self.display.bind(size=self.display.setter('text_size'))
        main_layout.add_widget(self.display)

        buttons_layout = GridLayout(cols=4, spacing=8, size_hint=(1, 0.75))

        buttons = [
            ['C', '⌫', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-', '0', '.', '=']
        ]

        for row in buttons:
            for symbol in row:
                btn = Button(
                    text=symbol,
                    font_size='28sp',
                    background_normal='',
                    background_color=self.get_button_color(symbol)
                )
                btn.bind(on_press=self.on_button_click)
                buttons_layout.add_widget(btn)

        main_layout.add_widget(buttons_layout)
        return main_layout

    def get_button_color(self, symbol):
        if symbol in ['÷', '×', '-', '+', '=']:
            return get_color_from_hex('#FF9500')
        elif symbol in ['C', '⌫', '%', '+/-']:
            return get_color_from_hex('#A5A5A5')
        else:
            return get_color_from_hex('#333333')

    def on_button_click(self, instance):
        text = instance.text
        current = self.display.text

        if text == 'C':
            self.display.text = '0'
        elif text == '⌫':
            if len(current) > 1 and current != 'Xatolik':
                self.display.text = current[:-1]
            else:
                self.display.text = '0'
        elif text == '=':
            try:
                expr = current.replace('÷', '/').replace('×', '*').replace('%', '/100')
                result = str(eval(expr))
                if result.endswith('.0'):
                    result = result[:-2]
                self.display.text = result
            except Exception:
                self.display.text = 'Xatolik'
        elif text == '+/-':
            if current != '0' and current != 'Xatolik':
                if current.startswith('-'):
                    self.display.text = current[1:]
                else:
                    self.display.text = '-' + current
        else:
            if current == '0' or current == 'Xatolik':
                if text in ['÷', '×', '-', '+', '%']:
                    self.display.text = '0' + text
                else:
                    self.display.text = text
            else:
                self.display.text += text


if __name__ == '__main__':
    CalculatorApp().run()