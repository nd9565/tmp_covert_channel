# **tmp Covert Channel**

Name: Nisarg Kiritbhai Dave

RIT ID: nd9565

tmp Covert Channel Assignment

## **Description**

The system mainly consists of two python scripts:

* tmp_cc_sender.py
* tmp_cc_receiver.py

The *tmp_cc_sender.py* script will prompt the user to enter their message which they wish to send to the receiver. It will take this message, create a *.txt* file, with the name of the file being ASCII value of a character from the message, in the */tmp/DSR/* directory. Then, it will wait for the receiver to read this value. Example, a message *"hello"* will have the first file as */tmp/DSR/104.txt* since 104 is the ASCII value of "h". The script will create an empty directory (also named DSR), to mark the end of the communication.

The *tmp_cc_receiver.py* script will read the value from the *.txt* file created in the */tmp/DSR* directory. Once it reads the value, it will create a */tmp/DRD* directory to acknowledge it. The *tmp_cc_sender.py* will then prepare for sending the next character. The script will stop reading and print the decoded message once it notices the empty DSR directory, which is the mark for ending the communication.

## **How to Run?**

Before testing, please make sure that your */tmp* directory does not consist of any directory named *DSR* and/or *DRD*, else the scripts might not work.

If there are any of these directories present, type in the following command to remove them:

```raw
> rm -r /tmp/DSR
```

*Replace DSR with DRD in the above command to remove DRD directory*

To test the scripts in your local environment, follow these steps:

* First execute the *tmp_cc_sender.py* script. You can run the script by typing in the following command:

```raw
> python3 tmp_cc_sender.py
```

This will prompt you to enter your message. It will notify the user when the message is completely received by the receiver.

*NOTE 1:* You can enter message with special characters too. I haven't tested the maximum length of the message that my program can handle and you are free to test it.

*For example, here is a sample message which you can try: "Hello, Friend! E-Corp is ours."*

*NOTE 2:* The longer the message, the longer it will take to transmit. Since I have not kept any progress indicators, it might look like the program froze, but please have patience and wait till it finishes execution. Alternatively, you can try with a shorter message first to test the program.

* Without closing the *tmp_cc_sender.py* script, run *tmp_cc_receiver.py* script parallely. Type in the following command to do so:

```raw
> python3 tmp_cc_receiver.py
```

This will notify user that it is reading the message and will print out the complete message once it is done reading the entire message.