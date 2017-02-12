#! /usr/bin/python

from collections import Counter


"""Get all ciphertext chars and find their frequencies"""
cipher_freqs = {}
with open('file3-73415.txt.enc') as encfile:
    while True:
        c = encfile.read(1)
        if not c:
            break
        code = c.encode("hex")
        if code in cipher_freqs.keys():
            cipher_freqs[code] += 1
        else:
            cipher_freqs[code] = 1

print 'Ciphertext code frequencies:'
for cd, fr in cipher_freqs.items():
    line = '%02s : ' % (cd)
    for i in range(fr):
        line += '|'
    print line



