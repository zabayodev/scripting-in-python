from PIL import Image, ImageFilter
import PIL
import PIL.ImageSequence


img = Image.open('./yellow/1.png')
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("blur.png", 'png')
print(img)