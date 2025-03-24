from nicegui import ui
from .._html_components.component_structure import Container, Header, Content, Footer
from .drawLine import draw_line
import random
import asyncio

# Function to generate the SVG for crosshair
def _draw_Gauge(x_tilt_deg, y_tilt_deg):
    def _draw_Cross():
        return f'''
            <svg stroke-width="2" stroke="var(--q-primary)">
                {draw_line(0, 400, 90, 800)}
                {draw_line(400, 0, 180, 800)}
            </svg>
        '''
    def _draw_x_tilt_indicator(x_tilt_deg):
        return f'''
            <svg stroke="var(--q-primary)" stroke-width="15">
                {draw_line(400, 400, x_tilt_deg +90, 350)}
                {draw_line(400, 400, x_tilt_deg +270, 350)}
            </svg>
        '''
    def _draw_y_tilt_indicator(y_tilt_deg):
        max_angle = 45
        max_displacement = 360
        displacement = min(((y_tilt_deg / max_angle) * max_displacement), max_displacement)
        return f'''
            <svg stroke-width="15" stroke="var(--q-primary)">
                <circle cx="400" cy="400" r="55" fill="var(--q-background)" stroke="var(--q-primary)" stroke-width="10"/>
                <circle cx="400" cy="{400 + displacement}" r="50" fill="var(--q-background)" stroke="none" stroke-width="0"/>
                <circle cx="400" cy="{400 + displacement}" r="35" fill="var(--q-background)" stroke-width="8"/>
                <circle cx="400" cy="{400 - displacement}" r="30" fill="var(--q-background)" stroke="none" stroke-width="0"/>
                <circle cx="400" cy="{400 - displacement}" r="15" fill="var(--q-primary)" stroke-width="7"/>
            </svg>
        '''  
    return f'''
        <svg>
            {_draw_Cross()}
            {_draw_x_tilt_indicator(x_tilt_deg)}
            {_draw_y_tilt_indicator(y_tilt_deg)}
        </svg>
    '''


def draw_mountAlignment():
    with Container():
        Header('vertical_distribute', 'MOUNT ALIGNMENT')
        with Content():
            with ui.row():
                canvas = ui.interactive_image(size=(800, 800)).classes('w-64')
                canvas.set_content(_draw_Gauge(0, 0.0))
            with ui.row().classes('w-full'):
                with ui.column().classes("font-bold"):
                    ui.label("X axis tilt:")
                ui.space()
                with ui.column():
                    x_value = ui.label()
                with ui.column():
                    ui.label("deg")
            with ui.row().classes('w-full'):
                with ui.column().classes("font-bold"):
                    ui.label("Y axis tilt:")
                ui.space()
                with ui.column():
                    y_value = ui.label()
                with ui.column():
                    ui.label("deg")
        with Footer():
            loop_chip = ui.chip('Stream data', selectable=True)
            loop_chip.props('outline square').style("margin: 0; cursor: pointer; padding: 15px 10px; ")
            loop_chip.classes('rounded-lg')
            loop_chip.on_click(lambda: read_magnetometer(loop_chip.selected))

    # Variable to store whether magnetometer reading is active
    magnetometer_active = False

    # Start/stop reading the magnetometer based on the chip's selection state
    async def read_magnetometer(state):
        nonlocal magnetometer_active
        magnetometer_active = state
        while magnetometer_active:
            # Simulate magnetometer readings
            x_tilt = random.uniform(-45, 45)
            y_tilt = random.uniform(-45, 45)

            # Update the UI with new readings
            x_value.set_text(f'{x_tilt:.1f}')
            y_value.set_text(f'{y_tilt:.1f}')
            canvas.set_content(_draw_Gauge(x_tilt, y_tilt))

            # Update every second
            await asyncio.sleep(0.5)