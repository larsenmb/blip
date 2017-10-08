import kivy
#kivy.require("1.9.0")
from kivy.properties import ObjectProperty
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
		on_press: root.enterTxt()
	TextInput:
		pos_hint: {'x':0, 'y':.8}
		size_hint: (1, .1)
		on_text: root.printTxt(args)
	Button: 
		pos_hint:{'x':0, 'y':.6}
		size_hint: (1, .15)
		text: root.messages_out
""")
Window.clearcolor = (1, 1, 1, 1)

#These classes just initialize stuff
class SplashScreen(Screen):
	pass
class ChatScreen(Screen):
	messages = []
	user_in = ""
	messages_out = ""
	def printTxt(self, text):
		self.user_in = text
	def enterTxt(self):
		self.messages.append(self.user_in)
		self.messages_out = str(self.messages).split('\',')
		print(self.messages_out)
	pass

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
