# !/usr/bin/env python

# dnsmasq failover (keepalived)
# Author: jiasir (Taio Jia) <jiasir@icloud.com>
# Source code: https://github.com/nofdev/dnsmasq-ha
# License: The MIT license

# Imports.
import os
import sys
import shutil
from command import Command

# Create the command class.
command = Command ()

# Usage of the program.
def usage ():
    print ('Usage: sudo python dnsmasq-ha.py <master|backup>')

# Go and get the code.
def update_apt_source ():
    print ('Waiting for apt source update...')
    command.execute ('sudo', 'apt-get', 'update')

# Install dnsmasq.
def install_dnsmasq():
    print ('Install dnsmasq...')
    command.execute ('sudo', 'apt-get', '-y', 'install', 'dnsmasq')

def install_keepalived (role):
    if (role == 'master'):
        print ('Install dnsmasq as a master node...')
        command.execute('sudo', 'apt-get', '-y', 'install', 'keepalived')
        shutil.copy ('conf/keepalived.conf.master', '/etc/keepalived/keepalived.conf')
    elif (role == 'backup'):
        print ('Install dnsmasq as a backup node...')
        command.execute ('sudo', 'apt-get', '-y', 'install', 'keepalived')
        shutil.copy ('conf/keepalived.conf.backup', '/etc/keepalived/keepalived.conf')

# Main ppogram.
def main():
    # Update the source.
    update_apt_source ()
    # Check on which environment to update.
    if (len (sys.argv) > 1):
        option = sys.argv [1]
    # Update the master if it is the argument to this script.
    if (option == "master"):
        install_dnsmasq ()
        install_keepalived ('master')
        print ('Done.')
    elif (option == "backup"):
        install_dnsmasq ()
        install_keepalived ('backup')
        print ('Done')
    else:
        # Otherwise show usage.
        usage ()

# Run the main program if called directly.
if (__name__ == '__main__'):
    if (os.getuid () == 0):
        main ()
    else:
        print ('You do not have permission!!')
        usage ()
        exit ()
