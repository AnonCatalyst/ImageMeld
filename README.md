# ImageMeld

**ImageMeld** is a powerful tool that allows you to embed files into images using steganography techniques. By leveraging the image's binary structure, you can securely store data within image files, making it an innovative solution for data concealment.

``Project development for this project is on hold``

## Features
- **File Embedding**: Embed one or more files into an image without noticeable changes.
- **ZIP Compression**: Optional automatic compress multiple files into a single ZIP archive before embedding.
- **Dependency Management**: Automatically checks and installs required dependencies.
- **User-Friendly Interface**: Interactive prompts guide you through the embedding process.

## Install & Run

- Requirements will auto install
1. `git clone https://github.com/AnonCatalyst/ImageMeld`
2. `cd ImageMeld`
3. `python3 imagemeld.py`

## Display Example

```
Welcome to ImageMeld!
Choose an option:
1. Embed files into an image
0. Exit
Enter your choice: 1
Enter the path to the input image file: Chase-National-Bank-Logo-500x281.ico
Enter the path for the output image file: Chase-National-Bank-Logo-500x2812.ico       
Enter the paths of the files to embed (separated by commas): BANKING.scr, BANKINFO.exe
Do you want to compress these files into a ZIP before embedding? (y/n): n
Successfully embedded BANKING.scr into Chase-National-Bank-Logo-500x2812.ico.
Successfully embedded BANKINFO.exe into Chase-National-Bank-Logo-500x2812.ico.
```
