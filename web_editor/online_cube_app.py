#!/usr/bin/env python

"""This module manages the LED cube using web server."""

from real_time_display import OnlineDisplay


if __name__ == '__main__':
    online_display = OnlineDisplay()

    try:
        online_display.start()
        online_display.run_cube()
    except KeyboardInterrupt:
        online_display.stop()
