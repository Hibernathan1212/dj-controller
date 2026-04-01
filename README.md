# DJ Controller

A MIDI jogless DJ controller similar to the Native Instruments S8 and D2 and X1 and Z1. Planning for it to just be a midi controller with knobs for mixing and controlling loops as well as buttons for play/pausing and others usually found on dj decks. Follows a modular design with the deck modules (2 on other side) and the mixer module which will have controls for 4 audio channels.

## Features

- Fully modular system
- 4 Audio track/channel support

## PCB

Made in Kicad

### Schematic

<img src=assets/deck-schematic.png alt="schematic" width="500"/>
<img src=assets/mix-schematic.png alt="schematic" width="500"/>

### PCB

<img src=assets/deck-pcb.png alt="pcb" width="500"/>
<img src=assets/mix-pcb.png alt="pcb" width="500"/>

## Firmware

Uses python with the usb midi library and adafruit to take the GPIO input and send midi signals back to the computer.

# BOM

| Product                   | Amount | Unit Cost (THB) | Price (THB) | Price (USD) | Link                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------- | ------ | --------------- | ----------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CD74HC4067M               | 4      |                 | 57.82       | 1.768033259 | [https://th.aliexpress.com/item/1005003227043008.html](https://th.aliexpress.com/item/1005003227043008.html)                                                                                                                                                                                                                                                                                                                               |
| bourn pta6043             | 7      |                 |             | 0           | [https://th.element14.com/bourns/pta6043-2015cpb103/potentiometer-slide-10kohm-250mw/dp/1857719?srsltid=AfmBOoqvuwWjaY3IxSU_h8GC3fKxQI9NZRXyVhPQeme_ul4yC49cFXwA](https://th.element14.com/bourns/pta6043-2015cpb103/potentiometer-slide-10kohm-250mw/dp/1857719?srsltid=AfmBOoqvuwWjaY3IxSU_h8GC3fKxQI9NZRXyVhPQeme_ul4yC49cFXwA)                                                                                                         |
| bourns ptv09a             | 27     | 28.77           | 776.79      | 23.75286328 | [https://www.digikey.co.th/en/products/detail/bourns-inc/PTV09A-4015F-B503/3781116?srsltid=AfmBOoozMcdKoPI-RDQG1lQ8Al6d9bN97g4HuZHgQqI5ib5jB8QRQoJ4](https://www.digikey.co.th/en/products/detail/bourns-inc/PTV09A-4015F-B503/3781116?srsltid=AfmBOoozMcdKoPI-RDQG1lQ8Al6d9bN97g4HuZHgQqI5ib5jB8QRQoJ4)                                                                                                                                   |
| 100nf 0805 smd capacitors | 10     |                 | 10          | 0.3057823   | [https://shopee.co.th/%E0%B8%95%E0%B8%B1%E0%B8%A7%E0%B9%80%E0%B8%81%E0%B9%87%E0%B8%9A%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%88%E0%B8%B8-smd-0805-capacitor-100nF-0.1uF-104-50V-1nF-0.001uF-102-50V-i.66333115.12805269810](https://shopee.co.th/%E0%B8%95%E0%B8%B1%E0%B8%A7%E0%B9%80%E0%B8%81%E0%B9%87%E0%B8%9A%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%88%E0%B8%B8-smd-0805-capacitor-100nF-0.1uF-104-50V-1nF-0.001uF-102-50V-i.66333115.12805269810) |
| 6 alps ec11               | 6      | 145.16          | 870.96      | 26.6324152  | [https://www.digikey.co.th/th/products/detail/alps-alpine/EC11M1575403/21721623?srsltid=AfmBOoqhhZso9w3b8GA6BwXuJuOzZO6x-qRcbBUOR0bSZI-PHIhii7KG](https://www.digikey.co.th/th/products/detail/alps-alpine/EC11M1575403/21721623?srsltid=AfmBOoqhhZso9w3b8GA6BwXuJuOzZO6x-qRcbBUOR0bSZI-PHIhii7KG)                                                                                                                                         |
| m3 screws                 | 14     | 20              | 20          | 0.6115646   | [https://shopee.co.th/340pcs-M3-Hex-Socket-Screw-Nut-Stainless-Steel-M3-Screws-Nuts-Assortment-Kit-Fas-i.127664245.2039302057](https://shopee.co.th/340pcs-M3-Hex-Socket-Screw-Nut-Stainless-Steel-M3-Screws-Nuts-Assortment-Kit-Fas-i.127664245.2039302057)                                                                                                                                                                               |
| orpheus pico              | 3      | ?               | ?           | 0           |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| jlcpcb                    |        |                 |             | 33.94       |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                           |        |                 |             | 0           |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| digikey delivery          |        |                 | 600         | 18.346938   |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                           |        |                 |             |             |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| total                     |        |                 |             | 105.3575966 |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
