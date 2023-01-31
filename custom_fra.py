#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import vxi11
inst = vix11.Instrument("TCPIP::192.168.178.31::INSTR")
print(instr.query_str('*IDN?'))

