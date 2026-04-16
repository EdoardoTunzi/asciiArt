# %%
from PIL import Image
import matplotlib.pyplot as plt

img_path = "emma_stone.jpeg"

img = plt.imread(img_path)
print(img.shape)
plt.imshow(img)

emma = Image.open(img_path)

""" for pixel in emma.getdata():
    print(pixel) """

grayscale = emma.convert("LA")
reduced = grayscale.resize((96, 96))
plt.imshow(reduced)

chars = ["@", "#", "$", "_", "|", "-"]

pixel_tuple = reduced.getdata()[0]
# print(pixel_tuple[0])

num_intervals = int(256 / len(chars))

div = pixel_tuple[0] / num_intervals

ascii_string = ""

for px in reduced.getdata():
    ascii_string += chars[int(px[0] / num_intervals)]

for i in range(0, len(ascii_string), reduced.width):
    print(ascii_string[i : i + reduced.width])

# %%
