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
        np[j].fill((r,g,b,ww))


def writetext(woord,r,g,b,ww):
    charpos = 0
    for letter in woord.upper():
        idx = 0
        for val in letters.alleletters(letter):
            charpostmp = charpos
            for j in val:
                if j == '1':
                    row_idx = 7-(idx+1)
                    np[row_idx][charpostmp] = (r,g,b,ww)
                    np[row_idx].write()
                charpostmp = charpostmp + 1
            idx = idx + 1
        charpos = charpos + 4
            

def scrolltextng(woord, r, g, b, ww, r_bg=0, g_bg=0, b_bg=0, ww_bg=0):
    # initialize the 5 LED rows
    beeld = []
    for i in range(5):
        beeld.append([])
    
    # loop through all letters of the message, create a 2 dimensional 
    # array of 0s and 1s 
    message = (13*" ") + woord.upper() + " "
    for letter in message:
        idx = 0
        for val in letters.alleletters(letter):
            for j in val:
                beeld[idx].append(int(j))
            idx = idx + 1
        
        # add space (empty column) after each letter
        for i in range(5):
            beeld[i].append(0)

    # find indeces that must be colored. ALl others get the background color
    colored = []
    for row in range(5):
        colored.append([i for i, e in enumerate(beeld[row]) if e == 1])

    lettercolor = (r, g, b, ww)
    bgcolor = (r_bg, g_bg, b_bg, ww_bg)
    textwidth = len(beeld[1])

    wissenzonderupdate(r_bg, g_bg, b_bg, ww_bg)
    for row in range(8): 
        np[row].write()

    # Frame by frame, show letters on ledkrant
    for frame_left in range(0, textwidth, 1):
        frame_right = frame_left + 41

        for row in range(5): 
            row_idx = 7-(row+1)
            np[row_idx].fill(bgcolor)
            for pixel_idx in colored[row]:
                if pixel_idx >= frame_left and pixel_idx <= frame_right:
                    led_idx = pixel_idx - frame_left
                    np[row_idx][led_idx] = lettercolor
        
        # It should be enough to refresh the top 5 rows. 
        # the others dont change because the letters only take up 5 rows
        for row in range(5): 
            row_idx = 7-(row+1)
            np[row_idx].write()
