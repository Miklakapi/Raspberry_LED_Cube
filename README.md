# Raspberry_LED_Cube

![license](https://img.shields.io/badge/license-MIT-blue)
![linux](https://img.shields.io/badge/os-Linux-green)
![language](https://img.shields.io/badge/language-Python3.9-blue)
![version](https://img.shields.io/badge/version-1.0.0-success)
![status](https://img.shields.io/badge/status-production-green)

A simple program in Python that manages the LED cube with a Raspberry Pi and two additional programs that can control the LED cube via a website.

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)

## General info
### Simple LED Cube
A program written in a Python that manages a LED Cube using a Raspberry Pi, transistors and shift registers.
The data is displayed based on the `sequences.json` file.
### Web App
Program written in Python, javaScript, HTML, CSS that allows you to edit and display sequences.
### Online LED Cube
A program written in Python that manages an LED cube just like a Simple LED Cube, but displays data based on data retrieved from a web server.

![Alt Text](https://github.com/Miklakapi/Raspberry_LED_Cube/blob/master/led_cube.gif)

```
One sequence
[
    "0000000000000000000000000",    <- First flor
    "0000000000000000000000000",
    "0000000000000000000000000",
    "1111110001100011000111111",
    "1111111111110111111111111",    <- Fifth floor
    0.04                            <- How long this sequence will be displayed
]

Cube columns
┌────┬────┬────┬────┬────┐
│ 05 │ 10 │ 15 │ 20 │ 25 │
├────┼────┼────┼────┼────┤
│ 04 │ 09 │ 14 │ 19 │ 24 │
├────┼────┼────┼────┼────┤
│ 03 │ 08 │ 13 │ 18 │ 23 │
├────┼────┼────┼────┼────┤
│ 02 │ 07 │ 12 │ 17 │ 22 │
├────┼────┼────┼────┼────┤
│ 01 │ 06 │ 11 │ 16 │ 21 │
└────┴────┴────┴────┴────┘
```
## Technologies
Project is created with:

* Python 3.9
* Flask
* Package to manage GPIO `RPi.GPIO`

## Setup
### Simple LED Cube
To run only LED Cube, run:
```python3 /src/app.py```
### Web App
To run web app, run:
```python3 /web_editor/web_app.py```
### Online LED Cube
To run online LED cube, run:
```python3 /web_editor/online_cube_app.py```

## Features
### Simple LED Cube
* Reading sequences and settings from a file.
* Returning errors to a file.
* Easy time management.
* Loop rate limiting class.
### Web App
* Creating sequences to the LED Cube with mouse clicks.
* Display sequences on the website after pasting it into the text area.
* Download json file with created sequences.
### Online LED Cube
* Gets data from web server
* Display data from web app

## Status
The project's development has been completed.
