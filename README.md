# ImageMeld

**ImageMeld** is a powerful tool that allows you to embed files into images using steganography techniques. By leveraging the image's binary structure, you can securely store data within image files, making it an innovative solution for data concealment.

## Features
- **File Embedding**: Embed one or more files into an image without noticeable changes.
- **ZIP Compression**: Automatically compress multiple files into a single ZIP archive before embedding.
- **Easy Extraction**: Effortlessly extract embedded files from the image.
- **Dependency Management**: Automatically checks and installs required dependencies.
- **User-Friendly Interface**: Interactive prompts guide you through the embedding and extraction process.

## Install & Run

- Requirements will auto install
1. `git clone https://github.com/AnonCatalyst/ImageMeld`
2. `cd ImageMeld`
3. `python3 imagemeld.py`

## Display Example

```
Welcome to ImageMeld!

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

Enter the path to the input image file: test.png
Enter the path for the output image file: testoutput.png         
Enter the paths of the files to embed (separated by commas): test.py
Embedded test.py into testoutput.png. File size: 25 bytes.
Extracting file size: 1847732490 bytes.
```
