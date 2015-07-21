#!/usr/bin/env python

import os
import sys

from paranoia.types import *
from paranoia.base.abstract.structure import Structure
from hopsin import raw_socket

# TODO class CIDRData(martinellis.CIDR, Dword)

class IPFlags(Structure.simple([
    ('reserved', Bitfield, {'bitspan': 1, 'value': 0})
    ,('df', Bitfield, {'bitspan': 1})
    ,('mf', Bitfield, {'bitspan': 1})])):
    ALIGNMENT = 1

IPv4Header = Structure.simple([
    ('version', Bitfield, {'bitspan': 4})
    ,('ihl', Bitfield, {'bitspan': 4})
    ,('dscp', Bitfield, {'bitspan': 6})
    ,('ecn', Bitfield, {'bitspan': 2})
    ,('total_length', Word)
    ,('identification', Word)
    ,('flags', IPFlags)
    ,('fragment_offset', Bitfield, {'bitspan': 13})
    ,('time_to_live', Byte)
    ,('protocol', Byte)
    ,('checksum', Word)
    ,('source_ip', Dword)
    ,('dest_ip', Dword)])

IPv6Header = Structure.simple([
    ('version', Bitfield, {'bitspan': 4})
    ,('traffic_class', Bitfield, {'bitspan': 8}) # for alignment's sake
    ,('flow_label', Bitfield, {'bitspan': 20})
    ,('payload_length', Word)
    ,('next_header', Byte)
    ,('hop_limit', Byte)
    ,('source_ip', Oword)
    ,('dest_ip', Oword)])

IPv6OptionHeader = Structure.simple([
    ('next_header', Byte)
    ,('header_length', Byte)])

IPv6RoutingHeader = Structure.simple([
    ('option', IPv6OptionHeader)
    ,('routing_type', Byte)
    ,('segments_left', Byte)])

IPv6FragmentHeader = Structure.simple([
    ('option', IPv6OptionHeader)
    ,('fragment_offset', Bitfield, {'bitspan': 13})
    ,('res', Bitfield, {'bitspan': 2})
    ,('m', Bitfield, {'bitspan': 1})
    ,('identification', Dword)])

class IPSocket(raw_socket.RawSocket):
    pass
