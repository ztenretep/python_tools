#!/usr/bin/python3

fg_col = [30, 31, 32, 33, 34, 35, 36, 37]
bg_col = [40, 41, 42, 43, 44, 45, 46, 47]

STD = "\033[49m"
CSI = "\033["

for i in fg_col:
    for j in bg_col:
        if i != j-10:
            fcol_esc = "{0}{1}{2}".format(CSI, str(i), "m")
            bcol_esc = "{0}{1}{2}".format(CSI, str(j), "m")
            col_esc = "{0}{1}".format(fcol_esc, bcol_esc)
            fcol_str = r"\033[" + str(i) + "m"
            bcol_str = r"\033[" + str(j) + "m"
            print("{0}{1}{2}{3}".format(col_esc, fcol_str, bcol_str, STD))
