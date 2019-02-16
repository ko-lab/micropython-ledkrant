def alleletters(letter):
    letters = {}
    letters['A'] = [2,5,7,5,5]
    letters['B'] = [6,5,6,5,6]
    letters['C'] = [3,4,4,4,3]
    letters['D'] = [6,5,5,5,6]
    letters['E'] = [7,4,6,4,7]
    letters['F'] = [7,4,6,4,4]
    letters['G'] = [7,4,7,5,7]
    letters['H'] = [5,5,7,5,5]
    letters['I'] = [7,2,2,2,7]
    letters['J'] = [7,1,1,5,6]
    letters['K'] = [5,5,6,5,5]
    letters['L'] = [4,4,4,4,7]
    letters['M'] = [5,7,7,5,5]
    letters['N'] = [5,7,7,7,5]
    letters['O'] = [2,5,5,5,2]
    letters['P'] = [7,5,7,4,4]
    letters['Q'] = [7,5,5,7,3]
    letters['R'] = [7,5,6,5,5]
    letters['S'] = [7,4,7,1,7]
    letters['T'] = [7,2,2,2,2]
    letters['U'] = [5,5,5,5,7]
    letters['V'] = [5,5,3,3,1]
    letters['W'] = [5,5,7,7,5]
    letters['X'] = [5,5,2,5,5]
    letters['Y'] = [5,5,7,2,2]
    letters['Z'] = [7,1,2,4,7]
    letters['0'] = [7,5,5,5,7]
    letters['1'] = [6,2,2,2,7]
    letters['2'] = [7,1,7,4,7]
    letters['3'] = [7,1,3,1,7]
    letters['4'] = [5,5,7,1,1]
    letters['5'] = [7,4,7,1,7]
    letters['6'] = [7,4,7,5,7]
    letters['7'] = [7,1,3,1,1]
    letters['8'] = [7,5,7,5,7]
    letters['9'] = [7,5,7,1,1]
    letters['?'] = [5,1,2,0,2]
    letters['!'] = [2,2,2,0,2]
    letters['+'] = [0,0,2,7,2]
    letters['-'] = [0,0,7,0,0]
    letters['('] = [3,4,4,4,3]
    letters[')'] = [6,1,1,1,6]
    letters['['] = [6,4,4,4,6]
    letters[']'] = [3,1,1,1,3]
    letters['%'] = [5,1,2,4,5]
    letters['#'] = [5,7,5,7,5]
    letters[' '] = [0,0,0,0,0]
    return letters[letter]

def zfill(s, width):
    if len(s) < width:
        return ("0" * (width - len(s))) + s
    else:
        return s

def binletter(letter,line):
    return zfill(bin(alleletters(letter)[line])[2:],3)
