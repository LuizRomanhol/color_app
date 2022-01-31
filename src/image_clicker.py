from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
import cv2

def in_between(floor,roof,n):
	if n > roof:
		n = roof-1
	if n < floor:
		n = floor+1
	return n
	
def draw_circle(file_path,touch):
	print(file_path)
	img = cv2.imread(file_path)
		
	x = int(in_between(0,img.shape[0],touch.x))
	y = int(in_between(0,img.shape[1],touch.y))
	
	mean_shape = img.shape[0] + img.shape[1]
	thickness = int(mean_shape/320)
	radius = int(mean_shape/320)
	img = cv2.circle(img, (y,x), radius, (255,0,0), thickness)
	
 			
	img_dir = 'tmp/img'+str(x)+'e'+str(y)+'.jpeg'
	cv2.imwrite(img_dir, img)
	print("VALORES X E Y:",x,y)
	return img_dir
	
