from umqtt.robust import MQTTClient
from wsled import scrolltextng, writetext, wissen
from time import sleep
import machine
import ure
from config import mqtt_server

DEFAULT_BRIGHTNESS = 0
DEFAULT_COLOR = [0, 0, 0]

def show_default():
    # the default, shown when no other command is running
    default_text = '  Ko-Lab'
    wissen(DEFAULT_COLOR[0], DEFAULT_COLOR[1], DEFAULT_COLOR[2],
        DEFAULT_BRIGHTNESS)
    writetext(default_text, 40, 40, 0, 40)


def sub_callback(topic, msg):

    if topic == b"ledkrant/write":
        # Show attention grabbing signal, then scroll text provided in msg 
        # from kolabbot (via `/krant [text]` command)
        for i in range(3):
            wissen(0, 0, 0, 0)
            sleep(1)
            writetext("   + + +", 255, 0, 0, 40)
            sleep(1)

        for i in range(3):
            wissen(0, 0, 0, 0)
            scrolltextng(str(msg, 'ascii'), 40, 40, 0, 40)
    
    elif topic == b"ledkrant/time":
        # Shows text in purple, the time is provided in a message from kolabbot
        wissen(0, 0, 0, 0)
        writetext("   " + str(msg, 'ascii'), 148, 0, 211, 40)
        sleep(10)

    elif topic == b"ledkrant/brightness":
        # change brightness of default image
        global DEFAULT_BRIGHTNESS
        DEFAULT_BRIGHTNESS = int(msg)

    elif topic == b"ledkrant/color":
        # change color of default image
        # TODO: refactor this try except mess
        print(msg)
        global DEFAULT_COLOR
        try:
            # try to parse as rgb
            col = ure.match('[rgb\\(]*([0-9]+)[, ]+([0-9]+)[, ]+([0-9]+)\\)', msg)
            r = int(col.group(1))
            g = int(col.group(2))
            b = int(col.group(3))
            DEFAULT_COLOR[0] = r
            DEFAULT_COLOR[1] = g
            DEFAULT_COLOR[2] = b
        except:
            try:
                # try to parse as hex
                col = ure.match('#([0-9a-f][0-9a-f])([0-9a-f][0-9a-f])([0-9a-f][0-9a-f])', msg) 
                r = int(col.group(1), 16)
                g = int(col.group(2), 16)
                b = int(col.group(3), 16)
                DEFAULT_COLOR[0] = r
                DEFAULT_COLOR[1] = g
                DEFAULT_COLOR[2] = b
            except:
                print("Not a valid color code.")

    elif topic == b"ledkrant/reset":
        # restart the ledkrant (for convenience, e.g. after uploading new code)
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

    while 1:
        c.wait_msg()

    c.disconnect()