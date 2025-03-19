from nicegui import ui
from datetime import datetime

def draw_gauge():

    gauge = ui.row()
    gauge.classes('w-64 rounded-2xl justify-between')
    gauge.style('border: solid; border-width: 1px; border-color: var(--q-primary); background-color: transparent; padding: 20px;')
    with gauge:
        with ui.column():
            with ui.row().classes('justify-between'):
                with ui.column().classes("font-bold"):
                    ui.label("utc:")
                    ui.label("Lat:")
                    ui.label("Lon:")
                with ui.column():
                    time_label = ui.label(datetime.now().isoformat())
                    lat_label = ui.label("0N0E")
                    lon_label = ui.label("0N0E") 
            with ui.row():
                with ui.column():
                    ui.chip('GPS', icon='gps_fixed').props('outline square').style("margin: 0")



    # container = ui.row().classes('w-64 rounded-2xl justify-between')
    # container.style('border: solid; border-width: 1px; border-color: var(--q-primary); background-color: transparent; padding: 20px;')
    # with container:
    #     with ui.column().classes("font-bold"):
    #         ui.label("utc:")
    #         ui.label("Lat:")
    #         ui.label("Lon:")

    #     with ui.column().classes():
    #         time_label = ui.label(datetime.now().isoformat())
    #         lat_label = ui.label("0N0E")
    #         lon_label = ui.label("0N0E") 

    #     ui.chip('GPS', icon='gps_fixed').props('outline square').style("margin: 0")

    # Function to update time dynamically
    def update_time():
        time_label.set_text(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"))

    ui.timer(1.0, update_time)  # Update time every second

draw_gauge()

ui.run()
