# Program that expects exactly two command-line arguments:
#
# -- in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
# -- in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
#
# The program should then overlay shirt.png (which has a transparent background) on the input
# after resizing and cropping the input to be the same size, saving the result as its output.

from PIL import Image, ImageOps
import os
import os.path
import sys

def main():
    # Verify if less than 2 arguments are passed
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # Verify if more than 2 arguments are passed
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # Only chance to have is 2 arguments passed
    else:
        if verify_arguments(sys.argv):
            create_output_file(sys.argv)


def verify_arguments(args):
    # Read arguments received
    arg1 = args[1]
    arg2 = args[2]
    # Check files in arguments received
    files_accepted = ('.jpg', '.jpeg', '.png')
    # Check if both files are supported
    if arg1.lower().endswith(files_accepted) and arg2.lower().endswith(files_accepted):
        # Check if both files are of identic suffix
        file1_suffix = arg1.lower().split('.')
        file2_suffix = arg2.lower().split('.')
        if file1_suffix[1] == file2_suffix[1]:
            # Check if base file exists
            if os.path.exists(arg1):
                return True
            else:
                sys.exit("Input does not exist")
        else:
            sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid output")


def create_output_file(args):
    # Read arguments received
    input_image = args[1]
    output_image = args[2]
    # Look for size in image to overlay
    overlay = Image.open("shirt.png")
    size = overlay.size
    # Resize input image to overlay size
    image_in = Image.open(input_image)
    image_in = ImageOps.fit(image_in, size)
    image_in.paste(overlay, (0,0), overlay)
    image_in.save(output_image)


if __name__ == "__main__":
    main()
