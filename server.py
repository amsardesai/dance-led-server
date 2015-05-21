#!/usr/bin/env python
# pylint: disable-msg=C0103,C0111
"""This module is the server for our Dance LED server."""

from flask import Flask
app = Flask(__name__)

led_matrix = [[False for x in range(32)] for x in range(16)]

@app.route("/")
def index():
    return "it works"

@app.route("/update/<c_x>/<c_y>/<on>")
def update(c_x, c_y, on):
    led_matrix[int(c_x)][int(c_y)] = (on == 'true')

    output = ''
    for row in led_matrix:
        output += '|'
        for cell in row:
            output += ('@' if cell == True else ' ') + '|'
        output += '\n'
    return output

if __name__ == "__main__":
    app.debug = True
    app.run()

