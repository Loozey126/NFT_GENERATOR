from ast import Return
from PIL import Image
import random
def create(nPNG):
    nIMG1 = input('How Many IMG for layer 1?\n')
    nIMG2 = input('How Many IMG for layer 2?\n')
    nIMG3 = input('How Many IMG for layer 3?\n')
    nIMG = range(int(nPNG))
    for i in nIMG:  
        background = Image.open(r".\LAYER\LAYER_1\\" + str(random.randint(1,int(nIMG1))) + '.png')
        layer1 = Image.open(r".\LAYER\LAYER_2\\" + str(random.randint(1,int(nIMG2))) + '.png')
        layer2 = Image.open(r".\LAYER\LAYER_3\\" + str(random.randint(1,int(nIMG3)))  + '.png')

        background = background.convert("RGBA")
        layer1 = layer1.convert("RGBA")
        layer2 = layer2.convert("RGBA")
        background.paste(layer1, mask=layer1)
        background.paste(layer2, mask=layer2)
        background.save(".\INPUT\\" + str(i) + ".png","PNG")
        print('Img'+str(i)+'.png printed')
