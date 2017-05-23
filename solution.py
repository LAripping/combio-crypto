#! /usr/bin/python

with open('file3-73415.txt.enc') as encfile:
    ciphertext = encfile.read()
print "Ciphertext read: (hex characters)"
print ciphertext.encode("hex")

with open('decrypted.txt') as decfile:
    plaintext = decfile.read()
print "\nPlaintext recovered:"
print plaintext

key = {}
i=0
while i<len(plaintext):
    key[ plaintext[i] ] = ciphertext[i].encode("hex")
    i += 1
print "\nKey used: {PTc : CTc-hex}"
print str(key)

restructured=""
for c in plaintext:
    restructured += key[c]
print "\nVERIFICATION:"
print "Re-ecrypting plaintext with suspected key: (hex characters)"
print ciphertext.encode("hex")

#row-index = plaintext char code
#row-value = ciphertext char code (that substitutes the plaintext char)

key_column = []
for i in range(256):
    try:
        value = int( key[ chr(i) ],16 )
    except KeyError:
        value = -1
    key_column.append(value)
print "\nKey column to be written in file:"
print str(key_column)

with open("keyfile.txt",'w') as keyfile:
    for elem in key_column:
        keyfile.write(str(elem)+'\n')


