# from PIL import Image, ImageDraw, ImageFont

# #Create an Image Object from an Image
# im = Image.open('a.png')
# width, height = im.size

# draw = ImageDraw.Draw(im)
# text = "sample watermark"

# font = ImageFont.truetype('a.ttf', 36)
# textwidth, textheight = draw.textsize(text, font)

# # calculate the x,y coordinates of the text
# margin = 10
# x = width - textwidth - margin
# y = height - textheight - margin

# # draw watermark in the bottom right corner
# draw.text((x, y), text, font=font)
# im.show()

# #Save watermarked image
# im.save('images/b.jpg')


from PIL import Image

im1 = Image.open('carbon.png')
width, height = im1.size
im2 = Image.open('wm.png')
width1, height1 = im2.size
back_im = im1.copy()
back_im.paste(im2,  (width - width1 -50, height - height1 - 100), im2)
back_im.save('post.png', quality=95)