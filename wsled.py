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
        idx = 0
        for val in letters.alleletters(letter):
            charpostmp = charpos
            for j in val:
                if j == '1':
                    np[7-idx][charpostmp] = (r,g,b,ww)
                    np[7-idx].write()
                charpostmp = charpostmp + 1
            idx = idx + 1
        charpos = charpos + 4
            
def scrolltextng(woord,r,g,b,ww):
    woordupper = woord.upper()
    beeld = []
    for i in range(5):
        beeld.append([])
    for letter in "             " + woordupper + " ":
        idx = 0
        for val in letters.alleletters(letter):
            for j in val:
                beeld[idx].append(j)
            idx = idx + 1
        for i in range(5):
            beeld[i].append(0)
    for k in range(0,len(beeld[1]),4):
        wissenzonderupdate(0,0,0,0)
        for i in range(5):
            idx = 0
            for j in beeld[i][0+k:42+k]:
                if j == '1':
                    np[7-i][idx] = (r,g,b,ww)
                idx = idx + 1
        for l in range(8):
            np[l].write()
