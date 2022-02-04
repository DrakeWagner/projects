from PIL import Image
import os

wd = 'c:\\Users\\dwagn\\Desktop\\'
pic_folder = wd + 'poke_pics'

def resizeAll(W, H):
    '''
    takes desired width and height
    '''
    iter = 0
    for file in os.listdir(pic_folder):
        iter += 1
        try:
            file = f"{pic_folder}\\{file}"
            im = Image.open(file) \
                 .resize((W, H), Image.ANTIALIAS)
            im.save(file)
            print(iter,'/',len(os.listdir(pic_folder)))
        except:
            print(f'file type for {file} not able to convert.')