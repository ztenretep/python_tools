#!/usr/bin/env python3
"""Create a frame arround text.

Unicode in the range of U+2500 to U+257F is used for the border chars.

"""
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-few-public-methods
# pylint: disable=consider-using-enumerate

# Set the constants.
WIDTH = 80
HEIGHT = 8

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

    def __draw_line_text(self, line_count):
        """Private method draw_line()."""
        for count in range(line_count):
            hspc0, _, hspc2 = self.__horizontal_spacing(self.text[count], self.hspan)
            print(self.chars[5] + (' ' * hspc0) + self.text[count] + (' ' * hspc2) + self.chars[5])

    def __draw_top(self):
        """Private method draw_top()."""
        print(self.chars[0] + self.bline + self.chars[1])

    def __draw_down(self):
        """Private method draw_down()."""
        print(self.chars[2] + self.bline + self.chars[3])

    def __draw_mid(self):
        """Private method draw_mid()."""
        vspc0, vspc1, vspc2 = self.__vertical_spacing(self.text, self.vspan)
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
BC = [[u'\u256D', u'\u256E', u'\u2570', u'\u256F', u'\u2500', u'\u2502'],
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
      [u'\u250C', u'\u2510', u'\u2514', u'\u2518', u'\u254C', u'\u254E'],
      ['/', '\\', '\\', '/', '-', '|'],
      ['+', '+', '+', '+', '-', '|'],
      ['*', '*', '*', '*', '*', '*'],
      ['#', '#', '#', '#', '#', '#']]

# Loop over the border strings.
for num in range(0, len(BC)):
    print("{0}{1}".format("Frame style: ", num + 1))
    # Create an instance of DrawBox.
    BORDER = DrawBox(BC[num], TEXT, WIDTH, HEIGHT)
    # Draw box.
    BORDER.draw_box()
