import subprocess
from PIL import Image
from PIL.ExifTags import TAGS


file = "images/image_one.jpeg" # this input must receive some file from the html page --- check later
image = Image.open(file)

exifdata = image.getexif()

for tagid in exifdata: # this list must print the result in some html list

    tagname = TAGS.get(tagid, tagid)

    value = exifdata.get(tagid)

    print(f"metadata: {tagname:25}: {value}") 


exe_process = "hachoir-metadata"
process = subprocess.Popen(

    [exe_process, file],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    universal_newlines=True
)

dic = {}

for tag in process.stdout:
    line = tag.strip().split(':')
    dic[line[0].strip()] = line[-1].strip()

for k, v in dic.items():
    print(k, ':', v)
