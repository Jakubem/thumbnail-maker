from PIL import Image
import rawpy
import numpy
import imageio
import glob, os

dirpath = os.getcwd()

# katalog z kwadratami
cropped = dirpath + "/cropped"

if not os.path.exists(cropped):
  os.mkdir(dirpath + "/cropped")

src = sorted(glob.glob("*.jpg"))

for infile in src:
  file, ext = os.path.splitext(infile)
  im = Image.open(infile)
  if im.size[0] < im.size[1]:
    x1 = 0
    y1 = im.size[1]/2 - im.size[0]/2

    x2 = im.size[0]
    y2 = im.size[1]/2 + im.size[0]/2

  elif im.size[0] > im.size[1]:
    
    x1 = im.size[0]/2 - im.size[1]/2
    y1 = 0

    x2 = im.size[0]/2 + im.size[1]/2
    y2 = im.size[1]
  else:
    x1 = 0
    y1 = 0
    x2 = im.size[0]
    y2 = im.size[1]
        
  # print(im.size)
  # print(x, y)
  cropped = im.crop((
    x1,
    y1,
    x2,
    y2
  ))
  cropped.save("cropped/" + file + ".jpg")