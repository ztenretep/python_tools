#!/usr/bin/env python3
"""Create a frame arround text.

Unicode in the range of U+2500 to U+257F is used for the border chars.

"""
# pylint: disable=consider-using-enumerate
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-format-args
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name

# Import Python module.
import sys

# Set the constants.
WIDTH = 80
HEIGHT = 8

# Set the text list.
TEXT = ["This is a text,", "printed for demonstration purposes,",
        "inside a frame, which is", "defined by a set of characters."]

# Set color sequences.
STD = "\033[49m"
COL0 = "\033[37m\033[40m"
COL1 = "\033[37m\033[41m"
COL2 = "\033[37m\033[42m"
COL3 = "\033[37m\033[43m"
COL4 = "\033[37m\033[44m"
COL5 = "\033[37m\033[45m"
COL6 = "\033[37m\033[46m"
COL7 = "\033[37m\037[46m"

# =============================
# User defined function reset()
# =============================
def reset():
    """Reset terminal window."""
    # Write ANSI code to terminal.
    sys.stdout.write("\033c")
    # Write buffer to screen immediately.
    sys.stdout.flush()

# ===============
# Class DrawBox()
# ===============
class DrawBox:
    """Class __init__ function."""
    spc = u"\u0020"
    std = "\033[49m"
    col = "\033[37m\033[40m"
    align = "center"

    def __init__(self, chars, text, width, height,
                 align=None, col=None):
        self.chars = chars
        self.text = text
        self.width = width
        self.height = height
        self.hspan = self.width - 2
        self.vspan = self.height - 2
        self.bline = self.chars[4] * self.hspan
        self.hspace = self.spc * self.hspan
        self.align = align if align is not None else self.align
        self.col = col if col is not None else self.col

    @staticmethod
    def __spacing(text, span):
        """Private static method __spacing()."""
        spc1 = len(text)
        tmp = span - spc1
        spc0 = int(tmp/2)
        spc2 = int(tmp - spc0)
        return spc0, spc1, spc2

    def __draw_line_space(self, count):
        """Private method draw_line()."""
        for _ in range(count):
            fmt_str = "{0}{2}{3}{2}{1}".format(self.col, self.std,
                                               self.chars[5], self.hspace)
            print(fmt_str)

    def __draw_line_text(self, line_count):
        """Private method draw_line()."""
        for count in range(line_count):
            hspc0, _, hspc2 = self.__spacing(self.text[count], self.hspan)
            lspc0 = self.spc * hspc0
            lspc2 = self.spc * hspc2
            if self.align == "center":
                istr = "{0}{2}{1}".format(lspc0, lspc2, self.text[count])
            elif self.align == "left":
                istr = "{2}{0}{1}".format(lspc0, lspc2, self.text[count])
            elif self.align == "right":
                istr = "{0}{1}{2}".format(lspc0, lspc2, self.text[count])
            fmt_str = "{0}{2}{3}{2}{1}".format(self.col, self.std,
                                               self.chars[5], istr)
            print(fmt_str)

    def __draw_top(self):
        """Private method draw_top()."""
        fmt_str = "{0}{2}{4}{3}{1}".format(self.col, self.std, self.chars[0],
                                           self.chars[1], self.bline)
        print(fmt_str)

    def __draw_down(self):
        """Private method draw_down()."""
        fmt_str = "{0}{2}{4}{3}{1}".format(self.col, self.std, self.chars[2],
                                           self.chars[3], self.bline)
        print(fmt_str)

    def __draw_mid(self):
        """Private method draw_mid()."""
        vspc0, vspc1, vspc2 = self.__spacing(self.text, self.vspan)
        self.__draw_line_space(vspc0)
        self.__draw_line_text(vspc1)
        self.__draw_line_space(vspc2)

    def draw_box(self):
        """Method draw_box()."""
        self.__draw_top()
        self.__draw_mid()
        self.__draw_down()

# Set the border char lists.
# [TOPLEFT, TOPRIGHT, DOWNLEFT, DOWNLEFT, HORIZONTAL, VERTICAL]
BC_UNI = [[u'\u256D', u'\u256E', u'\u2570', u'\u256F', u'\u2500', u'\u2502'],
          [u'\u250c', u'\u2510', u'\u2514', u'\u2518', u'\u2500', u'\u2502'],
          [u'\u2554', u'\u2557', u'\u255A', u'\u255D', u'\u2550', u'\u2551'],
          [u'\u2552', u'\u2555', u'\u2558', u'\u255B', u'\u2550', u'\u2502'],
          [u'\u2553', u'\u2556', u'\u2559', u'\u255C', u'\u2500', u'\u2551'],
          [u'\u250F', u'\u2513', u'\u2517', u'\u251B', u'\u2501', u'\u2503'],
          [u'\u250D', u'\u2511', u'\u2515', u'\u2519', u'\u2501', u'\u2502'],
          [u'\u250E', u'\u2512', u'\u2516', u'\u251A', u'\u2500', u'\u2503'],
          [u'\u250F', u'\u2513', u'\u2517', u'\u251B', u'\u2505', u'\u2507'],
          [u'\u250F', u'\u2513', u'\u2517', u'\u251B', u'\u254D', u'\u254F'],
          [u'\u250F', u'\u2513', u'\u2517', u'\u251B', u'\u2509', u'\u250B'],
          [u'\u250C', u'\u2510', u'\u2514', u'\u2518', u'\u2504', u'\u2506'],
          [u'\u250C', u'\u2510', u'\u2514', u'\u2518', u'\u2508', u'\u250A'],
          [u'\u250C', u'\u2510', u'\u2514', u'\u2518', u'\u254C', u'\u254E']]
BC_ASCII = [['/', '\\', '\\', '/', '-', '|'],
            ['+', '+', '+', '+', '-', '|'],
            ['*', '*', '*', '*', '*', '*'],
            ['#', '#', '#', '#', '#', '#']]

# *************
# Main function
# *************
def main():
    """Main script function."""
    # Reset terminal window.
    reset()
    # Loop over the border strings.
    for num in range(0, len(BC_UNI)):
        print("{0}{1}".format("Frame style: ", num + 1))
        # Create an instance of DrawBox.
        BORDER = DrawBox(BC_UNI[num], TEXT, WIDTH, HEIGHT, align=None, col=COL5)
        # Draw box.
        BORDER.draw_box()
    # Loop over the border strings.
    for num in range(0, len(BC_ASCII)):
        print("{0}{1}".format("Frame style: ", num + 1))
        # Create an instance of DrawBox.
        BORDER = DrawBox(BC_ASCII[num], TEXT, WIDTH, HEIGHT, align=None, col=COL4)
        # Draw box.
        BORDER.draw_box()

# Execute script as program or as module.
if __name__ == "__main__":
    # Call main function.
    main()
