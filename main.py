from PIL import Image
from colormap import rgb2hex
from past.builtins import xrange
import win32gui


image = "cow.jpg"  # Change this
offsetx = 0            
offsety = 0        
loop = True            


def get_image(image_path):
    global width, height
    image = Image.open(image_path, "r")
    width, height = image.size
    
    
    pixel_values = list(image.getdata())

    return pixel_values


image = get_image(image)


num = 0
num2 = 0

hdc = win32gui.GetDC(0)


def draw_image(num, num2):
    for n in xrange(width * height):

        tup = image[n]
        r = tup[2]
        g = tup[1]
        b = tup[0]
        hex = rgb2hex(r, g, b).replace("#", "")
        hexb = int(hex, 16)
    
        win32gui.SetPixel(hdc, num + offsetx, num2 + offsety, hexb)
        
            
        if num == width:
            num2 += 1
            num = 0
        num += 1
    num2 = 0



# loop
while loop:
    draw_image(num, num2)


# no loop
if loop == False:
    draw_image(num, num2)
# this was a 3 am coding project and i am VERY tired rn so don't blame me for bad coding!
