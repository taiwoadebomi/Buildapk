from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Manually load the kv file
Builder.load_file("project.kv")

class RegisterLayout(BoxLayout):
    def submit(self):
        name = self.ids.name_input.text
        email = self.ids.email_input.text
        password = self.ids.password_input.text

        print("Name:", name)
        print("Email:", email)
        print("Password:", password)

class MyApp(App):
    def build(self):
        return RegisterLayout()

MyApp().run()
