
# ======1.solution=========


import pywhatkit as pw



txt ="""Python is a high-level, interpreted programming language known for its simplicity and readability.
It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
Python is widely used in web development, data science, machine learning, automation, and more."""

pw.text_to_handwriting(txt,"demo1.png",[0,0,138])

print(' END ')

print("=================================================")


# ======2.solution=========


from PIL import Image, ImageDraw, ImageFont

# Load your handwriting-style font
font_path = "E:/python practice notes/Python projects begginner to advaced/QEGarrettWMoretz.ttf"  # replace with the path to your font
font = ImageFont.truetype(font_path, size=18)

text = """Python is a high-level, interpreted programming language known for its simplicity and readability.
It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
Python is widely used in web development, data science, machine learning, automation, and more."""

# Create an image
img = Image.new("RGB", (800, 600), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Draw the text
y = 10
for line in text.split('\n'):
    draw.text((10, y), line, font=font, fill=(0, 0, 138))
    y += 30

img.save("handwritten_output.png")
print("Image saved as handwritten_output.png")



print("=================================================")


# ======3.solution=========


from PIL import Image, ImageDraw, ImageFont

text = """Python is a high-level, interpreted programming language known for its simplicity and readability.
It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
Python is widely used in web development, data science, machine learning, automation, and more."""

# Create a white background image
img = Image.new("RGB", (800, 600), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Use default font
font = ImageFont.load_default()

# Draw text line by line
y = 10
for line in text.split('\n'):
    draw.text((10, y), line, font=font, fill=(0, 0, 138))
    y += 20

img.save("offline_handwriting.png")
print("Saved as offline_handwriting.png")
