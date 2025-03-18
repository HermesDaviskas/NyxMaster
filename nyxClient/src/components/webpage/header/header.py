from nicegui import ui
from utilities.themeSelector.themeSelector import nightTheme
from utilities.fullScreenToggle.fullScreenToggle import showInFullScreen

def createHeader(title: str, subtitle: str):

    with ui.row().classes('w-full border').style("border: none;"):

        # Header content with dynamic color adjustment and shadow
        with ui.column():
            ui.label(title) \
                .style("font-size: 24px; font-weight: bold; color: inherit; text-align: center; text-shadow: 1px 1px 1px currentColor;" )
            ui.label(subtitle) \
                .style("font-size: 12px; color: inherit; text-align: center; text-shadow: 1px 1px 1px currentColor;" )
            
        ui.space()

        # Wrap the switches in a column to stack them vertically

        # Night mode toggle switch with callback
        night_mode_switch = ui.switch('Night theme', value=True, on_change=lambda e: nightTheme(e.value)).style("color: inherit;")
        # Full screen switch with callback
        fullscreen_switch = ui.switch('Full screen', value=False, on_change=lambda e: showInFullScreen(e.value)).style("color: inherit;")

        ui.separator().style("margin-bottom: 15px; color: inherit;")

    # Example button (ensures button text color follows the theme)
    ui.button("Example Button", on_click=lambda: ui.notify("Button Clicked!")).style("color: inherit;")
