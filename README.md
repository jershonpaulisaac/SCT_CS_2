# Image Encryption/Decryption Tool

**Author:** Jershon Paul Isaac R  
**Internship Task:** Task 2 – SkillCraft Technology Internship (Cybersecurity)  

---

## Overview

This Python project is an **Image Encryption/Decryption Tool** that allows users to securely encrypt and decrypt images using multiple operations. The tool supports different encryption techniques and can be run via a simple **command-line interface**.

It is designed for **learning basic image-based cryptography** while practicing Python and NumPy skills.

---

## Features

- **XOR Encryption/Decryption:** Perform bitwise XOR on each pixel with a key.  
- **Addition/Subtraction Encryption/Decryption:** Modify pixel values with a key, supporting both encryption and decryption.  
- **Vertical Flip:** Flip the image upside down (no key required).  
- **Customizable Key:** Users can provide a key (0–255) for add, sub, and xor operations.  
- **Command-Line Interface:** Easy to use and automate.

---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/image-encryption-tool.git
cd image-encryption-tool
Install dependencies:

bash
Copy
Edit
pip install pillow numpy
Usage
Run the tool using the command line:

bash
Copy
Edit
python image_tool.py -i <input_file> -o <output_file> -m <mode> --op <operation> [--key <key>]
Arguments:
-i, --input : Input image file (required)

-o, --output : Output image file (required)

-m, --mode : Mode of operation (encrypt or decrypt)

--op : Operation to perform (add, sub, xor, flip)

--key : Key value for encryption/decryption (required for add, sub, xor; 0–255)

Examples
1. XOR Encryption:

bash
Copy
Edit
python image_tool.py -i input.png -o encrypted.png -m encrypt --op xor --key 123
2. XOR Decryption:

bash
Copy
Edit
python image_tool.py -i encrypted.png -o decrypted.png -m decrypt --op xor --key 123
3. Add Encryption:

bash
Copy
Edit
python image_tool.py -i input.png -o encrypted.png -m encrypt --op add --key 50
4. Flip Image Vertically:

bash
Copy
Edit
python image_tool.py -i input.png -o flipped.png -m encrypt --op flip
How It Works
Loading the Image:
The tool uses the Python Imaging Library (PIL) to open the image and convert it into a NumPy array for pixel manipulation.

Applying Operations:

XOR: Performs bitwise XOR between each pixel and the key.

Add/Subtract: Modifies each pixel value using the key with wrapping (0–255) using modulo arithmetic.

Flip: Vertically flips the image using NumPy.

Saving the Output:
The modified array is converted back into an image and saved as the output file.

Contribution
Contributions are welcome! You can:

Add more encryption techniques

## License

© 2025 Jershon Paul Isaac R. All rights reserved.  

This software and its source code are **protected**. You may **view and use** the code for personal or educational purposes **only**.  
**Modification, distribution, or commercial use** of this code **is strictly prohibited** without **prior written permission** from the author.  

Implement GUI for easier usage

Optimize performance for larger images
