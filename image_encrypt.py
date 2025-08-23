import argparse
from PIL import Image
import numpy as np


def process_image(input_file, output_file, mode, op, key=None):
    img = Image.open(input_file)
    arr = np.array(img)

    if op in ["add", "sub", "xor"]:
        if key is None:
            raise ValueError("This operation needs a --key (0-255)")

        if op == "xor":
            result = arr ^ key

        elif op == "add":
            if mode == "encrypt":
                result = (arr.astype(np.int16) + key) % 256
            else:  # decrypt
                result = (arr.astype(np.int16) - key) % 256

        elif op == "sub":
            if mode == "encrypt":
                result = (arr.astype(np.int16) - key) % 256
            else:  # decrypt
                result = (arr.astype(np.int16) + key) % 256

        result = result.astype(np.uint8)

    elif op == "flip":
        result = np.flipud(arr)

    else:
        raise ValueError("Unsupported operation")

    Image.fromarray(result).save(output_file)
    print(f"{mode.capitalize()}ed image saved: {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image Encryption/Decryption Tool")
    parser.add_argument("-i", "--input", required=True, help="Input image file")
    parser.add_argument("-o", "--output", required=True, help="Output image file")
    parser.add_argument("-m", "--mode", choices=["encrypt", "decrypt"], required=True, help="Mode")
    parser.add_argument("--op", choices=["add", "sub", "xor", "flip"], required=True, help="Operation")
    parser.add_argument("--key", type=int, help="Key (0-255) for add/sub/xor")

    args = parser.parse_args()

    process_image(args.input, args.output, args.mode, args.op, args.key)
