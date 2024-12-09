import TkEasyGUI as eg

# Size(width=1920, height=1080)

# Create window
layout = [
    [eg.Text("For wisdom is better than corals;\n" + 
             "All other desirable things cannot compare to it.")],
    [eg.Button("OK")]
#    [eg.geometry("300x150+100+300")]
#    [eg.location(100,300)]
]
#location=(0,0)
# eg.eg.set_location(xy=(10,10))
window = eg.Window("Title", layout=layout,size=(200,100),resizable=False)
# window.move(10,10)
# xPos = 1000 # X座標
# yPos = 700  # Y座標
# window.geometry(f"+{xPos}+{yPos}")
# window.set_location(xy=(10,10))
# print(window.get_location())
# window = eg.Window("Proverb", layout=layout)
# Event loop
while True:
    # get window event
    event, values = window.read()
    # print(window.get_location())
    # close button
    if event == eg.WINDOW_CLOSED:
        break
    # check OK Button
    if event == "OK":
        eg.popup("Pushed OK Button")
        break
window.close()
