# QR Code Generator

This Python program generates a QR code from user input and saves it as a PNG file. It uses the `qrcode` library to create the QR code and the `Pillow` library (PIL) to handle image operations.

## Prerequisites

Make sure you have Python installed on your system. You also need to install the following libraries:

- `qrcode`
- `Pillow`

You can install them using `pip`:

pip install qrcode[pil] pillow


## Usage
1. Run the program:
  python qr_code_generator.py

2.When prompted, enter the content you want to encode in the QR code. This can be a URL, text, or any other string.

3.The program will generate a QR code and save it as qr_code.png in the current directory.

4.The generated QR code image will also be displayed on the screen.

## Example

$ python qr_code_generator.py
Nhập nội dung cần tạo qr: https://example.com

This will create a QR code for https://example.com, save it as qr_code.png, and display it.
