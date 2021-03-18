# Simple DNS-Hijacking
[![Python3.x](https://img.shields.io/badge/python-3.x-FADA5E.svg?logo=python)](https://www.python.org/) [![PEP8](https://img.shields.io/badge/code%20style-pep8-red.svg)](https://www.python.org/dev/peps/pep-0008/)

A simple script DNS-Hijacking testing written in Python3.

## Setting up a DNS Proxy

**First Step** 

Before you can start using this tool, you must configure your machine to use a DNS nameserver and enable IP forwarding with the tool running on it. You have several options based on the operating system:

* **Linux** `echo 1 > /proc/sys/net/ipv4/ip_forward`, `iptables -A FORWARD -j ACCEPT`, and edit `/etc/resolv.conf` to include a line on the very top with your traffic analysis host.

* **MacOS** `sudo sysctl -w net.inet.ip.forwarding=1` and Open System Preferences and click on the Network icon. Select the active interface and fill in the DNS Server field. If you are using Airport then you will have to click on Advanced… button and edit DNS servers from there. Alternatively, you can edit `/etc/resolv.conf` and add a fake nameserver to the very top there.

### Disclaimer
- This tool is only for testing and educational purposes and can only be used where strict consent has been given. I am not responsible for any misuse or damage caused by this tool.

## Installation

```git clone https://github.com/CyberCommands/PyHijack.git```

```cd PyHijack/```

```sudo pip install -r requirements.txt```

**Run**

```sudo python3 hijack.py```
