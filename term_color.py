  GNU nano 4.8                                                                 term_color.py                                                                             
#!/usr/bin/python3
"""Terminal color demo."""

# Import the standard Python module.
import sys

# Set the array with foreground and background colors.
FG_COL = [30, 31, 32, 33, 34, 35, 36, 37]
BG_COL = [40, 41, 42, 43, 44, 45, 46, 47]

# Set ANSI constants.
STD = "\033[49m"
CSI = "\033["

# Loop over the color combinations.
for fg in FG_COL:
    for bg in BG_COL:
        # Print escape code to screen if fg and bg different.
        if fg != bg-10:
            fgcol_str = "{0}{1}{2}".format(r"\033[", str(fg), "m")
            bgcol_str = "{0}{1}{2}".format(r"\033[", str(bg), "m")
            fgcol_esc_seq = "{0}{1}{2}".format(CSI, str(fg), "m")
            bgcol_esc_seq = "{0}{1}{2}".format(CSI, str(bg), "m")
            col_esc_seq = "{0}{1}".format(fgcol_esc_seq, bgcol_esc_seq)
            fmt_str = "{0}{1}{2}{3}".format(col_esc_seq, fgcol_str, bgcol_str, STD)
            sys.stdout.write(fmt_str)
    # Print line break.
    sys.stdout.write("\n")
