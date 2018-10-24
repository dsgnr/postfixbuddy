## Postfix Buddy

PostfixBuddy is a recreation of pfHandle.perl but written in Python.

### Options

    -h, --help            show this help message and exit
    -l, --list            List all the current mail queues
    -p {active,bounce,corrupt,deferred,hold,incoming}, --purge {active,bounce,corrupt,deferred,hold,incoming}
                            Purge all messages from the mail queue.
    -f, --flush           Flush mail queues
    -s SHOW_MESSAGE, --show SHOW_MESSAGE
                            Show message from queue ID
    -v, --version         show program's version number and exit

#### Listing statistics of queues

```python 
➜ ./postfixbuddy.py  -l
============== Mail Queue Summary ==============
Active Queue Count: 12
Bounce Queue Count: 0
Corrupt Queue Count: 0
Deferred Queue Count: 23
Hold Queue Count: 0
Incoming Queue Count: 198
```
