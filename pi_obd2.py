#! /usr/bin/python 
import serial;
port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)
string_to_send = input("> ");
port.write(string_to_send.encode("utf-8"));
response = port.read();
print(response);
