from PIL import Image

im = Image.open("images/photo.jpg")

print("Nom : photo.jpg")
print("Format :", im.format)
print("Dimensions :", im.size)
print("Mode :", im.mode)


im = Image.open("images/photo.jpg")

region = im.crop((0, 0, 200, 200))

region.save("images/decoupage.jpg")