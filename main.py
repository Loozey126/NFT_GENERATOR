import random
import shutil
import imageio
import os
import glob
import json
import imgCreator

def createMetadata():
    IMAGES_BASE_URL = config["imgUrl"]
    NFT_NAME = config["nft-name"]
    COLLECTION_NAME = config["collection-name"]
    NFT_DESCRIPTION = config["nft-description"]
    nomi = config["name-list"]
    sesso = config["gender-list"]
    metadata = {
    "nft_name" : NFT_NAME + str(i),
    "description" : NFT_DESCRIPTION,
    "collection" : COLLECTION_NAME,
    "properties" : [
        {   
            "type":"Name",
            "name": random.choice(nomi)
        },
        {
            "type": "Gender",
            "name": random.choice(sesso)
        }
    ],
    "levels" : [
        {
            "name" : "Vision",
            "from" : random.randint(0,10),
            "to" : 10
        }
    ],
    "stats" : [
           {
             "name": "Age",
             "from": random.randint(0,100),
             "to": 100
           }
    ],
}
    with open(str(i) + ".json", "w") as outfile:
        json.dump(metadata, outfile,indent=4)
    shutil.move(str(i) + ".json",r'.\OUTPUT\METADATA')
def moveImg(src, dest):
    shutil.copy(src, dest)
def clearImg(dest):
    img = glob.glob(dest + '\\*')
    for f in img:
        os.remove(f)
def createImg(gifDest,format):
     
    imgGIF = []
    imgNames = (iN for iN in os.listdir(buffer) if iN.endswith(format))
    # Note:
    #     The serial number in the name of input images should have the same length (e.g., '00', '01', ...).
    #     If not, the 'sorted()' function will return the wrong order of images.

    for imgName in imgNames:
        imgGIF.append(imageio.imread(buffer +'\\' + imgName))
    imageio.mimsave(gifDest + GIF_NAME_DIFF, imgGIF, duration=DURATION_FRAME)

ciclo = input('[1] Create PNG From Layers\n[2] Create GIF From PNG\n\n Choose an option (1/2)\n')

if ciclo == '1':
    nPNG = input('How Many IMG do you need?\n')
    imgCreator.create(nPNG)
    answer = input('Do you want to make some GIF now?\n[y/n]\n')
    if answer == 'y':
        with open("config.json", "r") as configFile:
            config = json.load(configFile)
        gifDest = config["destination"]
        buffer = r'.\BUFFER'
        imgSrc = config["source"]
        answer = int(input('Hello, how many GIF do you need?\n'))
        numGif = range(answer)
        nPNG = int(nPNG) - 1
        DURATION_FRAME = input('Set frame duration time\n')
        for i in numGif:
            GIF_NAME_DIFF = "img" + str(i) + '.gif'
            clearImg(buffer)
            nFrame = range(random.randint(5,11))
            for frames in nFrame:
                global ran 
                ran = str(random.randint(0,int(nPNG)))
                src = imgSrc + '\\' + ran + '.png'
                moveImg(src, buffer)
            createImg(gifDest, '.png')
            createMetadata()
            print(GIF_NAME_DIFF +' Print Done')

elif ciclo == '2':
    with open("config.json", "r") as configFile:
        config = json.load(configFile)
    gifDest = config["destination"]
    buffer = r'.\BUFFER'
    imgSrc = config["source"]
    answer = int(input('Hello, how many GIF do you need?\n'))
    numGif = range(answer)
    nPNG  = len(glob.glob1(r'.\INPUT',"*.pdf"))
    DURATION_FRAME = input('Set frame duration time\n')
    for i in numGif:
        GIF_NAME_DIFF = "img" + str(i) + '.gif'
        clearImg(buffer)
        nFrame = range(random.randint(5,11))
        for frames in nFrame: 
            ran = str(random.randint(0,nPNG))
            src = imgSrc + '\\' + ran + '.png'
            moveImg(src, buffer)
        createImg(gifDest, '.png')
        createMetadata()
        print(GIF_NAME_DIFF +' Print Done')
else: print('ERROR: Unknow Response')
