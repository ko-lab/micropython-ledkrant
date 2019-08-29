# LED-Krant

## Setup

To install the required micropython libraries before fist use, use the WebREPL to log into the ledkrant, then run

```python
import upip
upip.install('micropython-umqtt.simple')
upip.install('micropython-umqtt.robust')
```

Create a file `webrepl_cfg.py` that contains

```
PASS = '[YOURPASSWORD]'
```

Create a file 'config.py' that contains the login for the 
ko-lab wifi and the LED-floor PI (which also runs the MQTT broker)

```
mqtt_server =	{
  "ip": '10.94.176.100',
  "user": 'USERNAME',
  "password": 'PASSWORD'
}

wifi = {
    "ssid": 'ko-lab-net',
    "password": 'PASSWORD'
}
```

## Misc

If the webrepl is not reacting to type input, comment out the call to `mqtt.run()` in `main.py`, then upload the file and restart the wemos.

To reload the module after making changes, without having to restart the wemos, run:
`import sys; del sys.modules['mqtt_listener']; del sys.modules['wsled']; import mqtt_listener; mqtt_listener.run()`


