#!/usr/bin/env python3
from getpass import getuser
from os.path import exists
import shutil, re

def is_terminator_installed():    
    # check if terminator is installed
    if shutil.which('terminator') != None:
        return True
    else:
        return False
    
read_file = False
def get_layouts():
    global read_file
    layouts = {}
    line_count = 0
    
    termconfigpath = f"/home/{getuser()}/.config/terminator/config"
    
    if not exists(termconfigpath):
        print('fail')
        return False
    
    with open(termconfigpath) as terminator_config:
        for line in terminator_config:
            line = line.rstrip('\n')
            line_count = line_count + 1
            
            if line == "[layouts]":
                read_file = True
                continue
            elif line == "[plugins]":
                read_file = False
                
            if read_file:
                if re.search(" \[{2}([A-Za-z0-9_-]+)\]{2}", line):
                    cur_layout = line[4:-2]
                    layouts[cur_layout] = line_count

    return layouts

def get_layout_settings(layout):
    termconfigpath = f"/home/{getuser()}/.config/terminator/config"
    layout_settings = {}
    
    all_layouts = list(get_layouts().items())
    main_layout_index = [i for i, item in enumerate(all_layouts) if re.search(layout, str(item))]
    main_layout = all_layouts[int(main_layout_index[0])]
    last_layout = all_layouts[-1]
    
    if not exists(termconfigpath):
        print('fail')
        return False
    
    with open(termconfigpath) as terminator_config:
        lines = terminator_config.readlines()[main_layout[1]:(last_layout[1] - 1)]
        for line in lines:
            line = line.rstrip('\n')

            if re.search(" \[{3}([A-Za-z0-9_-]+)\]{3}", line):
                child = line[7:-3]
                layout_settings[child] = {}
                continue
            else:
                field = str(re.findall('^ +\w+', line))[8:-2]
                value = str(re.findall('(\=[a-zA-Z0-9-,:@\" ]+)', line))[4:-2]
                layout_settings[child][field] = value
                continue
    return layout_settings
