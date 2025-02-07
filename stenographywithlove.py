from PIL import Image
import numpy as np

# Function to split a message into chunks
def split_message(message, chunk_size):
    return [message[i:i+chunk_size] for i in range(0, len(message), chunk_size)]

# Function to encode a message into an image
def encode_message(image_path, message, output_prefix):
    image = Image.open(image_path)
    img_array = np.array(image, dtype=np.uint8)  # Ensure proper uint8 handling
    flat_pixels = img_array.flatten()
    
    chunk_size = len(flat_pixels) // 8  # Estimate chunk size based on available space
    message_chunks = split_message(message, chunk_size)
    
    for index, chunk in enumerate(message_chunks):
        binary_message = ''.join(format(ord(char), '08b') for char in chunk) + '1111111111111110'
        
        if len(binary_message) > len(flat_pixels):
            raise ValueError("Message chunk is too long to encode in this image.")
        
        modified_pixels = flat_pixels.copy()
        
        for i, bit in enumerate(binary_message):
            new_value = (modified_pixels[i] & ~1) | int(bit)
            modified_pixels[i] = max(0, min(255, new_value))  # Ensure value stays in uint8 range
        
        encoded_img_array = modified_pixels.reshape(img_array.shape)
        encoded_image = Image.fromarray(encoded_img_array.astype(np.uint8))
        encoded_image.save(f"{output_prefix}_{index+1}.png")
    
    print(f"Message encoded successfully in {len(message_chunks)} chunks!")

# Function to decode a hidden message from images
def decode_message(image_paths):
    full_message = ""
    
    for image_path in image_paths:
        image = Image.open(image_path)
        img_array = np.array(image, dtype=np.uint8)
        flat_pixels = img_array.flatten()
        
        binary_message = ""
        for pixel in flat_pixels:
            binary_message += str(pixel & 1)
        
        chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
        message_chunk = "".join([chr(int(char, 2)) for char in chars])
        message_chunk = message_chunk.split("\ufffe")[0]
        
        full_message += message_chunk
    
    print("Decoded message:", full_message)
    return full_message

# Example usage
# encode_message('input.png', 'Your long message here', 'encoded_output')
# decode_message(['encoded_output_1.png', 'encoded_output_2.png'])
