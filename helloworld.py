#Andrew Hendricks
#creates a networktable, then publishes data to the table each second

from networktables import NetworkTable
from time import sleep

nt = NetworkTable.getTable("VISION")
bob = 0

while True:
    sleep(1.0) #waits 1 second then increments 'bob'
    bob += 1
    nt.putNumber('time',bob) #publish values to the table
