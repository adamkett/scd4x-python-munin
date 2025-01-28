#!/usr/bin/env python3
# munin version https://github.com/pimoroni/scd4x-python/blob/main/examples/basic.py
from datetime import datetime, timezone
from scd4x import SCD4X
from sys import argv, exit

device = SCD4X(quiet=True)
device.start_periodic_measurement()

if len(argv) > 1:
    # Autoconfiguration
    if argv[1] == "config":
        print("graph_title temperature C")
        print("graph yes")
        print("graph_category environmental")
        print("graph_info temperature C.")
        print("graph_vlabel temperature.")
        print("temperature.label temperature")
        exit()

try:
    co2, temperature, relative_humidity, timestamp = device.measure()
    print(f"temperature.value {temperature:.4f}")
except KeyboardInterrupt:
    pass

exit()
