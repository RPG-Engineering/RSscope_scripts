#!/usr/bin/env python3
# -*- coding: utf-8 -*-


input_chan = "3"
StartFrequency = "0.01"
StopFrequency = "15"
Time = 60*10
Amplitude = "1"

import vxi11
inst = vxi11.Instrument("TCPIP::192.168.178.31::INSTR")
print(inst.ask("*IDN?"))
inst.clear()
inst.write("*RST")
inst.write("WGENerator1:PRESet")
inst.write("CHANnel1:STATe OFF")
inst.write("CHANnel"+input_chan+":STATe ON")
inst.write("MEASurement1:MAIN PDELta")
inst.write("MEASurement1:ENABle")
inst.write("MEASurement1:SOURce C"+input_chan)

inst.write("WGENerator1:SWEep:STATe ON")
inst.write("WGENerator1:SWEep:FSTart "+StartFrequency)
inst.write("WGENerator1:SWEep:FEND "+StopFrequency)
inst.write("WGENerator<wg>:SWEep:TIME "+Time)
inst.write("WGENerator<wg>:VOLTage[:VPP] "+Amplitude)
inst.write("WGENerator<wg>[:ENABle] ON")





inst.write("TIMebase:SCALe 1")