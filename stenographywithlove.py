from PIL import Image
import numpy as np

# Function to encode a message into an image
def encode_message(image_path, message, output_path):
    image = Image.open(image_path)
    img_array = np.array(image)
    
    # Convert message to binary and add a stopping delimiter
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'
    
    flat_pixels = img_array.flatten()
    
    if len(binary_message) > len(flat_pixels):
        raise ValueError("Message is too long to encode in this image.")
    
    # Encode message into the least significant bits
    for i, bit in enumerate(binary_message):
        flat_pixels[i] = (flat_pixels[i] & ~1) | int(bit)
    
    # Reshape back to original image shape
    encoded_img_array = flat_pixels.reshape(img_array.shape)
    encoded_image = Image.fromarray(encoded_img_array.astype(np.uint8))
    encoded_image.save(output_path)
    print("Message encoded successfully!")

# Function to decode a hidden message from an image
def decode_message(image_path):
    image = Image.open(image_path)
    img_array = np.array(image)
    flat_pixels = img_array.flatten()
    
    binary_message = ""
    for pixel in flat_pixels:
        binary_message += str(pixel & 1)
    
    # Split binary string into 8-bit chunks and convert to characters
    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    message = "".join([chr(int(char, 2)) for char in chars])
    
    # Stop at the delimiter
    message = message.split("\ufffe")[0]  # Unicode equivalent of 1111111111111110
    print("Decoded message:", message)
    return message

# Example usage
# encode_message('input.png', 'Hello, Skyla!', 'encoded_image.png')
# decode_message('encoded_image.png')
