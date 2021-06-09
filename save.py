from tkinter import filedialog
import show
import json

def save_protocol_json():
    filename = filedialog.asksaveasfilename(parent=show.root, defaultextension='.json', filetypes=[('json files', '*.json')])
    if (filename != '' and show.root.protocol_dict):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(root.protocol_dict))


def save_log_json():
    filename = filedialog.asksaveasfilename(parent=show.root, defaultextension='.json', filetypes=[('json files', '*.json')])
    if (filename != '' and show.root.log_dict):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(root.log_dict))