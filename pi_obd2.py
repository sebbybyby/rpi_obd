#! /usr/bin/python 
import serial;
import threading;
import time;
    

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0);
def get_response();
  while True:
    response = port.read(1000);
    if (response != "".encode("utf-8"))
      print(response);
    sleep(0.01);
    
t = threading.Thread(target=get_response);
t.start();

while True:
  string_to_send = input("> ") + "\r";
  port.write(string_to_send.encode("utf-8"));
  #response = port.read(1000);
  #print(response);
