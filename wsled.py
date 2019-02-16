import machine, neopixel
import letters
np = [0,1,2,3,4,5,6,7]
np[0] = neopixel.NeoPixel(machine.Pin(5), 42, bpp=4)
np[1] = neopixel.NeoPixel(machine.Pin(4), 42, bpp=4)
np[2] = neopixel.NeoPixel(machine.Pin(0), 42, bpp=4)
np[3] = neopixel.NeoPixel(machine.Pin(2), 42, bpp=4)
np[4] = neopixel.NeoPixel(machine.Pin(14), 42, bpp=4)
np[5] = neopixel.NeoPixel(machine.Pin(12), 42, bpp=4)
np[6] = neopixel.NeoPixel(machine.Pin(13), 42, bpp=4)
np[7] = neopixel.NeoPixel(machine.Pin(15), 42, bpp=4)

def party():
 while 1:
  for j in range(8):
    for i in range(42):
        np[j][i]=(0,0,0,255)
    np[j].write()
  for j in range(8):
    for i in range(42):
        np[j][i]=(0,0,255,0)
    np[j].write()
  for j in range(8):
    for i in range(42):
        np[j][i]=(0,255,0,0)
    np[j].write()
  for j in range(8):
    for i in range(42):
        np[j][i]=(255,0,0,0)
    np[j].write()
    
def kolab():
    for j in range(8):
        for i in range(42):
            np[j][i] = (0,0,0,0)
        np[j].write()
    for i in [35,31,28,27,21,15,14,11,10,9]:
        np[0][i] = (0,255,0,0)
        np[0].write()
    for i in [35,32,29,26,21,16,13,11,8]:
        np[1][i] = (0,255,0,0)
        np[1].write()
    for i in [35,33,29,26,21,16,13,11,8]:
        np[2][i] = (0,255,0,0)
        np[2].write()
    for i in [35,34,29,26,24,23,21,16,15,14,13,11,10,9]:
        np[3][i] = (0,255,0,0)
        np[3].write()
    for i in [35,33,29,26,21,16,13,11,8]:
        np[4][i] = (0,255,0,0)
        np[4].write()
    for i in [35,32,29,26,21,16,13,11,8]:
        np[5][i] = (0,255,0,0)
        np[5].write()
    for i in [35,31,28,27,21,20,19,18,16,13,11,10,9]:
        np[6][i] = (0,255,0,0)
        np[6].write()
        
def wissen(r,g,b,ww):
    for j in range(8):
        for i in range(42):
            np[j][i] = (r,g,b,ww)
        np[j].write()

def wissenzonderupdate(r,g,b,ww):
    for j in range(8):
        for i in range(42):
            np[j][i] = (r,g,b,ww)
        
def writetext(woord,r,g,b,ww):
    charpos = 0
    for letter in woord.upper():
        for i in range(5):
            charpostmp = charpos
            for j in letters.binletter(letter,i):
                if int(j):
                    np[7-i][charpostmp] = (r,g,b,ww)
                    np[7-i].write()
                charpostmp = charpostmp + 1
        charpos = charpos + 4

def scrolltext(woord,r,g,b,ww):
    if (len(woord)*4) < 42:
        writetext(woord,r,g,b,ww)
        return
    for k in range(0,len(woord)*4+1,2):
        wissenzonderupdate(0,0,0,0)
        charpos = 0 - k
        for letter in woord.upper():
            for i in range(5):
                charpostmp = charpos
                for j in letters.binletter(letter,i):
                    if int(j) and charpostmp >=0 and charpostmp < 42:
                        np[7-i][charpostmp] = (r,g,b,ww)
                    charpostmp = charpostmp + 1
            charpos = charpos + 4
        for l in range(8):
            np[l].write()
