
from nicegui import ui

def showInFullScreen(mode: bool):
    fullscreen = ui.fullscreen()
    fullscreen.toggle()

    if not mode:
        fullscreen.exit()
    else:
        fullscreen.enter()

