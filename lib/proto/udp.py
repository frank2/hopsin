#!/usr/bin/env python

import os
import sys
from . import ip

from paranoia.types import *
from paranoia.base.abstract.structure import Structure

UDPHeader = Structure.simple([
    ('source_port', Word)
    ,('dest_port', Word)
    ,('length', Word)
    ,('checksum', Word)])

UDPv4Header = Structure.simple([
    ('source_ip', Dword)
    ,('dest_ip', Dword)
    ,('zeroes', Byte, {'value': 0})
    ,('protocol', Byte, {'value': 0x11})
    ,('udp_length', Word)
    ,('udp_header', UDPHeader)])

UDPv6Header = Structure.simple([
    ('source_ip', Oword)
    ,('dest_ip', Oword)
    ,('udp_length', Dword)
    ,('zeroes', Bitfield, {'bitspan': 24})
    ,('next_header', Byte)
    ,('udp_header', UDPHeader)])
    
class UDPSocket(ip.IPSocket):
    pass
