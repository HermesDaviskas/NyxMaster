from nicegui import ui

# Function to draw concentric circles
def draw_compass():
    # Create the interactive image with the compass drawing
    compass = ui.interactive_image(size=(800, 800))
    compass.classes('w-64 rounded-2xl')
    compass.style('border: solid; border-width: 1px; border-color: var(--q-primary); background-color: transparent; padding: 15px')
    compass.set_content(_draw_crosshair(3))
    

# Function to generate the complete SVG content with circles and cross
def _draw_crosshair(number_of_circles):
    svg_content = f'<svg width="800" height="800" style="stroke: var(--q-primary);"> {_draw_circles(number_of_circles)} {_draw_cross()} </svg>'
    return svg_content


# Function to generate the concentric circles
def _draw_circles(number_of_circles):
    inner_radius = 100
    outer_radius = 350
    crosshair_width = 3

    concentric_circles: str = ""
    # Calculate the radius increment step based on the number of circles
    radius_inc_step = round((outer_radius - inner_radius) / (number_of_circles - 1))
    for radius in range(inner_radius, outer_radius + radius_inc_step, radius_inc_step):
        concentric_circles += f'<circle cx="400" cy="400" r="{radius}" stroke-width="{crosshair_width}" fill="none"/>'

    return concentric_circles


# Function to generate horizontal and vertical lines
def _draw_cross():
    line_width = 2

    horizontal_line = f'<line x1="20" y1="400" x2="780" y2="400" stroke-width="{line_width}"/>'
    vertical_line = f'<line x1="400" y1="20" x2="400" y2="780" stroke-width="{line_width}"/>'

    cross = f'{horizontal_line} {vertical_line}'

    return cross


ui.run()
