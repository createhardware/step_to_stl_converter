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
layout = [[sg.T("")], 
          [sg.Text("Choose a input folder: "), sg.Input(), sg.FolderBrowse(key="-IN-")],
          [sg.Text("Write a pattern: "), sg.Input(key="-PATTERN-", default_text=pattern), sg.Text('Example: "*1200*.STEP"')],
          [sg.Text("Choose a output folder: "), sg.Input(), sg.FolderBrowse(key="-OUT-")],
          [sg.T("")], 
          [sg.Button("Submit"), sg.Button("Copy files"), sg.Button("Convert to STL")],
          ]

###Building Window
window = sg.Window('My File Browser', layout, size=(600,200))
    
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        print(values["-IN-"])
        blocks = find_files(values["-IN-"], values["-PATTERN-"])
        print(blocks.keys())
        # print(blocks)
        
    elif event == "Copy files":
        pass
        print("copy files to " + values["-OUT-"] + " , please!")
    
    elif event == "Convert to STL":
        print("TODO: convert files")
        
        