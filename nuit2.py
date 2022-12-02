# importing libraries
import os
import cv2
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from flask import Flask, request, jsonify
from flask import send_file

from numpy import asarray, array
# Checking the current directory path
print(os.getcwd())

# Folder which contains all the images
# from which video is to be generated
os.chdir("./vids")
path = r"C:\Users\ASUS\Desktop\py\imgs"



num_of_images = len(os.listdir('.'))
# print(num_of_images)
sections=['\\Condoms/','\\Mst/','\\Couples/','\\Protection/']
section = random.choice(sections)
answer_cap = (section)[1:-1]
name = '\\mst'+str(random.randint(1, 6))
pathh = path+section+name+'.jpg'

img = cv2.imread(pathh, cv2.IMREAD_UNCHANGED)


width = 750
height = 750
dim = (width, height)
 
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
im =Image.fromarray(resized) #Image.open(pathh)
def add_margin(im):
    width, height = im.size
    new_width = width + 500 
    new_height = height 
    result = Image.new(im.mode, (new_width, new_height), (255,255,255))
    result.paste(im)
    return asarray(result)
	# Video Generating function
def generate_video():
	image_folder = '.' # make sure to use your folder
	video_name = 'captcha'+str(random.randint(1, 38))+'.avi'
	os.chdir("./")

	frame = add_margin(im)
	img = Image.fromarray(frame, 'RGB')
	img_drawable = ImageDraw.Draw(img)
	myFont = ImageFont.truetype("arial.ttf", 25)
	myFont = ImageFont.truetype("arial.ttf", 30)
	img_drawable.text((780, 80), "What do you see in this picture ?",font=myFont, fill =(213, 150, 77))
	x = random.randint(1, 4)
	captchaa=[]
	if (x == 1):
		captchaa.append(answer_cap)

		img_drawable.text((820, 200), "- "+captchaa[0],font=myFont, fill =(0, 0, 0))
		fruits=['apples','oranges','bananas','mangoes','grapes','strawberry']
		captchaa.append(random.choice(fruits))
		img_drawable.text((820, 250), "- "+captchaa[1],font=myFont, fill =(0, 0, 0))
		names=['Mario','Lugi','Kylian','Dembele','Sami','Karim']
		captchaa.append(random.choice(names))
		img_drawable.text((820, 300), "- "+captchaa[2],font=myFont, fill =(0, 0, 0))
		nothing=['Table','Chair','Pencil','Pen','Paper','Clip']
		captchaa.append(random.choice(nothing))
		img_drawable.text((820, 350), "- "+captchaa[3],font=myFont, fill =(0, 0, 0))
	elif(x == 2):
		fruits=['apples','oranges','bananas','mangoes','grapes','strawberry']
		captchaa.append(random.choice(fruits))

		img_drawable.text((820, 200), "- "+captchaa[0],font=myFont, fill =(0, 0, 0))
		captchaa.append(answer_cap)
		img_drawable.text((820, 250), "- "+captchaa[1],font=myFont, fill =(0, 0, 0))
		names=['Mario','Lugi','Kylian','Dembele','Sami','Karim']
		captchaa.append(random.choice(names))
		img_drawable.text((820, 300), "- "+captchaa[2],font=myFont, fill =(0, 0, 0))
		nothing=['Table','Chair','Pencil','Pen','Paper','Clip']
		captchaa.append(random.choice(nothing))
		img_drawable.text((820, 350), "- "+captchaa[3],font=myFont, fill =(0, 0, 0))
	elif(x == 3):
		fruits=['apples','oranges','bananas','mangoes','grapes','strawberry']
		captchaa.append(random.choice(fruits))

		img_drawable.text((820, 200), "- "+captchaa[0],font=myFont, fill =(0, 0, 0))
		names=['Mario','Lugi','Kylian','Dembele','Sami','Karim']
		captchaa.append(random.choice(names))
		img_drawable.text((820, 250), "- "+captchaa[1],font=myFont, fill =(0, 0, 0))
		captchaa.append(answer_cap)
		img_drawable.text((820, 300), "- "+captchaa[2],font=myFont, fill =(0, 0, 0))
		nothing=['Table','Chair','Pencil','Pen','Paper','Clip']
		captchaa.append(random.choice(nothing))
		img_drawable.text((820, 350), "- "+captchaa[3],font=myFont, fill =(0, 0, 0))

	elif(x == 4):
		fruits=['apples','oranges','bananas','mangoes','grapes','strawberry']
		captchaa.append(random.choice(fruits))

		img_drawable.text((820, 200), "- "+captchaa[0],font=myFont, fill =(0, 0, 0))
		names=['Mario','Lugi','Kylian','Dembele','Sami','Karim']
		captchaa.append(random.choice(names))
		img_drawable.text((820, 250), "- "+captchaa[1],font=myFont, fill =(0, 0, 0))
		nothing=['Table','Chair','Pencil','Pen','Paper','Clip']
		captchaa.append(random.choice(nothing))
		img_drawable.text((820, 300), "- "+captchaa[2],font=myFont, fill =(0, 0, 0))
		captchaa.append(answer_cap)
		img_drawable.text((820, 350), "- "+captchaa[3],font=myFont, fill =(0, 0, 0))


	
# Add Text to an image
	
	# setting the frame width, height width
	# the width, height of first image
	height, width, layers = asarray(img).shape

	video = cv2.VideoWriter(video_name, 0, 1, (width, height))

	# Appending the images to the video one by one
	for i in range(0,5):
		video.write(asarray(img))
	
	
	# Deallocating memories taken for window creation
	cv2.destroyAllWindows()
	video.release() # releasing the video generated
	captchaa.append(video_name)
	return captchaa
# Calling the generate_video function
print(generate_video())
#generate_video()


"""app = Flask(__name__)


@app.route('/get_image')
def get_image():
    vid = 
    return vid

app.run(host = '127.0.0.1' , port = 5000)
"""