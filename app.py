import math

cypherText = open("Crypted/cypherText.txt", "r+")
cypherTextAsci = open("Crypted/cypherTextAsci.txt", "r+")
decryptedTextAsci = open("Decrypted/decryptedTextAsci.txt", "w")
decryptedText = open("Decrypted/decryptedText.txt", "w")
plainText = open("plainText.txt", "r")
plainTextToAsci = open("plainTextToAsci.txt", "w")

# to generate prime numers bad algorith
def prime(max):
    arr = []
    i = max
    while i > 0:
        compteur = 0
        j = i - 1
        while j > 1:
            if i % j == 0:
                break
            else:
                compteur = compteur + 1
            j = j - 1
        if compteur == i - 2:
            arr.append(i)

        i = i - 1
    return arr


# to generate prime numers better than prime1
def prime2(max):
    arr = []
    i = max
    while i > 0:
        compteur = 0

        j = 2
        while j < i:
            if i % j == 0:
                break
            else:
                compteur = compteur + 1
            j = j + 1
        if compteur == i - 2:
            arr.append(i)

        i = i - 1
    return arr


# compete an exiting list of prime numbers
def addToPrime(max, min, done):
    new = []
    i = max
    while i > min:
        compteur = 0
        j = i - 1
        while j > 1:
            if i % j == 0:
                break
            else:
                compteur = compteur + 1
            j = j - 1
        if compteur == i - 2:
            new.append(i)

        i = i - 1
    return new + done


def getAlphaOrBeta(p, g, a):
    return (pow(g, a) % p)

# get codAsci of string m

def toAsci(p):
    m = plainText.read()
    blanc = 0
    lengAsci = 0
    arr = None
    asci = []
    arr = list(m)
    for i in arr:
        # if ord(i) != 32 :

        lengAsci = lengAsci + len(str(ord(i)))
        asci.append(ord(i))

    lenp = len(str(p))
    strasci = ''.join(str(e) for e in asci)
    lenght = len(strasci)
    arrayasci = []
    j = 0
    while j < math.ceil(lenght / lenp):
        num = strasci[lenp * j:lenp * (j + 1)]
        j += 1
        temp = int(num)

        # print temp
        # print math.ceil(lenght / lenp)

        arrayasci.append(num)
        if temp >= p:
            j = 0
            lenp -= 1
            arrayasci = []
    if len(strasci) % lenp != 0:
        # print "lennnnnnp", lenp
        dif = len(strasci) % lenp
        end = strasci[-dif:]

        # print end
        toend = ""
        for k in range(0, lenp - dif):
            toend += "0"
        toend += end
        # print toend
        arrayasci.append(toend)

    arrayasci.append(str(lengAsci))
    plainTextToAsci.write(str(arrayasci))

    return arrayasci

# get the encrypted asci
def toEncrypt(p, alpha, b, beta):
    array = toAsci(p)
    # print "plain message =[ " + m + " ]"

    cypher = []
    for k in array:
        n = int(k)
        c = str((n * pow(alpha, b)) % p)

        cypher.append(c)

    cypherTextAsci.write(str(cypher))
    return crypted(cypher, p, beta)

# get the encrypted text
def crypted(cypher, p, beta):
    cph = ''.join(chr(int(e) % 256) for e in cypher)
    cypherText.write(str(cph))
    return toDecrypt(cypher, p, beta)


# decrypt from the encrypted asci to plain asci
def toDecrypt(cypher, p, beta):
    print cypher

    plain = []
    avg = 0
    for k in cypher:
        avg += len(k)

    length = round(float(avg) / len(cypher))
    # print length
    for k in cypher:
        element = int(k)
        m = (element * pow(beta, p - 1 - a) % p)

        if len(str(m)) != length:
            dif = length - len(str(m))
            temp = ""
            for j in range(0, int(dif)):
                temp += "0"

            temp += str(m)
            m = temp

        plain.append(str(m))

    decryptedTextAsci.write(str(plain))

    return tomessage(plain)

# get the plain text from the codAsci
def tomessage(array):
    print array
    last = array[-1]
    del array[-1]
    length = 0
    for k in array:
        length = length + len(k)

    if length != int(last):
        dif = length - int(last)
        element = array[-1]

        repair = list(element)
        for j in range(0, dif):
            del repair[0]
        array[-1] = "".join(e for e in repair)

        index = 0
        beforlist = ""
        for l in array:
            beforlist = beforlist + l

        toint = int(beforlist)
        newarr = list(str(toint))

        resultarr = []
        while index < int(last):

            fragment = ""
            # print index+1
            if index + 2 < int(last):
                if int(newarr[index] + newarr[index + 1] + newarr[index + 2]) > 256:
                    fragment = fragment + newarr[index] + newarr[index + 1]
                    resultarr.append(fragment)
                    index = index + 2
                else:
                    fragment = fragment + newarr[index] + newarr[index + 1] + newarr[index + 2]
                    resultarr.append(fragment)
                    index = index + 3
            else:
                fragment = fragment + newarr[index] + newarr[index + 1]
                resultarr.append(fragment)
                index = index + 2

        decrypted = ''.join(chr(int(e)) for e in resultarr)
        decryptedText.write(decrypted)

        return 0

    else:
        index = 0
        beforlist = ""
        for l in array:
            beforlist = beforlist + l

        toint = int(beforlist)
        newarr = list(str(toint))

        resultarr = []
        while index < int(last):

            fragment = ""

            if index + 2 < int(last):
                if int(newarr[index] + newarr[index + 1] + newarr[index + 2]) > 256:
                    fragment = fragment + newarr[index] + newarr[index + 1]
                    resultarr.append(fragment)
                    index = index + 2
                else:
                    fragment = fragment + newarr[index] + newarr[index + 1] + newarr[index + 2]
                    resultarr.append(fragment)
                    index = index + 3
            else:
                fragment = fragment + newarr[index] + newarr[index + 1]
                resultarr.append(fragment)
                index = index + 2

        decrypted = ''.join(chr(int(e)) for e in resultarr)
        decryptedText.write(decrypted)
        print "decrypted"
        print decrypted
        return 0


# p = 9973
# big prime number
p = 99991
# p = 1259

# a random number
g = 4513
# a=random(p-2,1)

# secret key
a = 9945

# m = 11
alpha = getAlphaOrBeta(p, g, a)

# secret key
b = 8935
beta = getAlphaOrBeta(p, g, b)


def algorithm(p, alpha, b, beta):
    return toEncrypt(p, alpha, b, beta)


algorithm(p, alpha, b, beta)

cypherText.close()
cypherTextAsci.close()
decryptedTextAsci.close()
decryptedText.close()
plainText.close()
plainTextToAsci.close()


