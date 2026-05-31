# Biox Systems QR Code Generator

## Assignment Description

This Assignment is a Python-based QR Code generator application developed for Biox Systems. The application accepts a URL from the user and generates a QR Code image in PNG format. The QR Code can be scanned using a mobile phone or QR Code scanner to open the entered website link.

The example URL used in this Assignment is:

```text
https://www.bioxsystems.com/
```

## Purpose of the Assignment

The purpose of this Assignment is to create a simple QR Code generator application using Python. The application demonstrates how Python can be used to accept user input, validate a URL, generate a QR Code, and save the output as an image file.

## Tools and Technologies Used

- Python
- qrcode library
- Pillow library
- Visual Studio Code
- GitHub

## Assignment Files

The repository contains the following files:

```text
biox-qr-code-generator/
│
├── main.py
├── requirements.txt
├── README.md
└── biox_qr_code.png
```

## File Descriptions

### main.py

This is the main Python source code file. It contains the program that accepts a URL, validates the URL, generates a QR Code, and saves the QR Code as a PNG image.

### requirements.txt

This is the manifest file. It lists the required Python library needed to run the application.

### README.md

This file explains the project, setup instructions, running steps, expected output, and coding best practices followed.

### biox_qr_code.png

This is the generated QR Code image for the Biox Systems URL.

### application_output_screenshot.png

This screenshot shows the application output after running the program successfully.

## Installation Instructions

Before running the application, make sure Python is installed on your computer.

To install the required library, run the following command in the terminal:

```bash
pip install -r requirements.txt
```

## How to Run the Application

Open the project folder in Visual Studio Code or any preferred code editor.

Open the terminal and run the following command:

```bash
python main.py
```

For Mac users, the command may be:

```bash
python3 main.py
```

## Example Input

When the application asks for a URL, enter:

```text
https://www.bioxsystems.com/
```

## Final Output

The application generates a QR Code image file named:

```text
biox_qr_code.png
```

This file is saved in the project folder.

## Coding Best Practices Followed

The following coding best practices were followed in this project:

- Meaningful function names were used.
- The code was divided into separate functions.
- Comments and docstrings were included for better understanding.
- URL input validation was added.
- The program provides clear output messages.
- The code is simple, readable, and easy to maintain.

## Conclusion

This project successfully creates a QR Code generator application using Python. The application accepts a valid URL from the user and generates a QR Code image. The project meets the assignment requirements by including the Python source code, manifest file, generated QR Code output, screenshot, and GitHub repository files.
