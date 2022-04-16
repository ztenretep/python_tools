#!/usr/bin/python3
"""Terminal clear and reset based on ANSI codes.

The so-called ANSI escape sequences can be used to control the terminal
window. ANSI escape sequences can be introduced by ESC (Escape) or CSI
(Control Sequence Introducer).

ESC as well as CSI are followed by a control sequence. ESC is ASCII
character \033 and CSI is ASCII character \033[:

    ESC = \033
    CSI = \033[

There are several possibilities to reset or clear a terminal window.
One common method is as follows:

    import os
    os.system('clear')
    os.system('reset')

Usage of clear() and reset():

    import term_ctrl
    term_ctrl.clear()
    term_ctrl.reset()

or

    from term_ctrl import clear
    from term_ctrl import reset
    clear()
    reset()
"""
# pylint: disable=useless-return

# Import the standard Python module.
import sys

# Set some constants.
NL = "\n"
CR = "\r"

# =============================
# User defined function reset()
# =============================
def reset():
    """Reset terminal window."""
    # Write ANSI code to terminal.
    sys.stdout.write("\033c")
    # Write buffer to screen immediately.
    sys.stdout.flush()
    # Return None.
    return None

# =============================
# User defined function clear()
# =============================
def clear():
    """Clear terminal window."""
    # Write ANSI code to terminal.
    sys.stdout.write("\033[H\033[J")
    # Write buffer to screen immediately.
    sys.stdout.flush()
    # Return None.
    return None
