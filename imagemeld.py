import os
import zipfile
import sys
import subprocess
from PIL import Image

# ANSI color codes for colored output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def install_package(package):
    """Install the required package using pip."""
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--break-system-packages', '--user', package])

def check_dependencies():
    """Check and install required dependencies."""
    try:
        import PIL  # Check if Pillow is installed
    except ImportError:
        print(f"{Colors.WARNING}Pillow not found. Installing Pillow...{Colors.ENDC}")
        install_package('Pillow')

def print_usage():
    """Display the usage instructions for the script."""
    usage_text = f"""
{Colors.HEADER}{Colors.BOLD}Welcome to ImageMeld!{Colors.ENDC}

This script allows you to embed one or more files into an image using steganography techniques.

You will be prompted to enter the paths for:
- The input image file (must be in a supported format like PNG).
- The output image file that will contain the embedded data.
- The files you want to embed (you can enter multiple files, separated by commas).

Example:
To embed a single file:
input.png, output.png, file1.exe

To embed multiple files:
input.png, output.png, file1.exe, file2.txt, file3.scr

Notes:
- The input image must have enough capacity to hold the data from the files being embedded.
- The output image will contain the embedded data at the end of the image file.
- If multiple files are specified, they will be compressed into a ZIP archive before embedding.

After running the script, the embedded files can be extracted from the output image.
"""
    print(usage_text)

def compress_files(file_paths, zip_name):
    """Compress multiple files into a ZIP archive."""
    with zipfile.ZipFile(zip_name, 'w') as zip_file:
        for file_path in file_paths:
            zip_file.write(file_path, os.path.basename(file_path))
    print(f"{Colors.OKGREEN}Compressed {len(file_paths)} files into {zip_name}.{Colors.ENDC}")

def embed_file_in_image(image_path, file_path, output_image):
    """Embed a file into an image."""
    # Load image
    img = Image.open(image_path)

    # Save the original image
    img.save(output_image)

    # Convert file to binary
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Append the file size at the end of the image
    file_size = len(file_data)
    file_size_bytes = file_size.to_bytes(4, byteorder='big')

    # Append the file size and file data to the end of the image file
    with open(output_image, 'ab') as img_file:
        img_file.write(file_size_bytes)
        img_file.write(file_data)

    print(f"{Colors.OKBLUE}Embedded {file_path} into {output_image}. File size: {file_size} bytes.{Colors.ENDC}")

def extract_file_from_image(image_path):
    """Extract the embedded file from the image."""
    with open(image_path, 'rb') as img_file:
        # Seek to the end of the file and read the last 4 bytes to get the file size
        img_file.seek(-4, os.SEEK_END)
        file_size_bytes = img_file.read(4)

        # Check if we actually read 4 bytes
        if len(file_size_bytes) < 4:
            raise ValueError("Could not read file size from the end of the image.")

        file_size = int.from_bytes(file_size_bytes, byteorder='big')
        print(f"{Colors.OKBLUE}Extracting file size: {file_size} bytes.{Colors.ENDC}")

        # Now seek back to read the file data
        img_file.seek(-4 - file_size, os.SEEK_END)

        # Check if seeking back is valid
        current_position = img_file.tell()
        print(f"{Colors.OKBLUE}Current position for reading data: {current_position}.{Colors.ENDC}")

        if current_position < 0:
            raise ValueError("Invalid position for extracting file data.")

        file_data = img_file.read(file_size)

    return file_data

def main():
    # Check and install dependencies
    check_dependencies()

    print_usage()

    # Take user inputs
    image_path = input("Enter the path to the input image file: ")
    output_image = input("Enter the path for the output image file: ")
    file_paths_input = input("Enter the paths of the files to embed (separated by commas): ")

    # Split the input into a list and strip any whitespace
    file_paths = [file.strip() for file in file_paths_input.split(',')]

    if len(file_paths) == 1:
        # If a single file is provided, embed it directly
        embed_file_in_image(image_path, file_paths[0], output_image)
    else:
        # If multiple files are provided, compress and embed them
        zip_name = 'files.zip'
        compress_files(file_paths, zip_name)
        embed_file_in_image(image_path, zip_name, output_image)

    # Optional: Extract and save the file for testing
    try:
        extracted_data = extract_file_from_image(output_image)
        with open('extracted_files.zip', 'wb') as extracted_file:
            extracted_file.write(extracted_data)
        print(f"{Colors.OKGREEN}Extracted embedded file to 'extracted_files.zip'.{Colors.ENDC}")
    except Exception as e:
        #print(f"{Colors.FAIL}An error occurred during extraction: {e}{Colors.ENDC}")
        print("")

if __name__ == "__main__":
    main()
