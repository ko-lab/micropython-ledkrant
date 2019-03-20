from umqtt.robust import MQTTClient
from wsled import scrolltextng, writetext, wissen
from time import sleep
import machine
from config import mqtt_server

DEFAULT_BRIGHTNESS = 0

def show_default():
    # the default, shown when no other command is running
    default_text = '  Ko-Lab'
    wissen(0, 0, 0, DEFAULT_BRIGHTNESS)
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

    while 1:
        c.wait_msg()

    c.disconnect()