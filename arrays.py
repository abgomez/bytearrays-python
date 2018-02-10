#! /bin/python

#Initialization

#test message to learn how to convert to bytes
message = "This is a test"
msgBytes = bytearray(message, 'utf-8')
print(msgBytes)

#construct header, header has package type and sequence number
packType = 0x20
seqNumber = 0x00
header = bytearray([packType, seqNumber])
print(header)

#create packet, concatenate header and message
packet = header+msgBytes
print "Print full package: %s" % packet
print "Print packet type: %c" % packet[0]
print "Print packet sequence: %x"  % packet[1]
print "Print packet Body: %s" % packet[2:len(packet)]

#now we want to duplicate the above logic, but this time we will use a text file.
#the text file will be split on 100bytes packages

#open file
inFile = open("declaration.txt", 'r')
text = inFile.read()
textArray = bytearray(text, 'utf-8')
#print(text)
textSize = len(textArray)
print "text size: %d" % textSize
#find out number of packets
numPcks = len(textArray)/100 
pckDic = {}
stIndex = 0
endIndex = 100
for packet in range(0, numPcks):
    if packet == 0:
        pckDic[seqNumber] = textArray[0:endIndex]
    else:
        pckDic[seqNumber] = textArray[stIndex:endIndex]
    seqNumber += 1
    #print seqNumber
    stIndex = endIndex
    #print stIndex
    endIndex += 100
    #print endIndex

#seqNumber += 1
#stIndex = endIndex
pckDic[seqNumber] = textArray[stIndex : len(textArray)]
#print (pckDic)
for key, value in pckDic.iteritems():
    print key, value
    #print "seq: %x, message: %s" % pck, pickDic[pck]
