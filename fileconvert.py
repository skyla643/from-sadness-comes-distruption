from PIL import Image

img = Image.open("UBQJABCLXU5MNJPAYM6QUTZA.jpg")  # Replace with your actual file name
img.save("input.png", "PNG")
print("Conversion successful! Saved as input.png")
