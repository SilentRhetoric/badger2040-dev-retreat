# Badger2040 for Algorand Developer Retreat

This repository contains the code that runs on the Pimoroni Badger2040 devices that were programmed for the Castell d'Code Algorand Developer Retreat.

## General Information

Pimoroni's guide for programming the Badger 2040 can be found at 
<https://learn.pimoroni.com/article/getting-started-with-badger-2040>.

The kit box contains a USB cable and adapter for connecting the badge to your laptop. It also has a battery pack that can be connected to the JST-PH connector if you want the badge to be interactive when not plugged into USB power. It is also possible to connect a USB battery to the USB-C port on the  badge to power it.

## Custom Badges for Castell d'Code

The badges were individually programmed by yours truly. I redesigned the badge display design to be more appealing and legible for this event and uploaded each person's personal details by hand.

The badge display is created by a MicroPython script at `examples/badge.py`, which grabs personal details from a `.txt` file and the image from a `.jpg` file in the `badges` directory.

Note a few quirks:
- There's only room for 12 characters in the font size I've used for the name, company, etc. The text can be drawn at different sizes and in different fonts, if desired.
- The image must fit within 128x128 pixels, but it is OK if it is smaller than that.
- If the badge gets into a bad state when connected to your computer, you can use the `rst` reset button on the back to reboot it and try to get it back into a good state.

## Hacker Bounty

Some bonus Algorand swag will be awarded to the person who most creatively hacks the badge to do something interesting. Show me your customization by the closing ceremony on Friday. I will determine the winner at my sole discretion.

Note: This bounty is only open to in-person attendees at the Developer Retreat so that I can hand you your swag.

-Brian