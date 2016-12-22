#!/usr/bin/env python

import os, sys, json, glob
from unrar import rarfile

CONFIG_FILE = 'config.json'

"""
Open and load a file at the json format
"""

def open_and_load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as config_file:
            return json.loads(config_file.read())
    else:
        print "File [%s] doesn't exist, aborting." % (CONFIG_FILE)
        sys.exit(1)

"""
Get files names described by sfv
"""

def get_files_from_sfv(sfv):
    res = []
    with open(sfv, 'r') as content_file:
        content = content_file.readlines()
        for l in content:
            res.append(l.split(' ')[0])
    return res

def check_sfv(sfv, fs):
    print "check " + sfv
    if (len(fs) == 0):
        print "!!! SFV is empty"
        return False
    for f in fs:
        if (not os.path.exists(f)):
            print "!!! file missing: " + f
            return False
    return True

def unrar(sfv, fs):
    print "unrar " + sfv
    for f in fs:
        if (f.endswith('.rar')):
            rar = rarfile.RarFile(f)
            todo = set()
            for x in rar.namelist():
                if (not os.path.exists(x)):
                    todo.add(x)
            lst = list(todo)
            print "Files to extract:"
            print lst
            if (len(lst) > 0):
                rar.extractall(members=lst)
    return True

def delete_files(sfv, fs):
    print "delete files in sfv"
    for f in fs:
        os.unlink(f)
    print "delete sfv: " + sfv
    os.unlink(sfv)

"""
Process folder in path p
"""

def process_path(p):
    print "*** Processing " + p
    os.chdir(p)
    for f in glob.glob("*/*.sfv"):
        os.chdir(f.split('/')[0])
        rep = f.split('/')[0]
        sfv = f.split('/')[1]
        fs = get_files_from_sfv(sfv)
        print ""
        print "--- " + rep
        if True:
            if (check_sfv(sfv, fs)):
                if unrar(sfv, fs):
                    delete_files(sfv, fs)
        os.chdir('..')

"""
Main
"""

if __name__ == "__main__":
    config = open_and_load_config()
    for p in config['paths']:
        process_path(p.encode('utf-8'))
