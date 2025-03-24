# File: project_folder/Client/src/index.py

# Import necessary modules from NiceGUI and other custom components
from nicegui import ui
from components.webpage.header.header import createHeader 
from utilities.themeSelector.themeSelector import nightTheme
from utilities.fullScreenToggle.fullScreenToggle import showInFullScreen
from components.gauges.gps.gps import gps_data_ui
from components.gauges.mountAlignment.mountAlignment import mount_leveling_ui
from components.gauges.orientation.orientation import orientation_ui

# Define the main page route for the telescope control UI
@ui.page('/')
def index():

    # Set the theme for the page; False indicates light theme
    # Set fullscreen toggle status; False means fullscreen is disabled
    nightTheme(False)
    showInFullScreen(False)

    # Create a header at the top of the page with a title and subtitle
    createHeader("NYX Master", "Automatic Telescope Motion Control & Image Analysis")

    # Create a row layout for the page
    with ui.row().style('width: 100%; height: 86vh;'):

        with ui.column().style('width:18%; height:100%'): 
            gps_data_ui()
            mount_leveling_ui()

        with ui.column().style('width:18%; height:100%'):
            orientation_ui() 

# Start the application server and begin rendering the UI
ui.run()
