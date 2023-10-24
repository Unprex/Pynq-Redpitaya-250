#!/usr/local/share/pynq-venv/bin/python

from pynq import GPIO

# Set Op Amp Power
adc_power = GPIO(908, "out")
dac_power = GPIO(909, "out")

adc_power.write(1)
dac_power.write(1)

adc_power.release()
dac_power.release()
