#!/usr/bin/python
"""
Clears all the data in a Vagrant Box.

Example usage:
python clear_vagrant.py <abs path to vagrant file>

note:
If your vagrants postgres db is password protected,
you'll be prompted for that password once this script
tries to ssh.

"""
import os, sys
if len(sys.argv) > 1:
    vagrant = sys.argv[1]
else: 
    print "Please supply an absolute path to a folder containing a Vagrant File."
    sys.exit()
origin = os.path.dirname(os.path.abspath(__file__))
os.chdir(vagrant)
os.system('vagrant ssh --command "dropdb vagrant"')
os.system('vagrant ssh --command "createdb vagrant"')
os.chdir(origin)