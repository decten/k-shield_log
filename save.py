from tkinter import filedialog
import json
import main

def save_protocol_json():
    filename = filedialog.asksaveasfilename(parent=main.root, defaultextension='.json', filetypes=[('json files', '*.json')])
    if (filename != '' and main.root.protocol_dict):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(main.root.protocol_dict))


def save_log_json():
    filename = filedialog.asksaveasfilename(parent=main.root, defaultextension='.json', filetypes=[('json files', '*.json')])
    if (filename != '' and main.root.log_dict):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(main.root.log_dict))