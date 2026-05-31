"""
QR Code Generator Application
Developed for Biox Systems

This program accepts a URL from the user and generates a QR Code image.
The generated QR Code is saved as a PNG file.
"""

import qrcode
from urllib.parse import urlparse
from pathlib import Path


def is_valid_url(url):
    """
    Checks whether the entered URL is valid.

    Args:
        url (str): The URL entered by the user.

    Returns:
        bool: True if the URL is valid, otherwise False.
    """
    parsed_url = urlparse(url)
    return parsed_url.scheme in ["http", "https"] and parsed_url.netloc != ""


def generate_qr_code(url, file_name="biox_qr_code.png"):
    """
    Generates a QR Code image for the given URL.

    Args:
        url (str): The website URL to be converted into a QR Code.
        file_name (str): The name of the output QR Code image file.
    """

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")

    output_path = Path(file_name)
    qr_image.save(output_path)

    print("QR Code generated successfully.")
    print(f"Saved file name: {output_path}")


def main():
    """
    Main function that controls the application flow.
    """

    print("Biox Systems QR Code Generator")
    print("--------------------------------")

    url = input("Enter the URL to generate QR Code: ").strip()

    if is_valid_url(url):
        generate_qr_code(url)
    else:
        print("Invalid URL. Please enter a valid URL starting with http:// or https://")


if __name__ == "__main__":
    main()
