"""
QR Code Generator Application
Developed for Biox Systems

This application allows the user to enter any URL dynamically
and generates a QR Code preview using a graphical user interface.
"""

import tkinter as tk
from tkinter import messagebox
from urllib.parse import urlparse
from pathlib import Path

import qrcode
from PIL import ImageTk


def is_valid_url(url):
    """
    Checks whether the entered URL is valid.

    Args:
        url (str): URL entered by the user.

    Returns:
        bool: True if the URL is valid, otherwise False.
    """
    parsed_url = urlparse(url)
    return parsed_url.scheme in ["http", "https"] and parsed_url.netloc != ""


def update_preview_url(event=None):
    """
    Updates the preview URL text when the user types in the input field.
    """
    url = url_entry.get().strip()

    if url:
        preview_url_label.config(text=url)
    else:
        preview_url_label.config(text="No URL entered")


def generate_qr_code():
    """
    Generates and displays a QR Code based on the URL entered by the user.
    """

    url = url_entry.get().strip()

    if not is_valid_url(url):
        messagebox.showerror(
            "Invalid URL",
            "Please enter a valid URL starting with http:// or https://"
        )
        return

    preview_url_label.config(text=url)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    output_path = Path("biox_qr_code.png")
    qr_image.save(output_path)

    qr_image = qr_image.resize((250, 250))

    qr_photo = ImageTk.PhotoImage(qr_image)

    qr_display_label.config(image=qr_photo)
    qr_display_label.image = qr_photo

    messagebox.showinfo(
        "Success",
        "QR Code generated successfully and saved as biox_qr_code.png"
    )


# Create main application window
window = tk.Tk()
window.title("QR Code Generator")
window.geometry("700x600")
window.configure(bg="#f2f2f2")
window.resizable(False, False)

# Title label
title_label = tk.Label(
    window,
    text="QR Code Generator",
    font=("Arial", 24, "bold"),
    bg="#f2f2f2",
    fg="black"
)
title_label.pack(pady=25)

# URL input label
url_label = tk.Label(
    window,
    text="Enter URL:",
    font=("Arial", 12),
    bg="#f2f2f2",
    fg="black"
)
url_label.pack()

# URL input field
url_entry = tk.Entry(
    window,
    width=55,
    font=("Arial", 12),
    justify="left"
)
url_entry.pack(pady=10)

# Update preview URL dynamically while typing
url_entry.bind("<KeyRelease>", update_preview_url)

# Preview label
preview_label = tk.Label(
    window,
    text="Preview URL:",
    font=("Arial", 12, "bold"),
    bg="#f2f2f2",
    fg="blue"
)
preview_label.pack(pady=(15, 0))

# Preview URL display
preview_url_label = tk.Label(
    window,
    text="No URL entered",
    font=("Arial", 12),
    bg="#f2f2f2",
    fg="blue"
)
preview_url_label.pack(pady=5)

# Generate button
generate_button = tk.Button(
    window,
    text="Generate QR Code",
    font=("Arial", 12, "bold"),
    bg="black",
    fg="white",
    width=25,
    height=2,
    command=generate_qr_code
)
generate_button.pack(pady=15)

# QR Code preview text
qr_preview_label = tk.Label(
    window,
    text="QR Code Preview:",
    font=("Arial", 14, "bold"),
    bg="#f2f2f2",
    fg="black"
)
qr_preview_label.pack(pady=10)

# QR Code display area
qr_display_label = tk.Label(
    window,
    bg="white",
    width=250,
    height=250
)
qr_display_label.pack(pady=5)

# Run the application
window.mainloop()