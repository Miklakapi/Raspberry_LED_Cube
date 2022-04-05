# Raspberry_LED_Cube

![license](https://img.shields.io/badge/license-MIT-blue)
![linux](https://img.shields.io/badge/os-Linux-green)
![language](https://img.shields.io/badge/language-Python3.9-blue)
![version](https://img.shields.io/badge/version-1.1.0-success)
![status](https://img.shields.io/badge/status-develop-yellow)

A simple python program that manages a led cube with a Raspberry Pi.

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [TODO](#todo)

## General info
A program written in a python that manages a led cube using a Raspberry Pi, transistors and shift registers.
The data is displayed based on the `sequences.json` file.

## Technologies
Project is created with:

* Python 3.9
* Module to manage GPIO `RPi.GPIO`

## Setup
To run this project, run:
```/src/main.py```

## Features
* Reading sequences and settings from a file.
* Returning errors to a file.
* Easy time management.
* Loop rate limiting class.

## Status
The project is in the development phase.

## ToDo
- Create Web page to create json sequences file