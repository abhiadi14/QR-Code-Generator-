import qrcode

def generate_qr_code(data, file_name):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(file_name)

if __name__ == "__main__":
    # Data to encode in the QR code
    data = input("Enter data to encode in the QR code: ")

    # File name for the QR code image
    file_name = input("Enter the file name to save the QR code image (with extension, e.g., qr_code.png): ")

    # Generate QR code
    generate_qr_code(data, file_name)
    print(f"QR code saved as {file_name}")
