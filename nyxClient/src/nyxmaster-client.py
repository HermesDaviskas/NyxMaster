from nicegui import ui
from components.webpage.header.header import createHeader 
from utilities.themeSelector.themeSelector import nightTheme
from utilities.fullScreenToggle.fullScreenToggle import showInFullScreen
from components.gauges.gps.gps import draw_gps
from components.gauges.mountAlignment.mountAlignment import draw_mountAlignment
from components.gauges._html_components.component_structure import Header
from components.gauges.orientation.orientation import draw_orientation


@ui.page('/')
def index():
    ui.add_css(":root {--nicegui-default-padding: 1.5rem; --nicegui-default-gap: 1rem;}")
    
    nightTheme(True)
    showInFullScreen(False)
    createHeader("NYX Master", "Automatic Telescope Motion Control & Image Analysis")
    with ui.row():
        with ui.column():
            draw_gps()
            draw_mountAlignment()
        with ui.column():
            draw_orientation()



ui.run()
