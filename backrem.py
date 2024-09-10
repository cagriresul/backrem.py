from humanfriendly.terminal import output
from rembg import remove

input_path = "images.jpeg"

output_path = "output.png"

# png olarak alma nedenimiz ona uygun olmasından kaynaklı

with open(input_path, "rb") as i :    # input path'i read binary olarak aç dedik
    with open(output_path ,"wb") as o:
        input = i.read()
        output = remove(input)
        o.write(output)