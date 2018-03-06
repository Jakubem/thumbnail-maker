## Simple scripts to automate my photo editing workflow

Run `pip install -r requirements.txt` to install all dependencies.

### To convert raw to jpg:
  Run ```convert.py``` in directory with your raw files. <br/> It'll create ```th``` folder with resized jpg's <br/>
  For files other than RW2 you have to edit ```file_ext``` variable. <br/>
  ```reduce.py``` will remove each raw file that match deleted jpg from th folder.

### To optimize all jpg files in directory:
  Run ```optimize.py``` in directory with your jpg files. <br/> It'll create ```optimized``` folder with optimized files.

### To crop all jpg files in directory to square:
  Based on [Crop Images with PIL/Pillow](http://matthiaseisen.com/pp/patterns/p0202/) <br/>
  Run ```crop.py``` in directory with your jpg files. <br/> It'll create ```cropped``` folder with cropped files.
