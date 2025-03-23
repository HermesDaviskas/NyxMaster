# themeSelector.py
from nicegui import ui

def nightTheme(mode: bool):
    dark = ui.dark_mode()
    
    if not mode:  # Day mode
        ui.colors()
        dark.disable()
        ui.run_javascript("document.body.style.color = '#5898d4';")  # Ensure text is black
        ui.run_javascript("document.body.style.backgroundColor = '#FFFFFF';")

    else:  # Night mode
        ui.colors(
            primary='#FF4444',
            secondary='#222222',
            accent='#FF4444',
            positive='#4CAF50',
            negative='#F44336',
            info='#2196F3',
            warning='#FFC107',
            text='#FF4444',
            background='#000000',
            surface='#111111'
        )
        dark.enable()
        ui.run_javascript("document.body.style.color = '#FF4444';")  # Ensure text is red
        ui.run_javascript("document.body.style.backgroundColor = '#000000';")
