import kivy
#kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
#from kivy.core.image import Image as CoreImage
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
Builder.load_string("""
<SplashScreen>:
    orientation: "vertical"
	Button:
		text: "B1"
		on_press: root.manager.current = "chat"
        Image:
            source: 'blip_squid.png'
            y: self.parent.x
            x: self.parent.y
            size: self.parent.height, self.parent.width
            allow_stretch: True
	
<ChatScreen>:
	orientation: "vertical"
	Button:
		text: "Send"
	TextInput:
		height: self.minimum_height
		width: self.height
		
""")

#These classes just initialize stuff
class SplashScreen(Screen):
	pass
class ChatScreen(Screen):
	pass

sm = ScreenManager()
sm.add_widget(SplashScreen(name="spash"))
sm.add_widget(ChatScreen(name="chat"))

class Blip(App, BoxLayout):
	def build(self):
		#sm.current="first_screen"
		#b = BoxLayout()
		#b.add_widget(TextInput())
		#b.add_widget(Button(text="Click me"))
		#b.add_widget(Label(text="Hello"))
		#widg = CustomWidget()
		return sm

#def drop_a_blip(*args):
#	sm.current="second"
	
mApp = Blip()
mApp.run() 
