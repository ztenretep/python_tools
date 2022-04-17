#!/usr/bin/env python
"""Create frame arround Text."""

# Set the constants.
WIDTH = 80
HEIGHT = 10

# Set the text list.
TEXT = ["First line", "Second line with text", "Third line also with text", "Last line"]

# =======================
# Class TableBorderChar()
# =======================
class DrawBox:
    """Class __init__ function."""
    # pylint: disable=too-many-instance-attributes
    def __init__(self, box_chars, box_text, box_width, box_height):
        self.chars = box_chars
        self.text = box_text
        self.width = box_width
        self.height = box_height
        self.hspan = self.width - 2
        self.line = self.chars[4] * self.hspan

    def vlen(self):
        """Method vlen()."""
        vspan = self.height - 2
        vspc0 = len(self.text)
        temp = vspan - vspc0
        vspc1 = int(temp/2)
        vspc2 = temp - vspc1
        return vspc0, vspc1, vspc2

    def draw_top(self):
        """Method draw_top()."""
        print(self.chars[0] + self.line + self.chars[1])
        return 0

    def draw_down(self):
        """Method draw_down()."""
        print(self.chars[2] + self.line + self.chars[3])
        return 0

    def draw_mid(self, text):
        """Method draw_mid()."""
        hspan = self.width - 2
        hspc0 = len(text)
        temp = hspan - hspc0
        hspc1 = int(temp/2)
        hspc2 = temp - hspc1
        print(self.chars[5] + (' ' * hspc1) + text + (' ' * hspc2) + self.chars[5])
        return 0

    def draw_box(self):
        """Method draw_box()."""
        vspc0, vspc1, vspc2 = self.vlen()
        self.draw_top()
        for _ in range(vspc1 - 1):
            self.draw_mid('')
        for i in range(vspc0):
            self.draw_mid(self.text[i])
        for _ in range(vspc2 - 1):
            self.draw_mid('')
        self.draw_down()
        return 0

# ===================
# Function draw_box()
# ===================
def draw_box(box):
    """Draw box."""
    box.draw_box()

# Set the border char lists.
# TL, TR, DL, DR, H, V
BC1 = [u'\u250c', u'\u2510', u'\u2514', u'\u2518', u'\u2500', u'\u2502']
BC2 = [u'\u2554', u'\u2557', u'\u255A', u'\u255D', u'\u2550', u'\u2551']

# Create an instance of DrawBox.
BORDER = DrawBox(BC1, TEXT, WIDTH, HEIGHT)
#BORDER = DrawBox(BC2, TEXT, WIDTH, HEIGHT)

# Draw box.
draw_box(BORDER)
