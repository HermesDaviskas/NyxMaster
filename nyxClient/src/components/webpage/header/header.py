from nicegui import ui
from utilities.themeSelector.themeSelector import nightTheme
from utilities.fullScreenToggle.fullScreenToggle import showInFullScreen

def createHeader(title: str, subtitle: str):

    with ui.row().classes('w-full'):

        with ui.row().style('align-items: center; width: 100%'):
            with ui.column().style('gap: 0px;'):
                ui.label(title).style("font-size: 24px; font-weight: bold; color: inherit; text-align: center; color: var(--q-primary);" )
                ui.label(subtitle).style("font-size: 12px; color: inherit; text-align: center;" )
                
            ui.space()

            night_mode_switch = ui.switch('Night theme', value=False, on_change=lambda e: nightTheme(e.value)).style("color: var(--q-primary);")
            fullscreen_switch = ui.switch('Full screen', value=False, on_change=lambda e: showInFullScreen(e.value)).style("color: var(--q-primary);")

        ui.separator().style("margin-bottom: 15px; background-color: var(--q-secondary)")
