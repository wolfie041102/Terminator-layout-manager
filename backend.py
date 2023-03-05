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
    termconfigpath = f"/home/{getuser()}/.config/terminator/config"
    
    if not exists(termconfigpath):
        print('fail')
        return False
    
    with open(termconfigpath) as terminator_config:
        for line in terminator_config:
            line = line.rstrip('\n')
            
            if line == "[layouts]":
                read_file = True
                continue
            elif line == "[plugins]":
                read_file = False
                
            if read_file:
                if re.search(" \[{2}([A-Za-z0-9_-]+)\]{2}", line):
                    cur_layout = line[4:-2]
                    layouts[cur_layout] = {}
                    continue
                elif re.search(" \[{3}([A-Za-z0-9_-]+)\]{3}", line):
                    child = line[7:-3]
                    layouts[cur_layout][child] = {}
                    continue
                else:
                    field = str(re.findall('^ +\w+', line))[8:-2]
                    value = str(re.findall('\S+$', line))[2:-2]
                    layouts[cur_layout][child][field] = value
                    continue
    print(layouts)
    

# def main():
    
#     # define vars
    
#     # ---g

get_layouts()        