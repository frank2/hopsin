#!/usr/bin/env python

import os
import sys
from . import ip

from paranoia.types import *
from paranoia.base.abstract.structure import Structure

class Flag(Bitfield):
    BITSPAN = 1

class TCPFlags(Structure.simple([
    ('ns', Flag)
    ,('cwr', Flag)
    ,('ece', Flag)
    ,('urg', Flag)
    ,('ack', Flag)
    ,('psh', Flag)
    ,('rst', Flag)
    ,('syn', Flag)
    ,('fin', Flag)])):
    ALIGNMENT = Structure.ALIGN_BIT
    
class TCPHeader(Structure):
    ALIGNMENT = 32
    
    STRUCT_DECLARATION = (
    ('source_port', Word)
    ,('dest_port', Word)
    ,('sequence', Dword)
    ,('ack', Qword)
    ,('data_offset', Bitfield, {'bitspan': 4})
    ,('reserved', Bitfield, {'bitspan': 3})
    ,('flags', TCPFlags)
    ,('window_size', Word))

class TCPSocket(ip.IPSocket):
    def __init__(self, **kwargs):
        ip.IPSocket.__init__(self, **kwargs)

        self.ip_header = kwargs.setdefault('ip_header', None)
