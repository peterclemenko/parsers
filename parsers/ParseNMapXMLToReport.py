import time
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser
from libnmap.objects import NmapService, NmapReport, NmapHost
from libnmap.reportjson import ReportDecoder, ReportEncoder

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("nmapxml")
args = parser.parse_args()


nmapXmlFile = args.nmapxml

f = open('nmapReport.txt', 'w')

nmap_report = NmapParser.parse_fromfile(nmapXmlFile)
for NmapHost in nmap_report.hosts:
    data = {}
    ip4 = NmapHost.ipv4
    ip6 = NmapHost.ipv6
    mac = NmapHost.mac
    services = NmapHost.services
    for serv in services:
            data = {}
            ip4 = NmapHost.ipv4
            ip6 = NmapHost.ipv6
            mac = NmapHost.mac
            port = serv.port
            proto = serv.protocol
            state = serv.state
            f.write(ip4 + ":" + str(port) + "/" + proto + '\n')  # python will convert \n to os.linesep

f.close()  # you can omit in most cases as the destructor will call it