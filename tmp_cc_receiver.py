########################################
# Name: Nisarg Dave
# RIT ID: nd9565
# Receiver code for "tmp covert channel"
########################################

import os
import time

print("Reading message from the Sender...")

decoded_msg = ""

while True:
	# Check if both DRD and DSR are present
	# If present, then it means that Receiver should wait for Sender to delete DSR
	while True:
		if(os.path.exists("/tmp/DSR") and os.path.exists("/tmp/DRD")):
			print("Waiting for Sender to delete DSR...")
			time.sleep(3)
			continue
		else:
			break
	
	# Check if only DRD is present and DSR is absent
	# If it is, then it means that Sender is waiting for Receiver to delete DRD
	# Hence, delete the DRD
	if(os.path.exists("/tmp/DRD") and not os.path.exists("/tmp/DSR")):
		cmd_remove_DRD = "rm -r /tmp/DRD"
		os.system(cmd_remove_DRD)
		print("Deleted DRD...")
	
	# Check if only DSR is present and DRD is absent
	# If so, it means that Receiver should read the data
	if(os.path.exists("/tmp/DSR") and not os.path.exists("/tmp/DRD")):
		# Get ASCII value from the file name from the DSR/ directory
		files = os.listdir("/tmp/DSR/")
		# If directory is empty, then it means that the communication has ended
		if(len(files) == 0):
			cmd_create_DRD_end = "mkdir /tmp/DRD" # Create DRD to acknowledge this step
			os.system(cmd_create_DRD_end)
			break
		# Else, continue reading the message
		ascii_filename = files[0].split(".txt")[0] # Extracting ASCII value from filename
		covert_char = chr(int(ascii_filename)) # Converting ASCII value to respective character
		decoded_msg += covert_char
		print("Read " + covert_char)
		cmd_create_DRD = "mkdir /tmp/DRD" # Create DRD once the data is read
		os.system(cmd_create_DRD)
		print("Created DRD, inside loop")
	
	# Check if both DSR and DRD are absent
	# If so, then the receiver should wait for Sender to create DSR
	while True:
		if((not os.path.exists("/tmp/DSR")) and (not os.path.exists("/tmp/DRD"))):
			print("Waiting for Sender to create DSR...")
			time.sleep(3)
			continue
		else:
			break

# Now that we are out of loop, the complete message is received and we can print the message
# First, check whether DSR is deleted. If deleted, then delete DRD too.
while True:
	if(os.path.exists("/tmp/DSR")):
		print("Out of loop. Waiting for DSR to be deleted...")
		time.sleep(3)
		continue
	else:
		cmd_remove_DRD_end = "rm -r /tmp/DRD"
		os.system(cmd_remove_DRD_end)
		print("Deleted DRD, outside loop")
		break

# Now, communication has officially ended and decoded message can be printed
print("Message received!")
print("Decoded message = " + decoded_msg)
