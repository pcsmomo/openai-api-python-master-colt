import argparse
import sys
from collections import namedtuple
from typing import List

import colorsys

ColorRGB = namedtuple("ColorRGB", ["r", "g", "b"])
ColorHSV = namedtuple("ColorHSV", ["h", "s", "v"])


def lerp(a: float, b: float, t: float) -> float:
    """
    Linearly interpolate between two values, a and b, based on a factor t.
    Args:
        a: The first value.
        b: The second value.
        t: A factor between 0 and 1, indicating the interpolation position between a and b.
    Returns:
        The interpolated value between a and b.
    """
    if not 0.0 <= t <= 1.0:
        raise ValueError("t must be between 0.0 and 1.0")
    return a + (b - a) * t


def rgb_to_hsv(color: ColorRGB) -> ColorHSV:
    """
    Convert a color from the RGB to the HSV color space.
    Args:
        color: A ColorRGB object representing the RGB color.
    Returns:
        A ColorHSV object containing the converted HSV color.
    """
    h, s, v = colorsys.rgb_to_hsv(
        color.r / 255.0, color.g / 255.0, color.b / 255.0)
    return ColorHSV(h, s, v)


def hsv_to_rgb(color: ColorHSV) -> ColorRGB:
    """
    Convert a color from the HSV to the RGB color space.
    Args:
        color: A ColorHSV object representing the HSV color.
    Returns:
        A ColorRGB object containing the converted RGB color.
    """
    r, g, b = colorsys.hsv_to_rgb(color.h, color.s, color.v)
    return ColorRGB(int(r * 255), int(g * 255), int(b * 255))


def gradient_between_colors(color1: ColorRGB, color2: ColorRGB, steps: int) -> List[ColorRGB]:
    """
    Generate a gradient between two RGB colors using the HSV color space.
    Args:
        color1: The first RGB color as a ColorRGB object.
        color2: The second RGB color as a ColorRGB object.
        steps: The number of steps in the gradient.
    Returns:
        A list of ColorRGB objects representing the gradient between the two colors.
    """
    color_gradient = []
    hsv1 = rgb_to_hsv(color1)
    hsv2 = rgb_to_hsv(color2)

    for step in range(steps + 1):
        t = step / steps
        h = lerp(hsv1.h, hsv2.h, t)
        s = lerp(hsv1.s, hsv2.s, t)
        v = lerp(hsv1.v, hsv2.v, t)
        color_gradient.append(hsv_to_rgb(ColorHSV(h, s, v)))

    return color_gradient


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments using argparse.
    Returns:
        A namespace object containing the command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Generate a gradient between two RGB colors")
    parser.add_argument(
        "color1", type=str, help='First RGB color in the format "R,G,B" (e.g. "255,0,0")')
    parser.add_argument(
        "color2", type=str, help='Second RGB color in the format "R,G,B" (e.g. "0,0,255")')
    parser.add_argument("-n", type=int, default=10,
                        help="Number of gradient steps (default: 10)")

    return parser.parse_args()


def main() -> int:
    """
    Main function to parse command-line arguments and generate the gradient.
    Returns:
        An exit code indicating success or failure.
    """

    args = parse_args()

    def parse_color_string(color_string: str) -> ColorRGB:
        """
        Parse a color string in the format "R,G,B" and return a ColorRGB object.
        Args:
            color_string: A string representing an RGB color in the format "R,G,B".
        Returns:
            A ColorRGB object containing the parsed RGB color.
        """
        try:
            return ColorRGB(*map(int, color_string.split(",")))
        except ValueError as e:
            raise ValueError(
                f"Invalid color string: {color_string}. Expected format: 'R,G,B'") from e

    try:
        color1 = parse_color_string(args.color1)
        color2 = parse_color_string(args.color2)
    except ValueError as e:
        print(e)
        return 1

    try:
        color_gradient = gradient_between_colors(color1, color2, args.n)
    except Exception as e:
        print(e)
        return 1

    for color in color_gradient:
        print(color)

    return 0


if __name__ == "__main__":
    sys.exit(main())
