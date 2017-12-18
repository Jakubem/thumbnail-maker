from PIL import Image
import rawpy
import numpy
import imageio
import glob, os

dirpath = os.getcwd()
os.mkdir(dirpath + "/cropped")

src = sorted(glob.glob("*.jpg"))

for infile in src:
  file, ext = os.path.splitext(infile)
  im = Image.open(infile)
  short_side = min(im.size)
  x = (short_side - im.size[0])/2
  y = (short_side - im.size[1])/2
  cropped = im.crop((
    -x,
    -y,
    im.size[0] + x,
    im.size[1] + y
  ))
  cropped.save("cropped/" + file + ".jpg")