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
    numbconv = eval('0b' + number)
    return numbconv

def binforoct(number):
    dec = eval('0b' + number)
    numbconv = decforoct(dec)
    return numbconv

def binforhex(number):
    dec = eval('0b' + number)
    numbconv = decforhex(dec)
    return numbconv

def octfordec(number):
    numbconv = eval('0o' + number)
    return numbconv

def octforbin(number):
    dec = decforbin('0o' + number)
    numbconv = decforbin(dec)
    return numbconv

def octforhex(number):
    dec = eval('0o' + number)
    numbconv = devforhex(dec)
    return numbconv

def hexfordec(number):
    numbconv = eval('0x' + number)
    return numbconv

def hexforbin(number):
    dec = eval('0x' + number)
    numbconv = decforbin(dec)
    return numbconv

def hexforoct(number):
    dec = eval('0x' +number)
    numbconf = decforoct(dec)
    return numbconf
