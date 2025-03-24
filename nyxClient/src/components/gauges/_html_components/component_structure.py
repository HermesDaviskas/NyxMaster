from nicegui import ui

def Container():
    return ui.element('div').classes('rounded-2xl h-full w-full justify-between') \
        .style('border: solid 1px var(--q-primary); background-color: transparent; padding: 20px; display: flex; flex-direction: column; gap:30px')

def Header(icon, title):
    with ui.element('div').classes('w-full flex items-center').style('gap: 15px'):
        ui.icon(icon).classes('text-xl')
        ui.label(f'{title}')
        ui.separator().classes('bg-primary w-full')

def Content():
    return ui.element('div').classes('h-full w-full flex items-center justify-start').style('display: flex; flex-direction: column; gap: 10px;')

def Footer():
    return ui.element('div').classes('w-full flex items-end justify-start')
