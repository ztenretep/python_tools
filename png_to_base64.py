#!/usr/bin/env python3
"""Convert a given png image to a base64 encoded image.

The standard Python module base64 cannot perform text wrapping. Therefore
the standard Python module textwrap is used. Setting the constant WIDTH a
text wrap can be performed.

The Base64 graphic is written to the screen and to a file.
"""
# pylint: disable=invalid-name
# pylint: disable=useless-return

# Import the Python module.
import base64
import textwrap

# Set the text width.
WIDTH = 80

# Set the input filename.
FN_IN = "test_logo.png"

# Set the output filename.
FN_OUT = "test_logo.b64"

# ====================
# Function read_file()
# ====================
def read_file(fn):
    """Read an image file.
    @params fn       (str)  : Filename as string
    @return img_data (bytes): Image data as byte string
    """
    # Open a file for reading.
    with open(fn, "rb") as fo:
        # Read the image data from the file.
        img_data = fo.read()
    # Return the image data.
    return img_data

# =====================
# Function write_file()
# =====================
def write_file(fn, b64_strlist):
    """Write an image file.
    @params fn          (str) : Filename as string
            b64_strlist (list): List of strings
    @return None
    """
    # Get the length of the list.
    length = len(b64_strlist)
    # Open a file for writing.
    with open(fn, 'w') as fo:
        # Loop over the number of elements.
        for line in range(length):
            # Get line to write.
            string = "{0}{1}".format(b64_strlist[line], "\n")
            # Write line to file.
            fo.write(string)
    # Return None
    return None

# ====================
# Function print_b64()
# ====================
def print_b64(b64_strlist):
    """Print base64 string to screen.
    @params b64_strlist (list): List of base64 substrings
    @return None
    """
    # Print the formated base64 data to screen.
    length = len(b64_strlist)
    for line in range(length):
        string = b64_strlist[line]
        print(string)
    # Return None
    return None

# ====================
# Main script function
# ====================
def main(fn_in, fn_out):
    """Main script function.
    @params fn_in  (str): Name of png file
            fn_out (str): Name of base64 file
    @return None
    """
    # Read the image data.
    img_data = read_file(fn_in)
    # Create a base64 byte string.
    b64_bytestr = base64.b64encode(img_data)
    # Create a base64 string.
    b64_string = b64_bytestr.decode("utf-8")
    # Perform the text wrap and get a string list.
    b64_strlist = textwrap.wrap(b64_string, width=WIDTH)
    # Print the base64 to screen.
    print_b64(b64_strlist)
    # Write b64 to file.
    write_file(fn_out, b64_strlist)
    # Return None
    return None

# Run script as program or as module.
if __name__ == "__main__":
    # Call the main function.
    main(FN_IN, FN_OUT)
