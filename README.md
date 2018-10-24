## Postfix Buddy

PostfixBuddy is a recreation of pfHandle.perl but written in Python.

### Options

    -h, --help            show this help message and exit
    -l, --list            List all the current mail queues
    -p {active,bounce,corrupt,deferred,hold,incoming}, --purge {active,bounce,corrupt,deferred,hold,incoming}
                            Purge messages from specific queues.
    -d DELETE_MAIL, --delete DELETE_MAIL
                            Delete specific email based on mailq ID.
    -c, --clean           Purge messages from all queues.
    -H, --hold            Hold all mail queues.
    -r, --release         Release all mail queues from held state.
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

#### Deleting mail based on mailq ID

This option allows you to delete a specific email in the queue if you know the mailq ID.

```
➜  ./postfixbuddy.py -d 77A4D1203C2
Do you really want to delete mail 77A4D1203C2? (Y/N): Y
postsuper: 77A4D1203C2: removed
postsuper: Deleted: 1 message
Deleted mail 77A4D1203C2!
```

#### Putting mail queues on hold

It is possible to put mail queues on hold. Whilst queues are in a held state, no attempt will be made to deliver it.

Note:  while  mail is "on hold" it will not expire when its time in the queue exceeds the **maximal_queue_lifetime** or **bounce_queue_lifetime** setting. It becomes subject to expiration after it is released from "hold".

```
➜  ./postfixbuddy.py -H
All mail queues now on hold!
```

To release the queues from their held state, simply use the `-r` flag.

```
➜  ./postfixbuddy.py -r
Queues no longer in a held state!
```

#### Deleting mail by subject

It is possible to specify the subject name can be searched for and removed within all mailqueues. This is particularly good if a spam outbreak has occured and you know of some specific keywords that are found in all mail. If subjects contain multiple words, please wrap them in inverted commas.

```
➜  ./postfixbuddy.py -S "This is my subject"
Searching for mail with this subject in: /var/spool/postfix/active...
grep: mail: No such file or directory
Searching for mail with this subject in: /var/spool/postfix/bounce...
grep: mail: No such file or directory
Searching for mail with this subject in: /var/spool/postfix/corrupt...
grep: mail: No such file or directory
Searching for mail with this subject in: /var/spool/postfix/deferred...
grep: mail: No such file or directory
postsuper: 931A4120226: removed
postsuper: Deleted: 1 message
Searching for mail with this subject in: /var/spool/postfix/hold...
grep: mail: No such file or directory
Searching for mail with this subject in: /var/spool/postfix/incoming...
```

#### Deleting mail by address

It is possible to delete mail by entering the hostname, or full email address. There is no need to wrap the address. **All** mail queues will be searched.

```
➜  ./postfixbuddy.py -D example.com
postsuper: 8669112052B: removed
postsuper: Deleted: 1 message
```
