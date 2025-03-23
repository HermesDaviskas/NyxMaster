from nicegui import ui
from .._html_components.component_structure import *

from .drawLine import draw_line

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
            <circle cx="400" cy="400" r="{line_lth /2-40}" stroke="var(--q-primary)" fill="none"/>
            <circle cx="400" cy="400" r="190" fill stroke="var(--q-primary)" stroke-width="2"/>
        '''
    def _draw_indicator(heading_deg):
        return f'''
            <circle cx="400" cy="400" r="20" fill="var(background-color)" stroke="var(--q-primary)" stroke-width="8"/>
            <g transform="rotate({heading_deg}, 400, 400)"> <polygon points="400, 250, 350, 350, 450, 350" fill="var(--q-primary)"/></g>
        '''
    return f'''
        <svg width="800" height="800"">
            {_draw_cross()}
            {_draw_indicator(heading_deg)}
        </svg>
    '''

def _drawAltitude(alt_deg):
    def _draw_cross():
        line_lth = 660
        return f'''
            {draw_line(750, 750, -90, line_lth, "0")}
            {draw_line(750, 750, -75, line_lth, "15")}
            {draw_line(750, 750, -60, line_lth, "30")}
            {draw_line(750, 750, -45, line_lth, "45")}
            {draw_line(750, 750, -30, line_lth, "60")}
            {draw_line(750, 750, -15, line_lth, "75")}
            {draw_line(750, 750, -00, line_lth, "90")}
            <circle cx="750" cy="750" r="{line_lth -40}" stroke="var(--q-primary)" fill="none"/>
            <circle cx="750" cy="750" r="{190}" fill stroke="var(--q-primary)" stroke-width="2"/>
        '''
    def _draw_indicator(alt_deg):
        return f'''
            <circle cx="750" cy="750" r="20" fill="var(background-color)" stroke="var(--q-primary)" stroke-width="8"/>
            <g transform="rotate({alt_deg -90}, 750, 750)"> <polygon points="750, 600, 700, 700, 800, 700" fill="var(--q-primary)"/></g>
        '''
    
    return f'''
        <svg width="800" height="800"">
            {_draw_cross()}
            {_draw_indicator(alt_deg)}
        </svg>
    '''


def draw_orientation():
            
    with Container("280px"):
            Header("explore", 'TELESCOPE ORIENTATION')
            with Content():
                heading = 10
                canvas = ui.interactive_image(size=(800, 800))
                canvas.classes('w-64')
                canvas.style('border:none; background-color:transparent; padding:15px;')
                canvas.set_content(_drawHeading(0, heading))
                with ui.column().classes("font-bold"):
                    ui.label("Heading:")
                ui.space()
                with ui.column():
                    sys_time = ui.label(heading)
            with Content():    
                canvas = ui.interactive_image(size=(800, 800))
                canvas.classes('w-64')
                canvas.style('border:none; background-color:transparent; padding:15px;')
                canvas.set_content(_drawAltitude(37.5))
                ui.label("Altitude: ")
