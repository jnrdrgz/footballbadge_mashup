from PIL import Image
name = "centralcordoba"
img = Image.open(name+"1.png")
img = img.resize((868,862),Image.ANTIALIAS)
img.save(name+'.png')