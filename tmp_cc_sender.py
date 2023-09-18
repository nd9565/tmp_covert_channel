######################################
# Name: Nisarg Dave
# RIT ID: nd9565
# Sender code for "tmp covert channel"
######################################

import os
import time

print("Welcome to tmp covert channel!")
print("Enter the message that you wish to send: ")
msg = input(">> ")

print("Make sure you run the receiver script!")
print("Sending the message to the receiver...")

for i in range (len(msg)):
	# Check if Receiver has set /tmp/DRD directory or not.
	# If it is set, wait until the receiver removes it
	while True:
		if(os.path.exists("/tmp/DRD")):
			print("Waiting for Receiver to delete DRD...")
			time.sleep(3)
			continue
		else:
			break
	
	# Covert character is the ASCII value stored in the file name
	ascii = ord(msg[i])
	covert_file_name = str(ascii) + ".txt"
	
	# Execute the command to create this file
	cmd_create_covert_file = "mkdir /tmp/DSR && touch /tmp/DSR/" + covert_file_name 
	os.system(cmd_create_covert_file)
	print("Sent " + msg[i])
	
	# Now, wait for the receiver to read the data and create DRD directory
	while True:
		if(os.path.exists("tmp/DRD")):
			cmd_remove_covert_file = "rm -r /tmp/DSR"
			os.system(cmd_remove_covert_file)
			print("Deleted DSR, inside loop")
			print(msg[i] + " read by receiver...")
			break
		else:
			print("Waiting for Receiver to read " + msg[i])
			time.sleep(3)
			continue
	
# Finally, send the message to end the communication
# I did it by creating an empty directory
cmd_end_communication = "mkdir /tmp/DSR"
os.system(cmd_end_communication)

# Now, wait for the receiver to acknowledge this
while True:
	if(os.path_exists("tmp/DRD")):
		cmd_remove_directory = "rm -r /tmp/DSR"
		os.system(cmd_remove_directory)
		print("Deleted DSR")
		break
	else:
		print("Waiting for Receiver to acknowledge the end...")
		time.sleep(3)
		continue

print("Your secret message is sent successfully! Check the receiver output to see the message!")
