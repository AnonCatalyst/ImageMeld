import sys
import subprocess
from file_extractor import extract_embedded_files, Colors


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

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

def main_menu():
    """Display the main menu and get user choice."""
    print(f"{Colors.HEADER}{Colors.BOLD}Welcome to ImageMeld!{Colors.ENDC}")
    print("Choose an option:")
    print(f"{Colors.OKBLUE}1. Embed files into an image{Colors.ENDC}")
    print(f"{Colors.FAIL}0. Exit{Colors.ENDC}")

    choice = input("Enter your choice: ")
    return choice

def embed_file_menu():
    """Menu for embedding files into an image."""
    image_path = input("Enter the path to the input image file: ")
    output_image = input("Enter the path for the output image file: ")
    file_paths_input = input("Enter the paths of the files to embed (separated by commas): ")

    # Split the input into a list and strip any whitespace
    file_paths = [file.strip() for file in file_paths_input.split(',')]

    # Ask if the user wants to compress files
    compress_choice = input("Do you want to compress these files into a ZIP before embedding? (y/n): ")
    if compress_choice.lower() == 'y':
        zip_name = 'files.zip'
        compress_files(file_paths, zip_name)
        embed_file_in_image(image_path, zip_name, output_image)
    else:
        # Embed each file individually
        for file_path in file_paths:
            embed_file_in_image(image_path, file_path, output_image)

def main():
    """Main function to control the flow of the program."""
    check_dependencies()

    while True:
        choice = main_menu()

        if choice == '1':
            # Embedding functionality
            embed_file_menu()
        
        elif choice == '0':
            print(f"{Colors.OKGREEN}Exiting ImageMeld. Goodbye!{Colors.ENDC}")
            break
        else:
            print(f"{Colors.WARNING}Invalid choice. Please try again.{Colors.ENDC}")

if __name__ == "__main__":
    main()
