#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import vxi11
import time
import csv
import numpy

input_chan = "3"
StartFrequency = 0.1
StopFrequency = 15.0
npoints = 100
Amplitude = 1


inst = vxi11.Instrument("TCPIP::192.168.178.31::INSTR")
print(inst.ask("*IDN?"))
inst.clear()
inst.write("*RST")
time.sleep(2)
inst.write("SYSTem:DISPlay:UPDate ON")
inst.write("CHANnel"+input_chan+":RANGe "+str(round(Amplitude*2)))
inst.write("STOP")
inst.write("WGENerator1:PRESet")
inst.write("CHANnel1:STATe OFF")
inst.write("CHANnel"+input_chan+":STATe ON")
inst.write("MEASurement1:MAIN PDELta")
inst.write("MEASurement1:ENABle")
inst.write("MEASurement1:SOURce C"+input_chan)

inst.write("WGENerator1:VOLTage:VPP "+str(Amplitude))
inst.write("WGENerator1:ENABle ON")

timestr = time.strftime("%Y%m%d-%H%M%S_")
with open('csv/'+timestr+'MXO44vsOldPreamp', mode='w') as csv_file:
    fieldnames = ['freq', 'Vppin', 'Vppout']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for f in numpy.geomspace(StartFrequency, StopFrequency, num=npoints):
        print("Testing at frequency "+str(round(f,2))+" Hz")
        inst.write("TIMebase:SCALe "+str(round(1.0/f/5.0)))
        inst.write("WGENerator1:FREQuency "+str(f))
        time.sleep(5)
        inst.write("RUNSingle")
        print(int(inst.ask("ACQuire:AVAilable?"))<1)
        while (int(inst.ask("ACQuire:AVAilable?"))<1):
            time.sleep(1)
            print ("Tick")

        print("Measured "+inst.ask("MEASurement1:RESult:ACTual")+" Vpp")
