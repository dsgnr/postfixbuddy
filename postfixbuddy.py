#!/usr/bin/env python
# postfixbuddy.py created by Daniel Hand (daniel.hand@rackspace.co.uk)
# This is a recreation of pfHandle.perl but in Python.

from __future__ import absolute_import, division, print_function
import os
from os.path import join
import argparse
import sys
import subprocess
from subprocess import call

__version__ = '0.1.0'


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list', dest='list_queues',
                        action='store_true',
                        help='List all the current mail queues')
    parser.add_argument('-p', '--purge', dest='purge_queues', type=str,
                        choices=['active', 'bounce', 'corrupt',
                                 'deferred', 'hold', 'incoming'],
                        help='Purge messages from specific queues.')
    parser.add_argument('-m', '--message', dest='delete_mail', type=str,
                        help='Delete specific email based on mailq ID.')
    parser.add_argument('-c', '--clean', dest='clean_queues',
                        action='store_true',
                        help='Purge messages from all queues.')
    parser.add_argument('-H', '--hold', dest='hold_queues',
                        action='store_true',
                        help='Hold all mail queues.')
    parser.add_argument('-r', '--release', dest='release_queues',
                        action='store_true',
                        help='Release all mail queues from held state.')
    parser.add_argument('-f', '--flush', dest='process_queues',
                        action='store_true', help='Flush mail queues')
    parser.add_argument('-D', '--delete', dest='delete_by_search', type=str,
                        help='Delete based on subject or email address')
    parser.add_argument('-s', '--show', dest='show_message', type=str,
                        help='Show message from queue ID')
    parser.add_argument('-v', '--version', dest='show_version',
                        action='store_true',
                        help='Shows version information')
    return parser

# All variables defined in this script reply on finding the queue_directory.
# This defines the pf_dir variable which is called later on.
try:
    get_queue_dir = subprocess.Popen(['/usr/sbin/postconf',
                                     '-h', 'queue_directory'],
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
    output, error = get_queue_dir.communicate()
    if output:
        pf_dir = output.split()[0]
except OSError as ex:
    sys.exit('Unable to find Postfix queue directory!')


class color:
    RED = '\033[31m\033[1m'
    GREEN = '\033[32m\033[1m'
    YELLOW = '\033[33m\033[1m'
    BLUE = '\033[34m\033[1m'
    MAGENTA = '\033[35m\033[1m'
    CYAN = '\033[36m\033[1m'
    WHITE = '\033[37m\033[1m'
    RESET = '\033[0m'


# Variables
active_queue = pf_dir + '/active'
bounce_queue = pf_dir + '/bounce'
corrupt_queue = pf_dir + '/corrupt'
deferred_queue = pf_dir + '/deferred'
hold_queue = pf_dir + '/hold'
incoming_queue = pf_dir + '/incoming'
queue_list = ['Active', 'Bounce', 'Corrupt',
              'Deferred', 'Hold', 'Incoming']
queue_types = [active_queue, bounce_queue, corrupt_queue,
               deferred_queue, hold_queue, incoming_queue]
parser = get_options()
args = parser.parse_args()


def show_version():
    print(color.GREEN + '''
                    _    __ _      _               _     _
    _ __   ___  ___| |_ / _(_)_  _| |__  _   _  __| | __| |_   _
    | '_ \ / _ \/ __| __| |_| \ \/ / '_ \| | | |/ _` |/ _` | | | |
    | |_) | (_) \__ \ |_|  _| |>  <| |_) | |_| | (_| | (_| | |_| |
    | .__/ \___/|___/\__|_| |_/_/\_\_.__/ \__,_|\__,_|\__,_|\__, |
    |_|                                                     |___/

    version: ''' + __version__, color.RESET)


def list_queues():
    print(color.MAGENTA + '==== Mail Queue Summary ====' +
          color.RESET)
    for index in range(len(queue_list)):
        file_count = sum(len(files) for _, _, files in
                         os.walk(queue_types[index]))
        print(color.YELLOW + queue_list[index], 'Queue Count:' +
              color.BLUE, file_count, color.RESET)
    print


def purge_queues():
    print(color.RED + 'Do you really want to purge the ' +
          args.purge_queues + ' queue? (Y/N): ' + color.RESET)
    tty = open('/dev/tty')
    option_answer = tty.readline().strip()
    tty.close()
    if option_answer == 'y':
        call(['postsuper', '-d', 'ALL', args.purge_queues])
        print(color.GREEN + 'Purged all mail from the ' +
              args.purge_queues + ' queue!' + color.RESET)
    if option_answer != 'y':
        print(color.RED + 'Invalid Input' + color.RESET)
        exit()


def clean_queues():
    print(color.RED + 'Do you really want to purge'
          'ALL mail queues? (Y/N): ' + color.RESET)
    tty = open('/dev/tty')
    option_answer = tty.readline().strip()
    tty.close()
    if option_answer == 'y':
        call(['postsuper', '-d', 'ALL'])
        print(color.GREEN + 'Purged all mail queues!' + color.RESET)
    if option_answer != 'y':
        print(color.RED + 'Invalid Input' + color.RESET)
        exit()


def delete_mail():
    print(color.RED + 'Do you really want to delete mail ' +
          args.delete_mail + '? (Y/N): ' +
          color.RESET)
    tty = open('/dev/tty')
    option_answer = tty.readline().strip()
    tty.close()
    if option_answer == 'y':
        call(['postsuper', '-d', args.delete_mail])
        print(color.GREEN + 'Deleted mail ID: ' + color.YELLOW +
              args.delete_mail + color.GREEN + '!' + color.RESET)
    if option_answer != 'y':
        print(color.RED + 'Invalid Input' + color.RESET)
        exit()


def hold_queues():
    call(['postsuper', '-h', 'ALL'])
    print(color.GREEN + 'All mail queues now on hold!' + color.RESET)


def release_queues():
    call(['postsuper', '-H', 'ALL'])
    print(color.GREEN + 'Queues no longer in a held state!' + color.RESET)


def process_queues():
    call(['postqueue', '-f'])
    print(color.GREEN + 'Flushed all queues!' + color.RESET)


def show_message():
    call(['postcat', '-q', args.show_message])


def delete_by_search():
    count = 0
    for index in range(len(queue_list)):
        for (dirname, dirs, files) in os.walk(queue_types[index]):
            for mail_id in files:
                thefile = os.path.join(dirname, mail_id)
                for line in open(thefile):
                    if args.delete_by_search in line:
                        subprocess.Popen(['/usr/sbin/postsuper',
                                         '-d', mail_id],
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
                        count += 1
    print(color.BLUE + 'Looking for mail containing: \"' +
          args.delete_by_search + '\"...' + color.RESET)
    if count == 0:
        print(color.RED + '\"' + args.delete_by_search +
              '\" not found in search.' + color.RESET)
    if count != 0:
        print(color.GREEN + 'Total deleted: {0}'.format(count) + color.RESET)


def main():
    if args.show_version:
        return show_version()
    if args.list_queues:
        return list_queues()
    if args.purge_queues:
        return purge_queues()
    if args.clean_queues:
        return clean_queues()
    if args.delete_mail:
        return delete_mail()
    if args.hold_queues:
        return hold_queues()
    if args.release_queues:
        return release_queues()
    if args.process_queues:
        return process_queues()
    if args.show_message:
        return show_message()
    if args.delete_by_search:
        return delete_by_search()
    return list_queues()

if __name__ == '__main__':
    main()
