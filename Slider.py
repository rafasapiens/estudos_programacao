from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Slide(BoxLayout):
    pass
    
class  Slider (App):
    def build(self):
        return Slide()
    
Slider().run()