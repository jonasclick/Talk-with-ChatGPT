import PySimpleGUI as sg

# - - - - - - GUI Definition - - - - - - #
layout = [[sg.Text("Input File:"), sg.Input(key="-IN-"), sg.FileBrowse(file_types=(("Excel Files", "*.xls*"),))],
    [sg.Text("Output Folder:"), sg.Input(key="-OUT-"), sg.FolderBrowse()],
    [sg.Exit(), sg.Button("Convert To CSV")],]

window = sg.Window("Excel to CSV Converter", layout)

while True:
    event, values = window.read()
    print(event, values) #can be removed
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "Convert To CSV":
        sg.popup_error("Not yet implemented")
window.close()