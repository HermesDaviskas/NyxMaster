from nicegui import ui
from .._html_components.component_structure import Container, Header, Content, Footer
from datetime import datetime


def draw_gps():

    with Container("280px"):

        Header('gps_fixed', 'GPS DATA')

        with Content():
            with ui.column().classes("font-bold"):
                ui.label("sys:")
                ui.label("utc:")
                ui.label("Lat:")
                ui.label("Lon:")

            ui.space()

            with ui.column():
                sys_time = ui.label(datetime.now().isoformat())
                utc_time = ui.label("- -  :  - -")
                lat_label = ui.label("- - N   - - E")
                lon_label = ui.label("- - N   - - E")
        
        with Footer():
            ui.chip('sync', icon='replay').props('outline square').style("margin: 0; cursor: pointer; padding: 15px 10px; ").classes('rounded-lg')

    def update_time():
        sys_time.set_text(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"))

    ui.timer(1.0, update_time)  # Update time every second

