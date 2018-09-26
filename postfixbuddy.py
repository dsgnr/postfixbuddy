#!/usr/bin/env python
#!python
# postfixbuddy.py created by Daniel Hand (daniel.hand@rackspace.co.uk)
# This is s a recreation of pfHandle.perl but in Python.

import os
import os.path
import argparse
from subprocess import call

__version__ = '0.1.0'

# Variables
pf_dir = '/var/spool/postfix/'
active_queue = pf_dir + 'active'
deferred_queue = pf_dir + 'deferred'
bounce_queue = pf_dir + 'bounce'
corrupt_queue = pf_dir + 'corrupt'
incoming_queue = pf_dir + 'incoming'


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--list", dest="list_queues", action="store_true",
                        help="List all the current mail queues")
    parser.add_argument("-p", "--purge", dest="purge_messages", action="store_true",
                        help="Purge all messages from the mail queue.")
    version = '%(prog)s ' + __version__
    parser.add_argument('-v', '--version', action='version', version=version)
    return parser


def list_queues():
    queue_list = ['Active', 'Deferred', 'Bounce', 'Corrupt', 'Incoming']
    queue_types = [active_queue, deferred_queue,
                   bounce_queue, corrupt_queue, incoming_queue]
    print
    print '============== Mail Queue Summary =============='
    for index in range(len(queue_list)):
        print queue_list[index], 'Queue Count:', len([name for name in os.listdir(
            queue_types[index]) if os.path.isfile(os.path.join(queue_types[index], name))])
    print

def purge_messages():
    check = str(raw_input("Question ? (Y/N): ")).lower().strip()
    try:
        if check[0] == 'y':
            call(["postsuper", "-d", "ALL"])
        elif check[0] == 'n':
            return False
        else:
            print('Invalid Input')
            return purge_messages()
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        return purge_messages()        


def main():
    parser = get_options()
    args = parser.parse_args()
    if args.list_queues:
        list_queues()
    if args.purge_messages:
        purge_messages()

if __name__ == '__main__':
    main()