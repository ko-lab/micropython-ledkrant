# LED-Krant

## Setup

To install required micropython libraries, use the WebREPL to log into the ledkrant, then run

```python
import upip
upip.install('micropython-umqtt.simple')
upip.install('micropython-umqtt.robust')
```

If the webrepl is not reacting to type input, comment out the call to `mqtt.run()` in `main.py`, then upload the file and restart the wemos.

TO reload the modulae after making changes, without havin to restart the wemos, run:
`del sys.modules['mqtt_listener']; import mqtt_listener; mqtt_listener.run()`
