# LED-Krant

## Setup

To install the required micropython libraries before fist use, use the WebREPL to log into the ledkrant, then run

```python
import upip
upip.install('micropython-umqtt.simple')
upip.install('micropython-umqtt.robust')
```

## Misc

If the webrepl is not reacting to type input, comment out the call to `mqtt.run()` in `main.py`, then upload the file and restart the wemos.

To reload the module after making changes, without having to restart the wemos, run:
`import sys; del sys.modules['mqtt_listener']; del sys.modules['wsled']; import mqtt_listener; mqtt_listener.run()`
