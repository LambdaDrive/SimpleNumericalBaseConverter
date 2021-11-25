def decforbin(number):
    numbconv = print("{:b}".format(number))
    return numbconv

def decforoct(number):
    numbconv = print("{:o}".format(number))
    return numbconv

def decforhex(number):
    numbconv = print("{:X}".format(number))
    return numbconv
    
def binfordec(number):
    numbconv = eval('0b' + str(number))
    return numbconv

def binforoct(number):
    dec = eval('0b' + str(number))
    numbconv = decforoct(dec)
    return numbconv

def binforhex(number):
    dec = eval('0b' + str(number))
    numbconv = decforhex(dec)
    return numbconv

def octfordec(number):
    numbconv = eval('0o' + str(number))
    return numbconv

def octforbin(number):
    dec = eval('0o' + str(number))
    numbconv = decforbin(dec)
    return numbconv

def octforhex(number):
    dec = eval('0o' + str(number))
    numbconv = decforhex(dec)
    return numbconv
#usar input entre aspas para converter de hexadecimal para outras bases
def hexfordec(number):
    numbconv = eval('0x' + str(number))
    return numbconv

def hexforbin(number):
    dec = eval('0x' + str(number))
    numbconv = decforbin(dec)
    return numbconv

def hexforoct(number):
    dec = eval('0x' + str(number))
    numbconf = decforoct(dec)
    return numbconf
