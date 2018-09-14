#!/usr/bin/env python
#!python
# postfixbuddy.py created by Daniel Hand (daniel.hand@rackspace.co.uk)
# This is s a recreation of pfHandle.perl but in Python.

import os
import os.path
import argparse

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
    parser.add_argument("-D", "--delete", dest="delete_message", action="store_true",
                        help="Delete the email message. Options: # or \"from:\"")
    parser.add_argument("-r", "--reprocess", dest="process_queue",
                        action="store_true", help="Try to reprocess queued messages now")
    parser.add_argument("-m", "--message", dest="display_message",
                        action="store_true", help="Displays the message")
    parser.add_argument("-N", dest="display_message_ID",
                        action="store_true", help="Displays only the message IDs")
    parser.add_argument("-P", dest="purge_messages", action="store_true",
                        help="Purge all messages from the mail queue. Options: hold|incoming|active|deferred")
    parser.add_argument("-s", "--stats", dest="display_stats",
                        action="store_true", help="Display the mail queue statistics")
    parser.add_argument("-S", "--subject", dest="select_subject", action="store_true",
                        help="Delete mail with this subject. Options: \"$subjectname\"")
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


def main():
    parser = get_options()
    args = parser.parse_args()
    if args.list_queues:
        list_queues()


if __name__ == '__main__':
    main()