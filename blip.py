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
		pos_hint: {'x':0, 'y':0}
		size_hint: (1, 1)
		allow_stretch: True
<ChatScreen>:
	orientation: "vertical"
	Button:
		text: "Send"
		pos_hint: {'x':0, 'y':.9}
		size_hint: (1, .1)
	TextInput:
		pos_hint: {'x':0, 'y':.8}
		size_hint: (1, .1)
		on_text: add_to_message(args)
""")

#These classes just initialize stuff
class SplashScreen(Screen):
	pass
class ChatScreen(Screen):
	pass


def add_to_message(self, text):
	pass
Window.bind(add_to_message=add_to_message)

sm = ScreenManager()
sm.add_widget(SplashScreen(name="spash"))
sm.add_widget(ChatScreen(name="chat"))

class Blip(App, BoxLayout):
	def build(self):
		return sm

#def drop_a_blip(*args):
#	sm.current="second"
	
mApp = Blip()
mApp.run() 
