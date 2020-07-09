---
title: Temperature to Cloud
tags: temperature, sensor, iot, pycom, lopy4, python, linux, ubuntu
description: Tutorial about sending data to the cloud via wifi.
---

# Data to cloud via WiFi
### a tutorial by to222ga

---

*DISCLAIMER:
This tutorial is made for Ubuntu users. The steps haven't been tested for Windows/Mac/other Linux distros. The actual code is the same for PC/Mac/Linux, but the **Getting Started** section is for Ubuntu.*

This tutorial will show you one way to send data to the cloud via WiFi, using MicroPython. The project will take about two hours, depending on how much you `ctrl+C -> ctrl+V`, or try to learn and code it yourself.

* Beginner :beginner:
* MicroPython :snake:
* LoPy4 :robot_face: 
* ~ 2 ± 1 hours :timer_clock: 
* WiFi :signal_strength:
* Linux :penguin: 

---

## Why?

I have a balcony facing south, so it get's blasted with sunshine from sunrise to sunset. If facing south wasn't enough, it has also windows so it is basically a 40&deg; oven. The fact that I have a cat means that I can't open the windows either. :cat::fire: 

The purpose of this project is to put a sensor on the balcony, which then alerts me when the temperature is below a certain value, so I can open the balcony door at the right time to cool down the apartment.

---

## Materials used :hammer: 

### Required

* You need a computer with at least one USB A-port.

|What?|Why?|Where?|:dollar:   |Note|
|-|-|-|-|-|
|LoPy4|The actual brain that does all the processing|[Pycom](https://pycom.io/product/lopy4/)|€35|*Other microcontrollers are ok, but it needs WiFi-support*
|3x jumper wires|Used to connect the LoPy4 to the sensor|[Ebay](https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=jumper+wire+breadboard+male+to+female&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=jumper+wire+breadboard+male+to+male)|~1€|*Make sure it's long enough. To connect the sensor directly to the board, you need male to female wires. If you use a breadboard you need male to male wires*|
|Temperature Sensor|Actually gathering data.|[Ebay](https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313.TR5.TRC1.A0.H0.Xtmp36.TRS0&_nkw=tmp36&_sacat=0)|~3€||
|Micro-USB Cable|Connecting the LoPy4 to the computer and powerbank|[Ebay](https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313.TR12.TRC2.A0.H0.Xmicro+usb+to+usb+cable.TRS0&_nkw=micro+usb+to+usb+cable&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=micro+usb+to+usb)|~2€|*You probably have one laying around at home*|
|Powerbank|To easily power the project without using an outlet|[Ebay](https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313.TR12.TRC2.A0.H0.Xpowerbank.TRS0&_nkw=powerbank&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=micro+usb+to+usb+cable)|~5€|**OPTIONAL** *Don't buy the absolute cheapest one. ***Safety first.*** I used a 1000 mAh battery which lasted for a day or so.*
|Breadboard|Makes it easy to connect everything when testing|[Ebay](https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313.TR2.TRC1.A0.H0.Xbreadboar.TRS0&_nkw=breadboard&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=tmp36)|<5€|**OPTIONAL**|

---

###### Sidenote: Ebay > Amazon; I :heart: Ebay; Ebay is life

---

## Getting started :timer_clock: 

*As stated in the beginning, this section is for Ubuntu-users.*

First you should always make sure that your LoPy4 is up to date. Get the latest firmware [here](https://software.pycom.io/downloads/linux-1.16.3.html). Follow the steps in the update-software.

When updating, you will be asked if you'd like to flash the device. **Flashing means resetting**. You should flash your device. Please note that any code already saved on the the device **will be lost**.

You need an IDE that supports Pymakr. Two good choices are

* [VS Code](https://code.visualstudio.com/) 
* [Atom](https://atom.io/)

There might be other IDEs but these two work great.

I chose VS Code, so it the following steps might differ a bit from Atom, but it should be basically the same.

Start your chosen IDE and install the plugin called `Pymakr`. It can be found in the `Extensions` section. 

You also have to install [Node.js](https://nodejs.org/en/) if you haven't already.

Plug in your LoPy4 and it should be automatically detected in VS Code.

Copy the following code and hit `Run` located in the bottom of VSCode.
```python
import pycom

pycom.heartbeat(False)
pycom.rgbled(0xFFC0CB)
```
If everything works correctly, the onboard LED should become pink.

---

## Connecting LoPy4 and the sensor :electric_plug: 

![Wiring of the project](https://imgur.com/DQRSCv3.png)

The temperature sensor requires an input voltage of 2.7 - 5.5V. The LoPy4 has a 3.3V out which is perfect. This way we don't need any kind of resistors in this project.

The connection is pretty straight forward. Just make sure to connect the pins correctly. Check your sensors sheet to see which way your sensor should go. **It's important not to mess this up, because it could completely destroy your LoPy-board.**

You could also use a breadboard to do the connection. [Here is a guide on how to use a breadboard.](https://www.sciencebuddies.org/science-fair-projects/references/how-to-use-a-breadboard)

---

## The cloud :cloud: 
I decided to use [Ubidots](https://ubidots.com/) as my cloud-solution.

The reason I chose Ubidots is because of it's ease to use. It makes it very simple to connect your device and send data to the cloud. You can easily create graphs and triggers. It is also free (there is a pro version).

I first tried using Pybytes, but setting up an event/trigger was much more difficult. When the temperature was under a certain value, I wanted to be notified somehow. In Pybytes you could create a Webhook and go via some steps to get notified. Ubidots has a built in feature that sends me an E-mail when the conditions of the event is met.

In Ubidots you also have much more freedom to customize your dashboard (screen where you see all your data/graphs) and it looks really neat.

---

## The actual code :computer: 

L I N K T O G I T H U B

---

## Sending the data...

The data is being sent every 10 minutes. To get more accurate data, the data is gathered every minute. Then the average temperature is being sent to the cloud.

I'm using WiFi to connect the board to the internet. You could use SigFox or LoRa, but my apartment doesn't have a LoRa-station close enough to be able to use LoRa and I really didn't like the feel of Sigfox, so WiFi was the way to go for me.

---

## ...and presenting the data

In Ubidots you can represent the data in many different ways. Graphs, tables, thermometers. Follow [this guide](https://help.ubidots.com/en/articles/961994-connect-any-pycom-board-to-ubidots-using-wi-fi-over-http) to connect your device to Ubidots. It will also show how to connect your device to your Wi-Fi network.

Just make sure to enter your WiFi SSID and password.
```python=13
wlan.connect("wifi-SSID-here", auth=(WLAN.WPA2, "wifi-password-here"), timeout=5000)
```

---

## Summary

I would love to have used LoRa instead of WiFi, because it consumes a lot less power, which would make the battery last a lot longer. It would also be cool if I could have connected the temperature to some blinds or curtains, so they would go up and down depending on the temperature.




---



### Thank you! :sheep: 

You can find me on

- GitHub
- Twitter
- or email me

