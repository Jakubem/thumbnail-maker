from PIL import Image
import rawpy
import numpy
import imageio
import glob, os

file_ext = ".RW2"

# get and sort each raw file from root directory as list
paths = sorted(glob.glob("*"+file_ext))

# loop trough paths list and create tiff from each raw file
for index, item in enumerate(paths):
  file, ext = os.path.splitext(item)
  raw = rawpy.imread(paths[index])
  rgb = raw.postprocess()
  imageio.imsave(file + ".tiff", rgb)

# get path to current directory
dirpath = os.getcwd()

# create th directory for thumbnails
os.mkdir(dirpath + "/th")

# set max size for thumbnails
size = 1920, 1080

# generate resized jpg from each tiff
for infile in glob.glob("*.tiff"):
  file, ext = os.path.splitext(infile)
  im = Image.open(infile)
  im.thumbnail(size)
  im.save(dirpath + "/th/" + file + ".jpg")

# rename each file in root directory
for index, item in enumerate(paths):
  os.rename(item, str(index + 1) + file_ext)

# get and sort each thumbnail from th directory as list
thumb = sorted(glob.glob("th/" + "*.jpg"))

# rename each file in th directory
for index, item in enumerate(thumb):
  os.rename(item, "th/" + str(index + 1) + ".jpg")

# remove all tiff files form directory
tiffs = glob.glob("*.tiff")
for index, item in enumerate(tiffs):
  os.remove(tiffs[index])