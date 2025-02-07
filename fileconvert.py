from PIL import Image

image_path = "input.jpg"  # Updated file name
img = Image.open(image_path)
img.save("input.png", "PNG")
print("Conversion successful! Saved as input.png")
