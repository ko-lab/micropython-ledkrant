def alleletters(letter):
    letters = {}
    letters['A'] = ['010','101','111','101','101']
    letters['B'] = ['110','101','110','101','110']
    letters['C'] = ['011','100','100','100','011']
    letters['D'] = ['110','101','101','101','110']
    letters['E'] = ['111','100','110','100','111']
    letters['F'] = ['111','100','110','100','100']
    letters['G'] = ['111','100','111','101','111']
    letters['H'] = ['101','101','111','101','101']
    letters['I'] = ['111','010','010','010','111']
    letters['J'] = ['111','001','001','101','110']
    letters['K'] = ['101','101','110','101','101']
    letters['L'] = ['100','100','100','100','111']
    letters['M'] = ['101','111','111','101','101']
    letters['N'] = ['101','111','111','111','101']
    letters['O'] = ['010','101','101','101','010']
    letters['P'] = ['111','101','111','100','100']
    letters['Q'] = ['111','101','101','111','011']
    letters['R'] = ['111','101','110','101','101']
    letters['S'] = ['111','100','111','001','111']
    letters['T'] = ['111','010','010','010','010']
    letters['U'] = ['101','101','101','101','111']
    letters['V'] = ['101','101','011','011','001']
    letters['W'] = ['101','101','111','111','101']
    letters['X'] = ['101','101','010','101','101']
    letters['Y'] = ['101','101','111','010','010']
    letters['Z'] = ['111','001','010','100','111']
    letters['0'] = ['111','101','101','101','111']
    letters['1'] = ['110','010','010','010','111']
    letters['2'] = ['111','001','111','100','111']
    letters['3'] = ['111','001','011','001','111']
    letters['4'] = ['101','101','111','001','001']
    letters['5'] = ['111','100','111','001','111']
    letters['6'] = ['111','100','111','101','111']
    letters['7'] = ['111','001','011','001','001']
    letters['8'] = ['111','101','111','101','111']
    letters['9'] = ['111','101','111','001','001']
    letters['?'] = ['101','001','010','000','010']
    letters['!'] = ['010','010','010','000','010']
    letters['+'] = ['000','000','010','111','010']
    letters['-'] = ['000','000','111','000','000']
    letters['('] = ['011','100','100','100','011']
    letters[')'] = ['110','001','001','001','110']
    letters['['] = ['110','100','100','100','110']
    letters[']'] = ['011','001','001','001','011']
    letters['%'] = ['101','001','010','100','101']
    letters['#'] = ['101','111','101','111','101']
    letters[' '] = ['000','000','000','000','000']
    letters[':'] = ['000','010','000','010','000']
    
    return letters[letter]
