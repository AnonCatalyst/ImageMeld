import os
from PIL import Image
import mimetypes

class Colors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def extract_embedded_files(image_path, output_dir='extracted_files'):
    """Extract embedded files from an image and save them to a specified directory."""
    try:
        embedded_files = []

        # Read the image data
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()

        # Ensure we start extracting from the end of the image data
        while len(img_data) > 4:
            # Read the last 4 bytes as file size
            file_size = int.from_bytes(img_data[-4:], byteorder='big')
            
            if file_size > len(img_data) - 4:
                print(f"{Colors.FAIL}Invalid file size detected. Stopping extraction.{Colors.ENDC}")
                break
            
            # Extract the file data based on the file size
            file_data = img_data[-(file_size + 4):-4]

            # Generate a unique name for the extracted file with appropriate extension
            extracted_file_name = f'extracted_{len(embedded_files) + 1}'
            # Guess the file type based on the content of the file data
            file_extension = mimetypes.guess_extension(mimetypes.guess_type(file_data)[0] or 'application/octet-stream')
            extracted_file_name += file_extension

            embedded_files.append({
                'name': extracted_file_name,
                'data': file_data,
                'size': file_size
            })

            # Update img_data to remove the extracted file's data
            img_data = img_data[:-(file_size + 4)]

        # Create a directory for extracted files
        os.makedirs(output_dir, exist_ok=True)

        # Save each extracted file in the new directory
        for embedded_file in embedded_files:
            extracted_file_path = os.path.join(output_dir, embedded_file['name'])
            with open(extracted_file_path, 'wb') as out_file:
                out_file.write(embedded_file['data'])
            print(f"{Colors.OKGREEN}Extracted {embedded_file['name']} of size {embedded_file['size']} bytes.{Colors.ENDC}")

        if not embedded_files:
            print(f"{Colors.FAIL}No embedded files found.{Colors.ENDC}")

        return embedded_files

    except Exception as e:
        print(f"{Colors.FAIL}Error during extraction: {e}{Colors.ENDC}")
        return []

