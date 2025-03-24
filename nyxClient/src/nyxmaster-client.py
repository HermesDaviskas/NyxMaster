from nicegui import ui
from components.webpage.header.header import createHeader 
from utilities.themeSelector.themeSelector import nightTheme
from utilities.fullScreenToggle.fullScreenToggle import showInFullScreen
from components.gauges.gps.gps import draw_gps
from components.gauges.mountAlignment.mountAlignment import draw_mountAlignment
from components.gauges.orientation.orientation import draw_orientation

@ui.page('/')
def index():

    nightTheme(False)
    showInFullScreen(False)
    createHeader("NYX Master", "Automatic Telescope Motion Control & Image Analysis")

    with ui.row().style('width: 100%; height: 86vh;'):  # Row takes full height
        with ui.column().style('width:18%; height:100%'):  # Column takes full height but does not stretch items
            draw_gps()
            draw_mountAlignment()
        with ui.column().style('width:18%; height:100%'):  # Column takes full height but does not stretch items
            draw_orientation()

ui.run()
