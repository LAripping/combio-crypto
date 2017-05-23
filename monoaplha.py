#! /usr/bin/python

from collections import Counter

def table(counter, n=10):
    total = sum(counter.values())
    for gram, fr in counter.most_common(n):
        pct = float(fr) / total * 100
        line = '%02s : %04.1f %%: ' % (gram, pct)
        for i in range(fr):
            line += '|'
        print line

def all_n_grams(n=2):
    ngrams_found = Counter()

    whitespace = []
    for k,v in key.items():
        if v==' ' or v=='.':
            whitespace.append(k)

    for j in range(len(ciphertext)-n*2):
        gram = ciphertext[j:j+n*2]

        # Don't count ngrams containing space or dot
        if len(whitespace)>0 and whitespace[0] in gram \
        or len(whitespace)>1 and whitespace[1] in gram:
            continue
        ngrams_found[ gram ] += 1

    return ngrams_found

def decrypt():
    """Given a key and a ciphertext,
    it prints the resulting plaintext with capitals"""
    plaintext = ""
    i = 0
    while i < len(ciphertext):
        if i%2==1:
            try:
                plaintext += key[ ciphertext[i-1]+ciphertext[i]  ]
            except KeyError:
                plaintext += ciphertext[i-1]+ciphertext[i]
        i += 1
    return plaintext

def pad(ciphertext, sep='x'):
    text_padded = ""
    i = 0
    for c in ciphertext:
        text_padded += c if i%2 else 'x'+c
        i += 1
    return text_padded


def word_starters():
    """Supposing the space character has been decrypted, use this as a
    separator in ciphertext to find the frequencies of word starting
    letters"""
    space = ''
    for k,v in key.items():
        if v==' ':
            space = k

    starters = Counter()
    for word in ciphertext.split( space ):
       first_two = word[0]+word[1]
       starters[first_two] += 1

    return starters

def word_enders():
    """Supposing the space character has been decrypted, use this as a
    separator in ciphertext to find the frequencies of word ending
    letters"""
    space = ''
    for k,v in key.items():
        if v==' ':
            space = k

    enders = Counter()
    for word in ciphertext.split( space ):
       last_two = word[-2]+word[-1]
       enders[last_two] += 1

    return enders

def doubles():
    doubles = Counter()

    c=""
    i = 0
    while i < len(ciphertext)-2:
        if i%2==1:
            c = ciphertext[i-1]+ciphertext[i]
            if c==ciphertext[i+1]+ciphertext[i+2]:
                doubles[c]+=1
                i += 2
        i+=1
    return doubles

#### Script

cipher_freqs = Counter()
ciphertext = ''                         # 11245a
key = {}
# Fill incrementally e.g. {'cf':' ', '19':'E'}
with open('file3-73415.txt.enc') as encfile:
    while True:
        c = encfile.read(1)
        if not c:
            break
        ciphertext += c.encode("hex")
        cipher_freqs[c.encode("hex")] += 1

ciphertext_padded =  pad(ciphertext)    # x11x24x5a...


print """ Usage:
n=10
print str(n)+' Most Frequent singles'
table( all_n_grams(1),n)

print str(n)+' Most Frequent digrams'
table( all_n_grams(2),n )

print str(n)+' Most Frequent 3grams'
table( all_n_grams(3),n )

print str(n)+' Most Frequent 4grams'
table( all_n_grams(4),n )

# Following methods available only  after finding space character

print str(n)+' Most Frequent word starting letters'
table( word_starters(),n )

print str(n)+' Most Frequent word ending letters'
table( word_enders(),n )

print str(n)+' Most Frequent doubles'
table( doubles(),n )
"""
