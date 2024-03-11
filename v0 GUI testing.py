from pathlib import Path

import pandas as pd
import PySimpleGUI as sg


def is_valid_path(filepath):
    if filepath and Path(filepath).exists():
        return True
    sg.popup_error("Filepath not correct")
    return False

def display_excel_file(excel_file_path, sheet_name):
    df = pd.read_excel(excel_file_path, sheet_name) #convert excel into pandas data frame (df)
    filename = Path(excel_file_path).stem   #.stem keeps only the filename from the whole path
    sg.popup_scrolled(df.dtypes, "=" * 25, df, title=filename)


def convert_to_csv(excel_file_path, output_folder, sheet_name, separator, decimal):
    df = pd.read_excel(excel_file_path, sheet_name) #convert excel into pandas data frame (df)
    filename = Path(excel_file_path).stem   #.stem keeps only the filename from the whole path
    outputfile = Path(output_folder) / f"{filename}.csv"
    df.to_csv(outputfile, sep=separator, decimal=decimal, index=False) #df.to_csv converts dataframe into a csv file 
    sg.popup_no_titlebar("Done.")


# - - - - - - GUI Definition - - - - - - #
layout = [
    [sg.Text("Input File:"), sg.Input(key="-IN-"), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),))],
    [sg.Text("Output Folder:"), sg.Input(key="-OUT-"), sg.FolderBrowse()],
    [sg.Exit(), sg.Button("Display Excel File"), sg.Button("Convert To CSV")],
]

# Run the GUI Window
window = sg.Window("Excel to CSV Converter", layout)

while True:
    event, values = window.read()
    print(event, values) #can be removed
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "Display Excel File":
        if is_valid_path(values["-IN-"]):
            display_excel_file(values["-IN-"], "Sheet1")
    if event == "Convert To CSV":
        if (is_valid_path(values["-IN-"])) and (is_valid_path(values["-OUT-"])):
            convert_to_csv(
                excel_file_path=values["-IN-"],
                output_folder=values["-OUT-"],
                sheet_name="Sheet1",
                separator=",",
                decimal=".",
            )
window.close()