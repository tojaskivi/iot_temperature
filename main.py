from network import WLAN      # library to connect to wifi
import urequests as requests  # sending data to ubidots
import machine                # basic functions used by the board 
import time                   # used to make the device sleep
import pycom                  # controlling the board, like onboard rgb

print("v 1.0.1")
pycom.heartbeat(False)
pycom.rgbled(0x999999)

TOKEN = "YOUR_UBIDOTS_TOKEN" #Put your ubidot token here
DELAY = 60 # How long between the measurements
send_limit = 10 # How often data should be sent to the cloud.
                # If delay is equal to 60 and send_limit is equal to 10, data will be sent every ten minutes
  
wlan = WLAN(mode=WLAN.STA)
wlan.antenna(WLAN.INT_ANT)

# Assign your Wi-Fi credentials
# This function connects to wifi
wlan.connect("your wifi SSID here", auth=(WLAN.WPA2, "your wifi password here"), timeout=5000)

while not wlan.isconnected ():
    machine.idle()
    # if wifi is not connected, the onboard led turns red to notify you that it can't reach the wifi
    pycom.rgbled(0xFF0000)
print("Connected to Wifi\n")

# Builds the json to send the request
def build_json(variable1, value1):
    try:
        data = {variable1: {"value": value1}}
        return data
    except:
        return None
      
# Sends the request. Please reference the REST API reference https://ubidots.com/docs/api/
# If the data is empty, don't send it
def post_var(device, value1):
    try:
        url = "https://industrial.api.ubidots.com/"
        url = url + "api/v1.6/devices/" + device
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        data = build_json("Temperature", value1)
        if data is not None:
            print(data)
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()
        else:
            pass
    except:
        pass

# function used to get the temperature
def get_temperature():

    # Analog to Digital Conversion
    adc = machine.ADC()

    # use pin 16 on the LoPy
    apin = adc.channel(pin='P16')

    # read the value from the sensor
    val = apin()

    # get the voltage
    millivolt = apin.voltage()
    
    # convert mV to celsius
    celsius = (millivolt-500)/10
    
    return celsius

# turn off the onboard led
pycom.rgbled(0x000000)

# defines variables
total_temperature = 0
counter = 0

# loop forever
while True:

    counter += 1
    print(counter)
    # save value from get_temperature()
    temperature = get_temperature()

    print(temperature)
    # add it so it is possible to get the average temperature
    total_temperature += temperature
    
    # when enough data is collected, send it to Ubidots
    if counter == send_limit:
        post_var("pycom", total_temperature/counter)
        print(total_temperature/counter)
        print(counter)
        counter = 0
        total_temperature = 0
    
    # device sleeps for DELAY seconds
    time.sleep(DELAY)
