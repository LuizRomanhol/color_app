from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
import src.image_clicker as imclicker

class MainWindow(Screen):
	pass

class SecondWindow(Screen):
	pass

class ThirdWindow(Screen):
	def on_touch_down(self, touch):
		if self.img.collide_point(*touch.pos):
			self.manager.image_source  = imclicker.draw_circle(self.manager.image_source,touch)
		
class WindowManager(ScreenManager):
    image_source = StringProperty()
    def selected(self,filename):
        try:    
            self.image_source = filename[0]
        except:
            pass

kv = Builder.load_file("color.kv")


class ColorApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    ColorApp().run()
