
def do_connect():
    from config import wifi
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(wifi["ssid"], wifi["password"])
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    
import webrepl
webrepl.start()
    

