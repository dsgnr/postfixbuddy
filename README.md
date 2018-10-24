## Postfix Buddy

PostfixBuddy is a recreation of pfHandle.perl but written in Python.

### Options

    -h, --help            show this help message and exit
    -l, --list            List all the current mail queues
    -p {active,bounce,corrupt,deferred,hold,incoming}, --purge {active,bounce,corrupt,deferred,hold,incoming}
                            Purge messages from specific queues.
    -c, --clean           Purge messages from all queues.
    -f, --flush           Flush mail queues
    -s SHOW_MESSAGE, --show SHOW_MESSAGE
                            Show message from queue ID
    -v, --version         show program's version number and exit

#### Listing statistics of queues

``` 
➜ ./postfixbuddy.py  -l
============== Mail Queue Summary ==============
Active Queue Count: 12
Bounce Queue Count: 0
Corrupt Queue Count: 0
Deferred Queue Count: 23
Hold Queue Count: 0
Incoming Queue Count: 198
```
#### Flushing mail queues
This forces Postfix to reprocess the mail queue.

```
➜ ./postfixbuddy.py -f
Flushed all queues!
```

#### Purging queues
It is possible to purge specific queues. To purge a single queue, specify the queue name after `-p`.

```
➜ ./postfixbuddy.py -p active
Do you really want to purge the active queue? (Y/N): Y
Purged all mail from the active queue!

➜ ./postfixbuddy.py -l
============== Mail Queue Summary ==============
Active Queue Count: 0
Bounce Queue Count: 0
Corrupt Queue Count: 0
Deferred Queue Count: 23
Hold Queue Count: 0
Incoming Queue Count: 198
```
#### Clean queues
This option allows you to purge all mail queues. This has been separated from the purge option to avoid accidental purging of all queues.

```
➜ ./postfixbuddy.py -c
Do you really want to purge ALL mail queues? (Y/N): Y
Purged all mail queues!

➜ ./postfixbuddy.py -l
============== Mail Queue Summary ==============
Active Queue Count: 0
Bounce Queue Count: 0
Corrupt Queue Count: 0
Deferred Queue Count: 0
Hold Queue Count: 0
Incoming Queue Count: 0
```

#### Viewing messages
It is possible to view specific mail based on their mailq IDs. 

```
➜  ./postfixbuddy.py -s 6CB161202AB
*** ENVELOPE RECORDS active/6CB161202AB ***
message_size:             398             206               1               0             398
message_arrival_time: Wed Oct 24 12:20:24 2018
create_time: Wed Oct 24 12:20:24 2018
named_attribute: rewrite_context=local
sender_fullname: root@web.domain.com
sender: root@localhost
*** MESSAGE CONTENTS active/6CB161202AB ***
Received: by localhost (Postfix, from userid 0)
	id 6CB161202AB; Wed, 24 Oct 2018 12:20:24 +0100 (BST)
To:username@example.com
Subject: Test mail from web
Message-Id: <20181024112024.6CB161202AB@localhost>
Date: Wed, 24 Oct 2018 12:20:24 +0100 (BST)
From: root@localhost (root@web.domain.com)

 Test mail from web via senmail

*** HEADER EXTRACTED active/6CB161202AB ***
original_recipient: username@example.com
recipient: username@example.com
*** MESSAGE FILE END active/6CB161202AB ***
```


