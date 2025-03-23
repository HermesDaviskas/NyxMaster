import math

def draw_line(x, y, angle, length):
    """
    Draws an SVG line starting from (x, y) at a given angle relative to the Y-axis (YY').
    
    Args:
        x (float): Starting x-coordinate.
        y (float): Starting y-coordinate.
        angle (float): Angle in degrees from the YY' axis (positive counterclockwise).
        length (float): Length of the line in pixels.
    
    Returns:
        str: SVG line element.
    """
    # Convert angle from degrees to radians
    radians = math.radians(angle)

    # Calculate the end point using trigonometry
    x_end = x + length * math.sin(radians)  # sin() for X because angle is from Y-axis
    y_end = y - length * math.cos(radians)  # cos() for Y (negative because SVG Y increases downward)

    # Return the SVG line element
    return f'<line x1="{x}" y1="{y}" x2="{x_end}" y2="{y_end}" stroke="black" stroke-width="2"/>'

# Example Usage:
svg_code = f'''
<svg width="800" height="800">
    {draw_line(400, 400, 30, 100)}  <!-- Line at 30° from the YY' axis -->
    {draw_line(400, 400, -45, 150)} <!-- Line at -45° (clockwise) -->
</svg>
'''

print(svg_code)
