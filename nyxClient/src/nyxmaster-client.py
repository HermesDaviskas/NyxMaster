from nicegui import ui
from components.webpage.header.header import createHeader 
from utilities.themeSelector.themeSelector import nightTheme
from utilities.fullScreenToggle.fullScreenToggle import showInFullScreen
from components.gauges.gps.gps import draw_gps
from components.gauges.horAlignment.horAlignment import draw_horAlignment
from components.gauges._html_components.component_structure import Header

@ui.page('/')
def index():
    ui.add_css(":root {--nicegui-default-padding: 1.5rem; --nicegui-default-gap: 1rem;}")
    
    nightTheme(True)
    showInFullScreen(False)
    createHeader("NYX Master", "Automatic Telescope Motion Control & Image Analysis")
    draw_gps()
    draw_horAlignment()


ui.run()
