#!/usr/bin/python
"""
Loads data from a pg_dump file into a Vagrant Box.

Example usage:
python import_pgdump.py <abs path to pg_dump> <abs path to folder containing vagrant file>

note:
If your vagrants postgres db is password protected,
you'll be prompted for that password once this script
tries to ssh.

You'll see many
`pg_restore: [archiver (db)] could not execute query: ERROR:  role "<rolename>" does not exist`
messages. Don't worry, you won't need that role to have permissions on the database
because you're going to be using the vagrant user to connect.

"""

import sys
import os

if len(sys.argv) == 3:
    file_path = sys.argv[1]
    vagrant = sys.argv[2]
    file_minus_path = os.path.basename(file_path)
    ready_file = "scp -P 2222 {f} vagrant@localhost:/home/vagrant/".format(f=file_path)
else:
    print "Please supply an aboluted path to a pg_dump followed by\nan absolute path to a folder containing a Vagrant File."
    sys.exit()
origin = os.path.dirname(os.path.abspath(__file__))
os.chdir(vagrant)
os.system("vagrant halt")
os.system("vagrant up")
os.system(ready_file)
os.system('vagrant ssh --command "dropdb vagrant"')
os.system('vagrant ssh --command "createdb vagrant"')
os.system('vagrant ssh --command "pg_restore -d vagrant ~/{f}"'.format(f=file_minus_path))
os.chdir(origin)
