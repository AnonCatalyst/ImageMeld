import os
from PIL import Image

class Colors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def extract_embedded_files(image_path):
    """Extract embedded files from an image and return a list of file names."""
    try:
        embedded_files = []
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()
            # Check for embedded file data by reading the last 4 bytes (file size placeholder)
            while len(img_data) > 4:
                file_size = int.from_bytes(img_data[-4:], byteorder='big')
                file_data = img_data[-(file_size + 4):-4]
                embedded_files.append({'name': f"extracted_{len(embedded_files) + 1}.bin", 'data': file_data, 'size': file_size})
                img_data = img_data[:-(file_size + 4)]
        return embedded_files
    except Exception as e:
        print(f"{Colors.FAIL}Error during extraction: {e}{Colors.ENDC}")
        return []
