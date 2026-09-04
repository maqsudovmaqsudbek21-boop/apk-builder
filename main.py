from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (0.1, 0.1, 0.1, 1)

class CalculatorApp(App):
    def build(self):
        self.title = "Kalkulyator"
        
        main_layout = BoxLayout(orientation="vertical", spacing=10, padding=15)
        
        self.display = Label(
            text="0",
            font_size="48sp",
            halign="right",
            valign="center",
            size_hint=(1, 0.25),
            color=(1, 1, 1, 1)
        )
        self.display.bind(size=self.display.setter('text_size'))
        main_layout.add_widget(self.display)
        
        buttons_layout = GridLayout(cols=4, spacing=8, size_hint=(1, 0.75))
        
        buttons = [
            ("C", (0.8, 0.2, 0.2, 1)),
            ("DEL", (0.8, 0.4, 0.1, 1)),
            ("%", (0.3, 0.3, 0.3, 1)),
            ("÷", (0.2, 0.6, 0.9, 1)),
            ("7", (0.2, 0.2, 0.2, 1)),
            ("8", (0.2, 0.2, 0.2, 1)),
            ("9", (0.2, 0.2, 0.2, 1)),
            ("×", (0.2, 0.6, 0.9, 1)),
            ("4", (0.2, 0.2, 0.2, 1)),
            ("5", (0.2, 0.2, 0.2, 1)),
            ("6", (0.2, 0.2, 0.2, 1)),
            ("-", (0.2, 0.6, 0.9, 1)),
            ("1", (0.2, 0.2, 0.2, 1)),
            ("2", (0.2, 0.2, 0.2, 1)),
            ("3", (0.2, 0.2, 0.2, 1)),
            ("+", (0.2, 0.6, 0.9, 1)),
            ("00", (0.2, 0.2, 0.2, 1)),
            ("0", (0.2, 0.2, 0.2, 1)),
            (".", (0.2, 0.2, 0.2, 1)),
            ("=", (0.1, 0.7, 0.3, 1))
        ]
        
        for text, color in buttons:
            btn = Button(
                text=text,
                font_size="28sp",
                background_normal="",
                background_color=color,
                bold=True
            )
            btn.bind(on_press=self.on_button_press)
            buttons_layout.add_widget(btn)
            
        main_layout.add_widget(buttons_layout)
        return main_layout

    def on_button_press(self, instance):
        text = instance.text
        current = self.display.text

        if text == "C":
            self.display.text = "0"
        elif text == "DEL":
            if current in ["Xato", "0"] or len(current) == 1:
                self.display.text = "0"
            else:
                self.display.text = current[:-1]
        elif text == "=":
            try:
                expr = current.replace("×", "*").replace("÷", "/")
                result = str(eval(expr))
                if result.endswith(".0"):
                    result = result[:-2]
                self.display.text = result
            except Exception:
                self.display.text = "Xato"
        else:
            if current in ["0", "Xato"]:
                if text in ["+", "-", "×", "÷", "%"]:
                    self.display.text = "0" + text
                elif text == ".":
                    self.display.text = "0."
                else:
                    self.display.text = text
            else:
                self.display.text += text

if __name__ == "__main__":
    CalculatorApp().run()