from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.base import runTouchApp
'''
class Teste(App):
    def build(self):
        return Button (text='Olá Mundo!')
'''
spinner = Spinner(
    text='Home',
    values=('Home','Work','Other','Custom'),
    size_hint=(None, None), size=(200,144),
    pos_hint={'center_x':.5, 'center_y':.5})
def show_select_value(spinner, text):
    print('The spinner', spinner, 'have text', text)
spinner.bind(text=show_select_value)

runTouchApp(spinner)


#Teste().run()