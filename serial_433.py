from rpi_rf import RFDevice
import time

rfdevice = RFDevice(26)  # GPIO utilisé
rfdevice.enable_rx()
print("Récepteur actif")
timestamp = None

try:
    while True:
        if rfdevice.rx_code_timestamp != timestamp:
            timestamp = rfdevice.rx_code_timestamp
            print("Signal reçu: {}".format(rfdevice.rx_code))
        time.sleep(0.01)
except KeyboardInterrupt:
    rfdevice.cleanup()
