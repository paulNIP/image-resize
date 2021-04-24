import PIL
from PIL import Image

mywidth = 48

img = Image.open('meta-ico-project.png')
wpercent = (mywidth/float(img.size[0]))

hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('ic_launcher.png')