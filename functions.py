def dectobin(number):
    result = []
    numbconv = ''
    while number >= 1:
        result.append(str(number % 2))
        number = number // 2
    result.reverse()
    for item in result:
        numbconv += item
    return numbconv

def dectooct(number):
    result = []
    numbconv = ''
    while number >= 1:
        result.append(str(number % 8))
        number = number // 8
    result.reverse()
    for item in result:
        numbconv += item
    return numbconv

def dectohex(number):
    result = []
    numbconv = ''
    while number >= 1:
        if number % 16 == 10:
            result.append('A')
        elif number % 16 == 11:
            result.append('B')
        elif number % 16 == 12:
            result.append('C')
        elif number % 16 == 13:
            result.append('D')
        elif number % 16 == 14:
            result.append('E')
        elif number % 16 == 15:
            result.append('F')
        else:
            result.append(str(number % 16))
        number = number // 16
    result.reverse()
    for item in result:
        numbconv += item
    return numbconv
    
def bintodec(number):
    numbconv = 0
    number = str(number)
    for i in range(len(number)):
        numbconv += (2**i)* int(number[-(i+1)])
    return numbconv

def bintooct(number):
    dec = binfordec(number)
    numbconv = decforoct(dec)
    return numbconv

def bintohex(number):
    dec = binfordec(number)
    numbconv = decforhex(dec)
    return numbconv

def octtodec(number):
    numbconv = 0
    number = str(number)
    for i in range(len(number)):
        numbconv += (8**i)* int(number[-(i+1)])
    return numbconv

def octtobin(number):
    dec = octfordec(number)
    numbconv = decforbin(dec)
    return numbconv

def octtohex(number):
    dec = octfordec(number)
    numbconv = decforhex(dec)
    return numbconv
#usar numero como string em numeros hexadecimais pois da erro de sintaxe se é escrito sem aspas
def hextodec(number):
    numbconv = 0
    number = str(number)
    for i in range(len(number)):
        if number[-(i+1)] == 'A':
            numbconv += (16**i) * 10
        elif number[-(i+1)] == 'B':
            numbconv += (16**i) * 11
        elif number[-(i+1)] == 'C':
            numbconv += (16**i) * 12
        elif number[-(i+1)] == 'D':
            numbconv += (16**i) * 13
        elif number[-(i+1)] == 'E':
            numbconv += (16**i) * 14
        elif number[-(i+1)] == 'F':
            numbconv += (16**i) * 15
        else:
            numbconv += (16**i)* int(number[-(i+1)])
    return numbconv

def hextobin(number):
    dec = hexfordec(number)
    numbconv = decforbin(dec)
    return numbconv

def hextooct(number):
    dec = hexfordec(number)
    numbconf = decforoct(dec)
    return numbconf
