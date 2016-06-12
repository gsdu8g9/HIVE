# ClaudiaMIND

### IRC hivemind DDoS tool

Basically a tool using which many people can attack a target specified using an IRC command.

# Disclaimer
**This tool is released for educational purposes only and comes with no warranty at all.**

**You may not use this software for any illegal or unethical purpose.**

# Getting the program & updating
* Getting the program: ```git clone https://github.com/ClaudiaDAnon/ClaudiaMIND.git```
* Updating the program: Make sure you're in the ClaudiaMIND directory, then ```git pull```

# Configuration
You can set your language in the configuration.conf file (ISO 639-1), as well as the minimum and maximum threads you want to attack using, whether you want to ping whenever the !ping command is received (default False, !ping doesn't run within Tor), and your native_ip to make the process of comparing it to your Tor IP shorter.

# Languages
These languages are currently supported:
* en
* cs

# Usage

```$ python claudiamind.py```

Port: 9050 for the ```service tor``` and 9150 for the Tor browser (and therefore works on Windows)

Simply: If you're running Windows, start the Tor browser and type 9150 into the port column. If you're running linux, download tor if not installed (```sudo apt-get install tor```), make sure the service is running (```sudo service tor start```) and either enter 9050 or nothing (9050 is default).
**Alternatively, you can use the Tor browser port (9150) on Linux too.**
*Protip: On Linux, you can run both the Tor browser and the service.*

# Argparse
You can also use -p for specifying the socks5 port. And -v for displaying the version.
```
$ ./claudiamind.py -h
$ ./claudiamind.py -p 9050
```

# Reporting policy
The script compares your IP to the Tor IP to make sure you're using Tor, and then sends me or any OP who requested it your **TOR IP**, only for statistical purposes and easier bugfixing. **Again, don't worry, that is not your real IP address.**.

It also sends me the version of your script, so I can tell some people to update it, etc.

# Tor routing
The *claudiashammer* module will say "Tor: False" - the module is indeed run without Tor, **but** this is because *claudiamind.py* already routes all of its traffic through Tor, including its modules' traffic. So even though *claudiashammer* says "Tor: False", it all goes through Tor.

# Using the program on multiple ports
Assuming you're in the ClaudiaMIND directory, just do this:
```
$ chmod +x claudia*
$ cd tor
$ chmod +x generate.py
$ ./generate.py
```
Now enter the amount of Tor ports you want
```
$ chmod +x torstart.sh
$ ./torstart.sh
```
Now, leave this window open and in another one, run claudiamind with one of the printed ports. (Obviously all of the ports. Ideally like 4 clients on the same port)

# Known issues
* Some nicknames cause problems with connecting
