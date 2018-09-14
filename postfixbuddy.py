#!/usr/bin/python
#!python
# postfixbuddy.py created by Daniel Hand (daniel.hand@rackspace.co.uk)
# This is s a recreation of pfHandle.perl but in Python.

import argparse

parser = argparse.ArgumentParser(description="pfHandle reimagined in python.")
# List active queue
parser.add_argument("-a", "--active", dest="active_queue", metavar='', action="store_true", help="Lists the current active mail queue")
# List bounced queue
parser.add_argument("-b", "--bounced", dest="bounced_queue", action="store_true", help="Lists the current bounce mail queue")
# List corrupt queue
parser.add_argument("-c", "--corrupt", dest="corrupt_queue", action="store_true", help="Lists the current corrupt mail queue")
# List deferred queue
parser.add_argument("-d", "--deferred", dest="deferred_queue", action="store_true", help="Lists the current deferred mail queue")
# Delete messages
parser.add_argument("-D", "--delete", dest="delete_message", action="store_true", help="Delete the email message. Options: # or \"from:\"")
# Reprocess queued messages
parser.add_argument("-r", "--reprocess", dest="process_queue", action="store_true", help="Try to reprocess queued messages now")
# List all current mail queues
parser.add_argument("-l", "--list", dest="list_queues", action="store_true", help="List all the current mail queues")
# Displays the message
parser.add_argument("-m", "--message", dest="display_message", action="store_true", help="Displays the message")           
# Display only the message IDs
parser.add_argument("-N", dest="display_message_ID", action="store_true", help="Displays only the message IDs")    
# Purge messages
parser.add_argument("-P", dest="purge_messages", action="store_true", help="Purge all messages from the mail queue. Options: hold|incoming|active|deferred")    
# Display stats
parser.add_argument("-s", "--stats", dest="display_stats", action="store_true", help="Display the mail queue statistics")   
# Delete messages with subject
parser.add_argument("-S", "--subject", dest="select_subject", action="store_true", help="Delete mail with this subject. Options: \"$subjectname\"") 

args = parser.parse_args()

if __name__ == '__main__':

    if args.active_queue:
        print "test"
 