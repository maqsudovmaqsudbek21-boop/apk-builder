from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

# Orqa fon rangini to'q rangga o'tkazish
Window.clearcolor = get_color_from_hex('#121212')

class CalculatorApp(App):
    def build(self):
        self.title = 'Kalkulyator'
        
        # Asosiy konteyner
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=15)
        
        # Natija ko'rinadigan ekran
        self.solution = Label(
            text="0",
            font_size='48sp',
            halign='right',
            valign='middle',
            size_hint=(1, 0.25),
            color=get_color_from_hex('#FFFFFF')
        )
        self.solution.bind(size=self.solution.setter('text_size'))
        main_layout.add_widget(self.solution)
        
        # Tugmalar ro'yxati va ularning ulushi (weight)
        buttons = [
            [('C', 1), ('+/-', 1), ('%', 1), ('÷', 1)],
            [('7', 1), ('8', 1), ('9', 1), ('×', 1)],
            [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
            [('1', 1), ('2', 1), ('3', 1), ('+', 1)],
            [('0', 2), ('.', 1), ('=', 1)]
        ]
        
        # Tugmalarni hosil qilish
        for row in buttons:
            h_layout = BoxLayout(spacing=10, size_hint=(1, 0.15))
            for label, weight in row:
                btn = Button(
                    text=label,
                    font_size='28sp',
                    size_hint=(weight, 1),
                    background_normal='',
                    background_color=self.get_button_color(label),
                    color=get_color_from_hex('#FFFFFF')
                )
                btn.bind(on_press=self.on_button_press)
                h_layout.add_widget(btn)
            main_layout.add_widget(h_layout)
            
        return main_layout

    def get_button_color(self, label):
        """Tugmalar uchun ranglarni belgilash"""
        if label in ['÷', '×', '-', '+', '=']:
            return get_color_from_hex('#FF9500') # Amallar (sarg'ish-olovrang)
        elif label in ['C', '+/-', '%']:
            return get_color_from_hex('#505050') # Yordamchi tugmalar (kulrang)
        else:
            return get_color_from_hex('#1C1C1E') # Raqamlar (to'q kulrang)

    def on_button_press(self, instance):
        text = instance.text
        current = self.solution.text

        if text == 'C':
            self.solution.text = '0'
        elif text == '=':
            try:
                # Matematik belgilarni Python sintaksisiga o'tkazish
                expression = self.solution.text.replace('×', '*').replace('÷', '/')
                result = str(eval(expression))
                
                # Agar natija .0 bilan tugasa, uni butun songa aylantirish
                if result.endswith('.0'):
                    result = result[:-2]
                self.solution.text = result
            except Exception:
                self.solution.text = 'Xato'
        elif text == '+/-':
            if current != '0' and current != 'Xato':
                if current.startswith('-'):
                    self.solution.text = current[1:]
                else:
                    self.solution.text = '-' + current
        elif text == '%':
            try:
                val = float(current) / 100
                res = str(val)
                if res.endswith('.0'):
                    res = res[:-2]
                self.solution.text = res
            except Exception:
                self.solution.text = 'Xato'
        else:
            if current == '0' or current == 'Xato':
                self.solution.text = text
            else:
                self.solution.text += text

if __name__ == '__main__':
    CalculatorApp().run()