import kivy
from kivy.app import App
from kivy.uix.widget import Widget





class MyLayout(Widget):
    def spinner_clicked(self, value):
            self.ids.spinner_id.text = f"{value}"




class Fitlog(App):
    def build(self):
        return MyLayout() 
    
Fitlog = Fitlog()
Fitlog.run()