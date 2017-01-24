import time
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser
from libnmap.objects import NmapService, NmapReport, NmapHost
from libnmap.reportjson import ReportDecoder, ReportEncoder

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("nmapxml")
args = parser.parse_args()

ignoreFile = "ignore.txt"

try:
    fh = open(ignoreFile,'r')
except:
# if file does not exist, create it
    fh = open(ignoreFile,'w')

nmapXmlFile = args.nmapxml

f = open('nmapReport.txt', 'w')

with open(ignoreFile) as igf:
    ignorelist = igf.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
ignorelist = [x.strip() for x in ignorelist] 

nmap_report = NmapParser.parse_fromfile(nmapXmlFile)
for NmapHost in nmap_report.hosts:
    data = {}
    ip4 = NmapHost.ipv4
    ip6 = NmapHost.ipv6
    mac = NmapHost.mac
    if ip4:
        if(ip4 not in ignorelist):
            services = NmapHost.services
            for serv in services:
                data = {}
                ip4 = NmapHost.ipv4
                port = serv.port
                proto = serv.protocol
                state = serv.state
                f.write(ip4 + ":" + str(port) + "/" + proto + '\n')  # python will convert \n to os.linesep

    if ip6:
        if(ip6 not in ignorelist):
            services = NmapHost.services
            for serv in services:
                data = {}
                ip6 = NmapHost.ipv6
                port = serv.port
                proto = serv.protocol
                state = serv.state
                f.write(ip6 + ":" + str(port) + "/" + proto + '\n')  # python will convert \n to os.linesep

f.close()  # you can omit in most cases as the destructor will call it