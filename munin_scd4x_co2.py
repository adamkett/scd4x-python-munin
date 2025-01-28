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
        print("graph_title co2 ppm")
        print("graph yes")
        #print("graph_args --base 2500 -l 400")
        #print("graph_scale no")
        print("graph_category environmental")
        print("graph_info CO2 PPM.")
        print("graph_vlabel co2.")
        print("co2.label co2")
        print("co2.warning 1500")
        print("co2.critical 2000")
        exit()

try:
    co2, temperature, relative_humidity, timestamp = device.measure()
    print(f"co2.value {co2:.2f}")
except KeyboardInterrupt:
    pass

exit()
