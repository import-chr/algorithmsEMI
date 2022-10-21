def getHashValue(word, sz):
    total = 0
    hashI = 0

    for i in range(len(word)):
        total += ord(word[i]) * (i + 1)
    
    hashI = total % sz

    return int(hashI)

def insertHash(word, ht, sz):
    idx = getHashValue(word, sz)
    ht[idx].append(word)

def findCad(word, ht, sz):
    hw = getHashValue(word, sz)

    for i in ht[hw]:
        if i == word:
            return True
    
    return False

tabelSize = 15
ht = [[] for i in range(tabelSize)]

insertHash("borrador", ht, tabelSize)
insertHash("impresora", ht, tabelSize)
insertHash("pluma", ht, tabelSize)
insertHash("cuaderno", ht, tabelSize)

print(ht)
print(f'buscando impresora... {findCad("impresora", ht, tabelSize)}')