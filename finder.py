import os
import glob

import PySimpleGUI as sg


work_dir = os.getcwd()
pattern = "*1200*.STEP"

def find_files(folder, pattern):
    out = dict()
    for root, dirs, files in os.walk(folder):
        for file in files:
            # if file.endswith('.STEP'):
            #     # print(os.path.join(root, file))
            if glob.fnmatch.fnmatch(file, pattern):
                # print(file)
                # print(os.path.join(root, file))
                out[file] = os.path.join(root, file)
    return out
                
                


sg.theme("DarkTeal2")
layout = [[sg.T("")], [sg.Text("Choose a file: "), sg.Input(), sg.FolderBrowse(key="-IN-")],[sg.Button("Submit")]]

###Building Window
window = sg.Window('My File Browser', layout, size=(600,150))
    
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        print(values["-IN-"])
        blocks = find_files(values["-IN-"], pattern)
        print(blocks.keys())
        