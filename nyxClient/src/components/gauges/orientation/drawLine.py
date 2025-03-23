import math

def draw_line(x, y, angle, length, label=None):
    """
    Draws an SVG line starting from (x, y) at a given angle relative to the Y-axis (YY'),
    with an optional label positioned optimally.

    Args:
        x (float): Starting x-coordinate.
        y (float): Starting y-coordinate.
        angle (float): Angle in degrees from the YY' axis (positive counterclockwise).
        length (float): Length of the line in pixels.
        label (str, optional): Text label for direction. Defaults to None.

    Returns:
        str: SVG line (and optional label) element.
    """
    radians = math.radians(angle)

    # Calculate line end coordinates
    x_end = x + length * math.sin(radians)
    y_end = y - length * math.cos(radians)

    # Construct the line SVG element
    svg_elements = [
        f'<line x1="{x}" y1="{y}" x2="{x_end}" y2="{y_end}" stroke="var(--q-primary)" stroke-width="2"/>'
    ]

    # If a label is provided, calculate its position and alignment
    if label:
        label_offset = 30
        x_label = x + (length + label_offset) * math.sin(radians)
        y_label = y - (length + label_offset) * math.cos(radians)

        # Adjust text alignment based on quadrant
        if 45 < angle < 135:  # Right side (E, NE, SE)
            anchor = "start"
        elif 225 < angle < 315:  # Left side (W, NW, SW)
            anchor = "end"
        else:  # Top and Bottom (N, S)
            anchor = "middle"

        svg_elements.append(
            f'<text x="{x_label}" y="{y_label}" font-size="40" font-weight="bold" '
            f'fill="var(--q-primary)" text-anchor="{anchor}" dominant-baseline="middle">{label}</text>'
        )

    return "\n".join(svg_elements)
