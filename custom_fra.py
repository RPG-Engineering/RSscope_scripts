#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import vxi11
inst = vxi11.Instrument("TCPIP::192.168.178.31::INSTR")
print(inst.ask("*IDN?"))
inst.clear()
#inst.write("RESET")
