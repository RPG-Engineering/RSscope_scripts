#!/usr/bin/env python3
# -*- coding: utf-8 -*-


input_chan = "3"

import vxi11
inst = vxi11.Instrument("TCPIP::192.168.178.31::INSTR")
print(inst.ask("*IDN?"))
inst.clear()
inst.write("*RST")
inst.write("WGENerator1:PRESet")
inst.write("CHANnel1:STATe OFF")
inst.write("CHANnel"+input_chan+":STATe ON")