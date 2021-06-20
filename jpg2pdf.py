import os 
from PIL import Image
os.system('clear') 
# im1 = Image.open('image1.jpg')
# im2 = Image.open('image2.jpg')
# # /Users/sagnikdebnath/Desktop/Periodic Test /Maths/
# # im = Image.new('RGB',(250,250),(250,250,250))
# # im.paste(im =im1)
# # im.paste(im = im2,box=(0,im1.size[1]))
# # im.save('image.pdf',format="PDF")
# # im.show()
# im1.size
# print(im1.size,im2.size,sep='\n\n')
def checklargestsize(listz):
    imagewidths = []
    imagelength = []
    for i in listz:
        imagelength.append(i.size[0])
        imagewidths.append(i.size[1])
    return max(imagelength), max(imagewidths)
def sortz(listz):
    newlist = []
    for i in range(0,len(listz)):
        newlist.append([listz[i].split('.')[0],i])
    newlist.sort(key=lambda a : int(a[0]))
    p = listz[0].split('.')[1]
    listz = []
    for i in newlist:
        listz.append(i[0]+'.'+str(p))
    return listz
path = os.path.abspath(str(input(':')))
ImagePath = []
ImageList =[]
ImagePath = os.listdir(path)
ImagePath.pop(0)
ImagePath = sortz(ImagePath)
c = 1
for imgpat in ImagePath:
    if c != 1 :
        im = Image.open(path+'/'+imgpat)
        ImageList.append(im)
    c = c+1 
l,b = checklargestsize(ImageList)
newim = Image.new('RGB',(l,b*len(ImageList)),(250,250,250))
for im in ImageList:
    if ImageList.index(im) == 0 :
        newim.paste(im=im)
    else: 
        newim.paste(im=im,box=(0,ImageList[ImageList.index(im)-1].size[0]))
newim.show()
newim.save('image.pdf',format="PDF")
newim.show()
