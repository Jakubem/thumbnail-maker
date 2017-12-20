from PIL import Image, ImageFilter
import rawpy
import numpy
import imageio
import glob, os

dirpath = os.getcwd()

file_ext = ".NEF"

src = sorted(glob.glob("*"+file_ext))

os.chdir(dirpath + "/th")
thumbnails = sorted(glob.glob("*.jpg"))
os.chdir(dirpath)
raw = []
remove_raw = []
jpg = []

for index_raw, item_raw in enumerate(src):
  file_raw, ext_raw = os.path.splitext(item_raw)
  raw.append(item_raw)
  for index, item in enumerate(thumbnails):
    file, ext = os.path.splitext(item)
    if file == file_raw:
      remove_raw.append(item_raw)
      break
  continue

for i in remove_raw:
  raw.remove(i)
for i in raw:
  os.remove(i)
