from nicegui import ui
from .._html_components.component_structure import Container, Header, Content, Footer
import random
import asyncio
import math

def draw_horAlignment():

    with Container("280px"):

        Header('vertical_distribute', 'HOR ALIGNMENT')

        with Content():
            compass = ui.interactive_image(size=(800, 800)).classes('w-64 rounded-2xl').style('border: none; background-color: transparent; padding: 15px')
            compass.set_content(_draw_crosshair(0, 0))

            with ui.row().style('width: 100%; justify-content: left; display: grid; grid-template-columns: 1fr 1fr;'):
                with ui.row():
                    ui.label("x :")
                    x_value = ui.label()
                    ui.label("deg")
                with ui.row():
                    ui.label("y :")
                    y_value = ui.label()
                    ui.label("deg")

        with Footer():
            loop_chip = ui.chip('Activate magnetometer', selectable=True)
            loop_chip.props('outline square').style("margin: 0; cursor: pointer; padding: 15px 10px; ")
            loop_chip.classes('rounded-lg')
            loop_chip.on_click(lambda: toggle_magnetometer(loop_chip.selected))

    # Variable to store whether magnetometer reading is active
    magnetometer_active = False

    # Event handler for chip selection toggle
    def toggle_magnetometer(state):
        nonlocal magnetometer_active
        magnetometer_active = state

    # Start/stop reading the magnetometer based on the chip's selection state
    async def read_magnetometer():
        nonlocal magnetometer_active
        while True:
            if magnetometer_active:
                # Simulate magnetometer readings
                x_tilt = random.uniform(-15, 15)
                y_tilt = random.uniform(-15, 15)

                # Update the UI with new readings
                x_value.set_text(f'{x_tilt:.1f}')
                y_value.set_text(f'{y_tilt:.1f}')
                compass.set_content(_draw_crosshair(x_tilt, y_tilt))
            await asyncio.sleep(0.5)  # Update every second

    # Start the magnetometer reading loop
    ui.timer(0.5, read_magnetometer)

# Function to generate the SVG for crosshair
def _draw_crosshair(x_tilt, y_tilt):
    
    def _draw_center():
        return f'<circle cx="400" cy="400" r="50" fill="none" stroke="var(--q-primary)" stroke-width="10"/>'
    
    def _draw_cross():
        return '''
            <line x1="20" y1="400" x2="780" y2="400" stroke-width="2"/>
            <line x1="400" y1="20" x2="400" y2="780" stroke-width="2"/>
        '''

    def _draw_line_xx(x_angle):
        # Convert the angle to radians
        x_angle_rad = math.radians(x_angle)

        # Length of the line (fixed to 400px)
        length = 400

        # Calculate the end coordinates of the line using trigonometry
        x_start = 400 - length * math.cos(x_angle_rad)
        y_start = 400 + length * math.sin(x_angle_rad) 
        x_end = 400 + length * math.cos(x_angle_rad)
        y_end = 400 - length * math.sin(x_angle_rad) 

        # Return the line SVG element
        return (f'<line x1="{x_start}" y1="{y_start}" x2="{x_end}" y2="{y_end}" stroke-width="15" stroke="var(--q-primary)"/>')
    
    def _draw_line_yy(x_angle, y_angle):
        # Convert the angle to radians
        x_angle_rad = math.radians(x_angle + 90)
        x_angle_rad_minus = math.radians(x_angle - 90)
        y_angle_rad = math.radians(y_angle)

        # Scale y_angle to determine length (400px at 10°, 0px at 0°)
        max_angle = 10
        if (y_angle > max_angle): length = 400
        else: length = (y_angle / max_angle) * 400
        

        # Calculate the end coordinates of the line using trigonometry
        x_start = 400 - length * math.cos(x_angle_rad_minus)
        y_start = 400 + length * math.sin(x_angle_rad_minus) 
        x_end = 400 - length * math.cos(x_angle_rad)
        y_end = 400 + length * math.sin(x_angle_rad)

        # Return the line SVG element
        return (f'''
                    <line x1="{x_start}" y1="{y_start}" x2="{x_end}" y2="{y_end}" stroke-width="10" stroke="var(--q-primary)"/>
                    <circle cx="400" cy="400" r={abs(length)} fill="none" stroke="var(--q-primary)" stroke-width="1"/>
                ''')




    return f'''
        <svg width="800" height="800" style="stroke: var(--q-primary);">
            {_draw_center()}
            {_draw_cross()}
            {_draw_line_xx(x_tilt)}
            {_draw_line_yy(x_tilt, y_tilt)}
        </svg>
    '''
