#!/usr/bin/env python
"""Create frame arround Text."""
# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

# Set the constants.
WIDTH = 80
HEIGHT = 3

# =======================
# Class TableBorderChar()
# =======================
class DrawBox:
    """Class __init__ function."""
    # pylint: disable=too-many-instance-attributes
    def __init__(self, borderchar, width, height):
        self.borderchar = borderchar
        self.top_left = borderchar[0]
        self.top_right = borderchar[1]
        self.mid_left = borderchar[2]
        self.mid_right = borderchar[3]
        self.down_left = borderchar[4]
        self.down_right = borderchar[5]
        self.horizontal = borderchar[6]
        self.vertical = borderchar[7]
        self.width = width
        self.height = height

    def draw_top(self):
        """Method draw_top()."""
        span = self.width-2
        line = self.horizontal * span
        print(self.top_left + line + self.top_right)
        return 0

    def draw_mid(self):
        """Method draw_mid()."""
        span = self.width-2
        body = self.vertical + (' ' * span) + self.vertical
        for _ in range(self.height - 1):
            print(body)
        return 0

    def draw_down(self):
        """Method draw_down()."""
        span = self.width-2
        line = self.horizontal * span
        print(self.down_left + line + self.down_right)
        return 0

# ===================
# Function draw_box()
# ===================
def draw_box(box):
    """Draw box."""
    box.draw_top()
    box.draw_mid()
    box.draw_down()

# Set the border char lists.
BC1 = [u'\u250c', u'\u2510', u'\u251C', u'\u2524', u'\u2514', u'\u2518', u'\u2500', u'\u2502']
BC2 = [u'\u250c', u'\u2510', u'\u251C', u'\u2524', u'\u2514', u'\u2518', u'\u2500', u'\u2502']

# Create an instance of DrawBox.
BORDER = DrawBox(BC1, WIDTH, HEIGHT)

# Draw box.
draw_box(BORDER)
