from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class CyberDemo(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        title = Label(
            text="CYBER DEMO",
            font_size=30
        )

        welcome = Label(
            text="Welcome to Cyber Security Demo",
            font_size=18
        )

        button = Button(
            text="TEST PAYLOAD",
            font_size=20,
            size_hint=(1, 0.3)
        )

        button.bind(on_press=self.test_payload)

        layout.add_widget(title)
        layout.add_widget(welcome)
        layout.add_widget(button)

        return layout

    def test_payload(self, instance):
        popup = Popup(
            title="Test Successful",
            content=Label(
                text="Safe Demo Payload Working!"
            ),
            size_hint=(0.8, 0.4)
        )
        popup.open()

CyberDemo().run()
