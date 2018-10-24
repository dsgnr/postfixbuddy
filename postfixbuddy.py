#!/usr/bin/env python
#!python
# postfixbuddy.py created by Daniel Hand (daniel.hand@rackspace.co.uk)
# This is a recreation of pfHandle.perl but in Python.

from __future__ import absolute_import, division, print_function
import os
import os.path
import argparse
from subprocess import call

__version__ = '0.1.0'

# Variables
pf_dir = '/var/spool/postfix/'
active_queue = pf_dir + 'active'
bounce_queue = pf_dir + 'bounce'
corrupt_queue = pf_dir + 'corrupt'
deferred_queue = pf_dir + 'deferred'
hold_queue = pf_dir + 'hold'
incoming_queue = pf_dir + 'incoming'


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--list", dest="list_queues", action="store_true",
                        help="List all the current mail queues")
    parser.add_argument('-p', '--purge', dest='purge_messages', type=str, choices=['active', 'bounce', 'corrupt', 'deferred', 'hold', 'incoming'],
                        help="Purge all messages from the mail queue.")
    parser.add_argument("-f", "--flush", dest="process_queues", action="store_true",
                        help="Flush mail queues")
    parser.add_argument("-s", "--show", dest="show_message", type=str, help="Show message from queue ID")
    version = '%(prog)s ' + __version__
    parser.add_argument('-v', '--version', action='version', version=version)
    return parser

def list_queues():
    queue_list = ['Active', 'Bounce', 'Corrupt', 'Deferred', 'Hold', 'Incoming']
    queue_types = [active_queue, bounce_queue, corrupt_queue,
                   deferred_queue, hold_queue, incoming_queue]
    print
    print ('============== Mail Queue Summary ==============')
    for index in range(len(queue_list)):
        print (queue_list[index], 'Queue Count:', len([name for name in os.listdir(
            queue_types[index]) if os.path.isfile(os.path.join(queue_types[index], name))]))
    print

def purge_messages():
    parser = get_options()
    args = parser.parse_args()
    check = str(raw_input("Do you really want to purge the " + args.purge_messages + " queue? (Y/N): ")).lower().strip()
    try:
        if check[0] == 'y':
            call(["postsuper", "-d", "ALL", args.purge_messages])
        elif check[0] == 'n':
            return False
        else:
            print('Invalid Input')
            return purge_messages()
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        return purge_messages()

def process_queues():
    call(["postqueue", "-f"])
    print ('Flushed all queues')

def show_message():
    parser = get_options()
    args = parser.parse_args()
    call(["postcat", "-q", args.show_message])

def main():
    parser = get_options()
    args = parser.parse_args()
    if args.list_queues:
        list_queues()
    if args.process_queues:
        process_queues()
    if args.purge_messages:
        purge_messages()
    if args.show_message:
        show_message()

if __name__ == '__main__':
    main()
