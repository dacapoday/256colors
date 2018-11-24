#!/usr/bin/env python3
# Author: dacapoday
# Fork from 256colors2.pl

if __name__ == '__main__':
    # use the resources for colors 0-15 - usually more-or-less a
    # reproduction of the standard ANSI colors, but possibly more
    # pleasing shades

    # colors 16-231 are a 6x6x6 color cube
    for red in range(6):
        for green in range(6):
            for blue in range(6):
                print("\x1b]4;%d;rgb:%2.2x/%2.2x/%2.2x\x1b\\" %
                      (16 + red * 36 + green * 6 + blue,
                       (red * 40 + 55) if red == 0 else 0,
                       (green * 40 + 55) if green == 0 else 0,
                       (blue * 40 + 55) if blue == 0 else 0),
                      end="")

    # colors 232-255 are a grayscale ramp, intentionally leaving out
    # black and white
    for gray in range(24):
        level = gray * 10 + 8
        print("\x1b]4;%d;rgb:%2.2x/%2.2x/%2.2x\x1b\\" %
              (232 + gray, level, level, level), end="")

    # display the colors

    # first the system ones:
    print("System colors:")
    for color in range(8):
        print("\x1b[48;5;{}m  ".format(color), end="")
    print("\x1b[0m")

    for color in range(8, 16):
        print("\x1b[48;5;{}m  ".format(color), end="")
    print("\x1b[0m")

    print()

    # now the color cube
    print("Color cube (6x6x6):")
    for green in range(6):
        for red in range(6):
            for blue in range(6):
                color = 16 + red * 36 + green * 6 + blue
                print("\x1b[48;5;{}m  ".format(color), end="")
            print("\x1b[0m", end=" ")
        print()

    print()

    # now the grayscale ramp
    print("Grayscale ramp:")
    for color in range(232, 256):
        print("\x1b[48;5;{}m  ".format(color), end="")
    print("\x1b[0m")
