from nicegui import ui

def Container(width):
    return ui.row().classes('rounded-2xl justify-between') \
        .style(f'border: solid 1px var(--q-primary); background-color: transparent; padding: 20px; gap: 35px; width:{width}')

def Header(icon, title):
    with ui.row().style('width: 100%; align-items: center;'):
        ui.icon(f'{icon}').classes('text-xl')
        ui.label(f'{title}')
        ui.space()
        ui.separator().style('background-color: var(--q-primary); height: 1px; width: 100%')

def Content():
    return ui.row().style('width: 100%; justify-content: center;')

def Footer():
    return ui.row().style('width: 100%; justify-content: left; align-items: center;')