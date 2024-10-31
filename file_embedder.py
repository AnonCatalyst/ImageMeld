import zipfile
from pathlib import Path

class Colors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def compress_files(file_paths, zip_name):
    """Compress multiple files into a ZIP file."""
    try:
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for file_path in file_paths:
                # Ensure the file exists before adding it to the zip
                if Path(file_path).is_file():
                    zip_file.write(file_path, arcname=Path(file_path).name)
                    print(f"{Colors.OKBLUE}Added {file_path} to {zip_name}.{Colors.ENDC}")
                else:
                    print(f"{Colors.FAIL}Error: {file_path} does not exist.{Colors.ENDC}")
        print(f"{Colors.OKGREEN}Compressed {len(file_paths)} files into {zip_name}.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Error during compression: {e}{Colors.ENDC}")

def embed_file_in_image(image_path, file_path, output_image):
    """Embed a single file into an image."""
    try:
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()

        with open(file_path, 'rb') as f:
            file_data = f.read()

        # Prepare the file size as 4 bytes
        file_size = len(file_data)
        size_bytes = file_size.to_bytes(4, byteorder='big')

        # Write the new image with embedded file
        with open(output_image, 'wb') as output_file:
            output_file.write(img_data + file_data + size_bytes)  # Append file data and size at the end

        print(f"{Colors.OKGREEN}Successfully embedded {file_path} into {output_image}.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Error during embedding: {e}{Colors.ENDC}")
