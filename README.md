# **Steganography with Love**

## **Overview**
This project is a **steganography tool** that allows users to **hide messages inside images** using the **Least Significant Bit (LSB) encoding technique**. The method was famously used by **Cicada 3301**, a mysterious cryptographic organization, in their **hidden coded images**. This project was built as both a **technical challenge and an emotional expression**, providing a unique way to store messages hidden from plain sight.

## **How It Works**
This tool takes an **image file** (PNG format recommended) and **hides a secret message within its pixel data**. The encoded image appears **identical** to the original but contains the **hidden text**, which can only be retrieved using the decoding function.

### **Steganography Concept**
- Every pixel in an image consists of **RGB (Red, Green, Blue) values**.
- Each color value is represented as an **8-bit binary number**.
- This tool modifies **the least significant bit** of each pixel to store message data **without visibly altering the image**.

---

## **Setup Instructions**

### **1️⃣ Prerequisites**
Ensure you have the following installed:
- Python (3.6+ recommended)
- Virtual Environment (`venv`)
- Required Libraries: `Pillow` (PIL) and `NumPy`

To install dependencies:
```sh
pip install pillow numpy
```

---

### **2️⃣ Clone the Repository**
To get started, clone this repository:
```sh
git clone https://github.com/yourgithubusername/steganography-with-love.git
cd steganography-with-love
```

---

### **3️⃣ Setup Virtual Environment (Recommended)**
Create and activate a virtual environment:
```sh
python -m venv .venv
source .venv/bin/activate  # For Mac/Linux
.venv\Scripts\activate    # For Windows
```

---

## **Usage**

### **🔹 Encoding a Message into an Image**
Use the `encode_message` function to hide a secret message:
```sh
python -c "import stenographywithlove; stenographywithlove.encode_message('input.png', 'Your hidden message here', 'encoded_output')"
```
This will create an **encoded image** (`encoded_output_1.png`) with the hidden text inside.

---

### **🔹 Decoding a Hidden Message from an Image**
To retrieve the hidden message from an encoded image, run:
```sh
python -c "import stenographywithlove; stenographywithlove.decode_message(['encoded_output_1.png'])"
```
This will print the **hidden message** that was embedded inside the image.

---

## **Why This Project Matters**

### **Personal Significance**
This project serves as a **personal outlet**—a way to encode emotions, pain, and thoughts **inside an image** as a form of **expression and healing**. The idea is that **even if words can't be spoken, they can still be stored, hidden, and preserved** in a unique way.

### **Historical Connection to Cicada 3301**
This technique was **famously used by Cicada 3301**, a secretive organization that created one of the **most intricate cryptographic puzzles** on the internet. Their use of **steganography in images** helped create a **legendary puzzle that remains unsolved in parts today**.

---

## **Future Enhancements**
- **🔒 Encrypting the hidden message before encoding for added security.**
- **🎭 Adding image obfuscation techniques to make detection even harder.**
- **🛠 GUI implementation for user-friendly interaction.**

---

## **License**
This project is open-source and available under the **MIT License**.

#### **🔹 Built with Love, Code, and Hidden Messages.**

## WITH LOVE SMRCCC3301 
