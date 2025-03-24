from nicegui import ui
from .._html_components.component_structure import Container, Header, Content, Footer
from .drawLine import draw_line
import random
import asyncio

# Function to render the leveling gauge SVG
def _render_leveling_gauge(x_tilt_deg, y_tilt_deg):
    def _render_axis():
        return f'''
            <svg stroke-width="2" stroke="var(--q-primary)">
                {draw_line(0, 400, 90, 800)}  <!-- Vertical line -->
                {draw_line(400, 0, 180, 800)} <!-- Horizontal line -->
            </svg>
        '''
    
    def _render_x_tilt_indicator(x_tilt_angle):
        return f'''
            <svg stroke="var(--q-primary)" stroke-width="15">
                {draw_line(400, 400, x_tilt_angle + 90, 350)}   <!-- Top indicator -->
                {draw_line(400, 400, x_tilt_angle + 270, 350)}  <!-- Bottom indicator -->
            </svg>
        '''
    
    def _render_y_tilt_indicator(y_tilt_angle):
        max_angle = 45
        max_displacement = 360
        displacement = min(((y_tilt_angle / max_angle) * max_displacement), max_displacement)
        return f'''
            <svg>
                <circle cx="400" cy="400" r="55" fill="var(--q-background)" stroke="var(--q-primary)" stroke-width="10"/>
            </svg>
            <svg>
                <circle cx="400" cy="{400 + displacement}" r="50" fill="var(--q-background)" stroke="none" stroke-width="0"/>
                <circle cx="400" cy="{400 + displacement}" r="35" fill="var(--q-background)" stroke="var(--q-primary)" stroke-width="8"/>
            </svg>
            <svg>
                <circle cx="400" cy="{400 - displacement}" r="30" fill="var(--q-background)" stroke-width="0"/>
                <circle cx="400" cy="{400 - displacement}" r="15" fill="var(--q-primary)" stroke="var(--q-primary)" stroke-width="7"/>
            </svg>
        '''  
    return f'''
        <svg>
            {_render_axis()}
            {_render_x_tilt_indicator(x_tilt_deg)}
            {_render_y_tilt_indicator(y_tilt_deg)}
        </svg>
    '''


def mount_leveling_ui():
    with Container():
        Header('vertical_distribute', 'MOUNT LEVELING')
        with Content():
            with ui.row():
                gauge_display = ui.interactive_image(size=(800, 800)).classes('w-64')
                gauge_display.set_content(_render_leveling_gauge(0, 0.0))
            with ui.row().classes('w-full'):
                with ui.column().classes("font-bold"):
                    ui.label("X axis tilt:")
                ui.space()
                with ui.column():
                    x_tilt_label = ui.label()
                with ui.column():
                    ui.label("deg")
            with ui.row().classes('w-full'):
                with ui.column().classes("font-bold"):
                    ui.label("Y axis tilt:")
                ui.space()
                with ui.column():
                    y_tilt_label = ui.label()
                with ui.column():
                    ui.label("deg")
        with Footer():
            stream_data_toggle = ui.chip('Stream data', selectable=True)
            stream_data_toggle.props('outline square').style("margin: 0; cursor: pointer; padding: 15px 10px; ")
            stream_data_toggle.classes('rounded-lg')
            stream_data_toggle.on_click(lambda: stream_magnetometer_data(stream_data_toggle.selected))

    # Variable to store whether magnetometer reading is active
    magnetometer_stream_active = False

    # Start/stop reading the magnetometer based on the chip's selection state
    async def stream_magnetometer_data(state):
        nonlocal magnetometer_stream_active
        magnetometer_stream_active = state
        while magnetometer_stream_active:
            # Simulate magnetometer readings
            x_tilt_angle = random.uniform(-45, 45)
            y_tilt_angle = random.uniform(-45, 45)

            # Update the UI with new readings
            x_tilt_label.set_text(f'{x_tilt_angle:.1f}')
            y_tilt_label.set_text(f'{y_tilt_angle:.1f}')
            gauge_display.set_content(_render_leveling_gauge(x_tilt_angle, y_tilt_angle))

            # Update every half second
            await asyncio.sleep(0.5)
