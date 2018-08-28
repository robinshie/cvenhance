from PIL import Image

img = Image.open("./imgs/empire.jpg").convert('L')

img.show()