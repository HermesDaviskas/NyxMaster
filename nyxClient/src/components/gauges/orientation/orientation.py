from nicegui import ui
from .._html_components.component_structure import Container, Header, Content, Footer
import random
import asyncio

def draw_horAlignment():

    with Container("280px"):

        Header('vertical_distribute', 'HOR ALIGNMENT')

        with Content():
            compass = ui.interactive_image(size=(800, 800)).classes('w-64 rounded-2xl').style('border: none; background-color: transparent; padding: 15px')
            compass.set_content(_draw_crosshair(3, 0, 0))

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
                x_tilt = random.uniform(-90, 90)
                y_tilt = random.uniform(-90, 90)

                # Update the UI with new readings
                x_value.set_text(f'{x_tilt:.1f}')
                y_value.set_text(f'{y_tilt:.1f}')
                compass.set_content(_draw_crosshair(3, x_tilt *4, y_tilt *4))
            await asyncio.sleep(0.5)  # Update every second

    # Start the magnetometer reading loop
    ui.timer(0.5, read_magnetometer)

# Function to generate the SVG for crosshair
def _draw_crosshair(number_of_circles, x_offset, y_offset):

    def _draw_circles():
        inner_radius, outer_radius, crosshair_width = 100, 350, 3
        radius_inc_step = (outer_radius - inner_radius) // (number_of_circles - 1)
        return ''.join(f'<circle cx="400" cy="400" r="{r}" stroke-width="{crosshair_width}" fill="none"/>'
                       for r in range(inner_radius, outer_radius + radius_inc_step, radius_inc_step))

    def _draw_cross():
        return '''
            <line x1="20" y1="400" x2="780" y2="400" stroke-width="2"/>
            <line x1="400" y1="20" x2="400" y2="780" stroke-width="2"/>
        '''

    def _draw_indicator():
        return f'<circle cx="{400 + x_offset}" cy="{400 - y_offset}" r="35" fill="var(--q-primary)"/>'

    return f'''
        <svg width="800" height="800" style="stroke: var(--q-primary);">
            {_draw_circles()}
            {_draw_cross()}
            {_draw_indicator()}
        </svg>
    '''
