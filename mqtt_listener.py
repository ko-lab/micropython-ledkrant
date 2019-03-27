from umqtt.robust import MQTTClient
from wsled import scrolltextng, writetext, wissen, party
from time import sleep
import machine
import ure
from config import mqtt_server

BRIGHTNESS = 0 # using warm white for brightness
BG_COLOR = [0, 0, 0]
TEXT_COLOR = [20, 230, 220]

def show_default():
    """ the default, shown when no other command is running """
    text = '  Ko-Lab'
    wissen(BG_COLOR[0], BG_COLOR[1], BG_COLOR[2], BRIGHTNESS)
    writetext(text, TEXT_COLOR[0], TEXT_COLOR[1], TEXT_COLOR[2], BRIGHTNESS)


def clamp(i, low=0, high=255):
    """ limits integer i to range [low, high] """
    return min(max(i, low), high)


def parse_color_string(s):
    """ tries to parse a string as rgb or hex color code, returns [r, g, b] tuple if 
    succesful, False otherwise """
    rgb = [0, 0, 0]
    try:
        # try to parse string as rgb color
        col = ure.match('[rgb\\(]*([0-9]+)[, ]+([0-9]+)[, ]+([0-9]+)\\)', s)
        rgb[0] = clamp(int(col.group(1)))
        rgb[1] = clamp(int(col.group(2)))
        rgb[2] = clamp(int(col.group(3)))
    except:
        try:
            # try to parse string as #hexhexhex color code
            col = ure.match('#([0-9a-f][0-9a-f])([0-9a-f][0-9a-f])([0-9a-f][0-9a-f])', s) 
            rgb[0] = clamp(int(col.group(1), 16))
            rgb[1] = clamp(int(col.group(2), 16))
            rgb[2] = clamp(int(col.group(3), 16))
        except:
            print(s + " is not a valid color code.")
            return False

    return rgb


def sub_callback(topic, msg):
    """ processes messages from all subscribed topics """
    global BRIGHTNESS
    global BG_COLOR
    global TEXT_COLOR

    print((topic, msg))

    if topic == b"ledkrant/write":
        # Show attention grabbing signal, then scroll text provided in msg 
        # from kolabbot (via `/krant [text]` command)
        for i in range(3):
            wissen(0, 0, 0, 0)
            sleep(0.3)
            writetext("   + + +", 255, 0, 0, 40)
            sleep(0.3)
        wissen(0, 0, 0, 0)

        for i in range(3):
            scrolltextng(str(msg, 'ascii'), 
                TEXT_COLOR[0], TEXT_COLOR[1], TEXT_COLOR[2], BRIGHTNESS,
                BG_COLOR[0], BG_COLOR[1], BG_COLOR[2], BRIGHTNESS)

    elif topic == b"ledkrant/time":
        # Shows text in purple, the time is provided in a message from kolabbot
        try:
            text = str(msg, 'ascii')
            wissen(0, 0, 0, 0)
            writetext("   " + text, 148, 0, 211, 40)
            sleep(10)
        except:
            pass

    elif topic == b"ledkrant/brightness":
        # change brightness of default image
        try:
            BRIGHTNESS = clamp(int(msg))
        except:
            pass

    elif topic == b"ledkrant/color":
        # change color of default image

        rgb = parse_color_string(msg)
        if(rgb):
            BG_COLOR[0] = rgb[0]
            BG_COLOR[1] = rgb[1]
            BG_COLOR[2] = rgb[2]

    elif topic == b"ledkrant/textcolor":
        # change color of default text
        rgb = parse_color_string(msg)
        if(rgb):
            TEXT_COLOR[0] = rgb[0]
            TEXT_COLOR[1] = rgb[1]
            TEXT_COLOR[2] = rgb[2]

    elif topic == b"ledkrant/party":
        # change color of default text
        party(duration = 10)

    elif topic == b"ledkrant/reset":
        # restart the ledkrant (for convenience, e.g. after uploading new code)
        print('restarting...')
        wissen(0, 0, 0, 0)
        writetext("    Bye!", 0, 0, 60, 60)
        sleep(2)
        wissen(0, 0, 0, 0)
        machine.reset()

    show_default()


def run():
    sleep(4)
    show_default()

    c = MQTTClient('ledkrant', 
        mqtt_server["ip"], 
        user=mqtt_server["user"], 
        password=mqtt_server["password"])

    c.DEBUG = True
    c.set_callback(sub_callback)
    c.connect()
    c.subscribe(b"ledkrant/write")
    c.subscribe(b"ledkrant/time")
    c.subscribe(b"ledkrant/brightness")
    c.subscribe(b"ledkrant/reset")
    c.subscribe(b"ledkrant/color")
    c.subscribe(b"ledkrant/textcolor")
    c.subscribe(b"ledkrant/party")

    while 1:
        c.wait_msg()

    c.disconnect()