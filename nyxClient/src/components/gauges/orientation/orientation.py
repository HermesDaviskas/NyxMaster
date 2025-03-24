from nicegui import ui
from .._html_components.component_structure import *
from .drawLine import draw_line

import random
import asyncio

def _drawHeading(mount_offset_deg, heading_deg):
    def _draw_cross():
        line_lth = 660
        return f'''
            {draw_line(400, 400, 0 +mount_offset_deg, line_lth /2, "N")}
            {draw_line(400, 400, 90 +mount_offset_deg, line_lth /2, "E")}
            {draw_line(400, 400, 180 +mount_offset_deg, line_lth /2, "S")}
            {draw_line(400, 400, 270 +mount_offset_deg, line_lth /2, "W")}
            {draw_line(400, 400, 45 +mount_offset_deg, line_lth /2, "NE")}
            {draw_line(400, 400, 135 +mount_offset_deg, line_lth /2, "SE")}
            {draw_line(400, 400, 225 +mount_offset_deg, line_lth /2, "SW")}
            {draw_line(400, 400, 315 +mount_offset_deg, line_lth /2, "NW")}
            <circle cx="400" cy="400" r="{line_lth/2 -40}" stroke="var(--q-primary)" fill="none"/>
            <circle cx="400" cy="400" r="190" fill="var(--q-background)" stroke="var(--q-primary)" stroke-width="2"/>
        '''
    def _draw_indicator(heading_deg):
        return f'''
            <circle cx="400" cy="400" r="20" fill="var(--q-background)" stroke="var(--q-primary)" stroke-width="8"/>
            <g transform="rotate({heading_deg}, 400, 400)"> <polygon points="400, 250, 350, 350, 450, 350" fill="var(--q-primary)"/></g>
        '''
    return f'''
        <svg>
            {_draw_cross()}
            {_draw_indicator(heading_deg)}
        </svg>
    '''

def _drawAltitude(alt_deg):
    def _draw_cross():
        line_lth = 660
        altitude_labels = range(0, 100, 10)
        lines = "\n".join(f'{draw_line(750, 750, angle -90, line_lth, str(angle))}' for angle in altitude_labels)
        return f'''
            {lines}
            <circle cx="750" cy="750" r="{line_lth -40}" stroke="var(--q-primary)" stroke-width="0" fill="none"/>
            <circle cx="750" cy="750" r="{190}" fill="var(--q-background)" stroke="var(--q-primary)" stroke-width="0"/>
        '''
    def _draw_indicator(alt_deg):
        return f'''
            <circle cx="750" cy="750" r="20" fill="var(--q-background)" stroke="var(--q-primary)" stroke-width="8"/>
            <g transform="rotate({alt_deg -90}, 750, 750)"> <polygon points="750, 600, 700, 700, 800, 700" fill="var(--q-primary)"/></g>
        '''
    
    return f'''
        <svg>
            {_draw_cross()}
            {_draw_indicator(alt_deg)}
        </svg>
    '''


def draw_orientation():     
    with Container():
            
        Header("explore", 'TELESCOPE ORIENTATION')
            
        with Content():
            with ui.row():
                canvas_heading = ui.interactive_image(size=(800, 800)).classes('w-64')
                canvas_heading.set_content(_drawHeading(0, 0))
            with ui.row().classes('w-full'):
                with ui.column().classes("font-bold"):
                    ui.label("Heading:")
                ui.space()
                with ui.column():
                    heading = ui.label()
                with ui.column():
                    ui.label("deg")

        with Content():   
            with ui.row(): 
                canvas_altitude = ui.interactive_image(size=(800, 800)).classes('w-64')
                canvas_altitude.set_content(_drawAltitude(0))
            with ui.row().classes('w-full'):
                with ui.column().classes("font-bold"):
                    ui.label("Altitude:")
                ui.space()
                with ui.column():
                    altitude = ui.label()
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
            hdg = random.uniform(0, 360)
            alt = random.uniform(0, 90)

            # Update the UI with new readings
            heading.set_text(f'{hdg:.1f}')
            altitude.set_text(f'{alt:.1f}')

            # Update both canvases simultaneously
            canvas_heading.set_content(_drawHeading(0, hdg))
            canvas_altitude.set_content(_drawAltitude(alt))

            # Update every second
            await asyncio.sleep(0.5)
    
    # Use asyncio.create_task to start the magnetometer reading asynchronously
    # asyncio.create_task(read_magnetometer(True))

ui.run()
