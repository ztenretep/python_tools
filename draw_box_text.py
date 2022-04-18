#!/usr/bin/env python3
"""Create a frame arround text."""
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-few-public-methods

# Set the constants.
WIDTH = 80
HEIGHT = 10

# Set the text list.
TEXT = ["This is a text,", "printed for demonstration purposes,",
        "inside a frame, which is", "defined by a set of characters."]

# ===============
# Class DrawBox()
# ===============
class DrawBox:
    """Class __init__ function."""
    def __init__(self, box_chars, box_text, box_width, box_height):
        self.chars = box_chars
        self.text = box_text
        self.width = box_width
        self.height = box_height
        self.hspan = self.width - 2
        self.vspan = self.height - 2
        self.bline = self.chars[4] * self.hspan
        self.hspace = ' ' * self.hspan

    @staticmethod
    def __vertical_spacing(text, vspan):
        """Private static method __vertical_spacing()."""
        vspc1 = len(text)
        tmp = vspan - vspc1
        vspc0 = int(tmp/2)
        vspc2 = int(tmp - vspc0)
        return vspc0, vspc1, vspc2

    @staticmethod
    def __horizontal_spacing(text, hspan):
        """Private static method __horizontal_spacing()."""
        hspc1 = len(text)
        tmp = hspan - hspc1
        hspc0 = int(tmp/2)
        hspc2 = int(tmp - hspc0)
        return hspc0, hspc1, hspc2

    def __draw_line_space(self, count):
        """Private method draw_line()."""
        for _ in range(count):
            print(self.chars[5] + self.hspace + self.chars[5])
        return 0

    def __draw_line_text(self, line_count):
        """Private method draw_line()."""
        for count in range(line_count):
            hspc0, _, hspc2 = self.__horizontal_spacing(self.text[count], self.hspan)
            print(self.chars[5] + (' ' * hspc0) + self.text[count] + (' ' * hspc2) + self.chars[5])
        return 0

    def __draw_top(self):
        """Private method draw_top()."""
        print(self.chars[0] + self.bline + self.chars[1])
        return 0

    def __draw_down(self):
        """Private method draw_down()."""
        print(self.chars[2] + self.bline + self.chars[3])
        return 0

    def __draw_mid(self):
        """Private method draw_mid()."""
        vspc0, vspc1, vspc2 = self.__vertical_spacing(self.text, self.vspan)
        self.__draw_line_space(vspc0)
        self.__draw_line_text(vspc1)
        self.__draw_line_space(vspc2)
        return 0

    def draw_box(self):
        """Method draw_box()."""
        self.__draw_top()
        self.__draw_mid()
        self.__draw_down()
        return 0

# Set the border char lists.
# BC = [TOPLEFT, TOPRIGHT, DOWNLEFT, DOWNLEFT, HORIZONTAL, VERTICAL]
BC0 = [u'\u250F', u'\u2513', u'\u2517', u'\u251B', u'\u2501', u'\u2503']
BC1 = [u'\u250c', u'\u2510', u'\u2514', u'\u2518', u'\u2500', u'\u2502']
BC2 = [u'\u2554', u'\u2557', u'\u255A', u'\u255D', u'\u2550', u'\u2551']

# Create an instance of DrawBox.
#BORDER = DrawBox(BC1, TEXT, WIDTH, HEIGHT)
BORDER = DrawBox(BC0, TEXT, WIDTH, HEIGHT)

# Draw box.
BORDER.draw_box()
