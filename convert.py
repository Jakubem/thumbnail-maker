from PIL import Image
import rawpy
import numpy
import imageio
import glob, os

paths = sorted(glob.glob("*.RW2"))
for index, item in enumerate(paths):
  raw = rawpy.imread(paths[index])
  rgb = raw.postprocess()
  imageio.imsave(item + ".tiff", rgb)

dirpath = os.getcwd()
os.mkdir(dirpath + "/th")

size = 1920, 1080
  
for infile in glob.glob("*.tiff"):
  file, ext = os.path.splitext(infile)
  im = Image.open(infile)
  im.thumbnail(size)
  im.save(dirpath + "/th/" + file + ".jpg")

for index, item in enumerate(paths):
  os.rename(item, str(index) + ".RW2")
  
thumb = sorted(glob.glob("th/" + "*.jpg"))
for index, item in enumerate(thumb):
  os.rename(item, "th/" + str(index) + ".jpg")

tiffs = glob.glob("*.tiff")
for index, item in enumerate(tiffs):
  os.remove(tiffs[index])