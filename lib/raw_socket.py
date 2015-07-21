#!/usr/bin/env python

import os
import socket
import sys

class SocketError(Exception):
    pass

class RawSocket(socket.socket):
    FAMILY = socket.AF_INET
    FAMILY_INET = socket.AF_INET
    FAMILY_INET6 = socket.AF_INET6
    FAMILY_UNIX = socket.AF_UNIX
    
    def __init__(self, **kwargs):
        self.family = kwargs.setdefault('family', self.FAMILY)

        if not self.family in (self.FAMILY_INET, self.FAMILY_INET6, self.FAMILY_UNIX):
            raise SocketError('family must be INET, INET6 or UNIX')

        socket.socket.__init__(self, self.family, socket.SOCK_RAW, socket.IPPROTO_IP)
