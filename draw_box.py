#!/usr/bin/env python3
"""Draw box."""
# pylint: disable=too-many-instance-attributes

# Set width and height.
WIDTH = 80
HEIGHT = 20

# ===============
# Class DrawBox()
# ===============
class DrawBox:
    """Class __init__ function."""
    def __init__(self, border_chars, box_width, box_height):
        self.chars = border_chars
        self.width = box_width
        self.height = box_height
        self.span = self.width-2
        self.hspace = ' ' * self.span
        self.bline = self.chars[4] * self.span
        self.hline = self.chars[5] + self.hspace + self.chars[5]

    def draw_top(self):
        """Class method draw_top()."""
        print(self.chars[0] + self.bline + self.chars[1])
        return 0

    def draw_down(self):
        """Class method draw_down()."""
        print(self.chars[2] + self.bline + self.chars[3])
        return 0

    def draw_mid(self):
        """Class method draw_mid()."""
        for _ in range(self.height - 2):
            print(self.hline)
        return 0

    def draw_box(self):
        """Class method draw_box()."""
        self.draw_top()
        self.draw_mid()
        self.draw_down()
        return 0

# Define the border char lists with unicode characters. 
# BC = [TOPLEFT, TOPRIGHT, DOWNLEFT, DOWNRIGHT, HORIZONTAL, VERTICAL]
BC1 = [u'\u250c', u'\u2510', u'\u2514', u'\u2518', u'\u2500', u'\u2502']
BC2 = [u'\u2554', u'\u2557', u'\u255A', u'\u255D', u'\u2550', u'\u2551']

# Create an instance of DrawBox.
BOX = DrawBox(BC1, WIDTH, HEIGHT)

# Draw box.
BOX.draw_box()
