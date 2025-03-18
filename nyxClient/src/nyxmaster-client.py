from nicegui import ui
from components.webpage.header.header import createHeader 
from utilities.themeSelector.themeSelector import nightTheme
from utilities.fullScreenToggle.fullScreenToggle import showInFullScreen

@ui.page('/')
def index():
    ui.add_css(":root {--nicegui-default-padding: 1.5rem; --nicegui-default-gap: 1rem;}")
    
    nightTheme(True)  # Start with day mode
    showInFullScreen(False)

    createHeader("NYX Master", "Automatic Telescope Motion Control & Image Analysis")


ui.run()
