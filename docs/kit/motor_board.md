---
layout: default
title: Motor Board
---
Motor Board
===========

<img src="/images/content/kit/mcv4b.png" alt="A phot of an un-cased motor board" title="An un-cased motor board" class="right" />
The Motor Board can be used to control two 12V DC motors. Your kit contains two of these boards to allow you to control up to four motors. These can be used for moving your robot, although don't feel you are limited to using them for this purpose.

The speed and direction of the two outputs are controlled independently through the USB interface.
The USB interface is isolated from the rest of the board to prevent damage to the host in the case of a board failure.
Due to this isolation the board must have power applied to the power connector, from the motor rail on the power board, to function.
If the board does not have power applied to the power connector then the kit will report that there is a problem with the motor board.

Board Diagram
-------------

![motor board diagram](/images/content/kit/mcv4b_board_diagram.png "The Motor Board")

Indicators
----------

| LED                    | Meaning                 | Initial power-up state
|------------------------|-------------------------|------------------------------
| Power                  | The board is powered    | On
| M{0,1} Speed/Direction | Brightness indicates speed, colour indicates direction | Off
| USB Power              | The USB interface is powered | On
| USB Data               | Data is being transferred to/from the board | Off

Case Dimensions
---------------

The case measures 70x84x20mm. Don't forget that the cables will stick out.

Specification
-------------

| Parameter                             | Value       |
|---------------------------------------|-------------|
| Nominal input voltage                 | 11.1V ± 15% |
| Absolute maximum input voltage        | 16V         |
| Minimum input voltage                 | 9V          |
| Output voltage                        | 11.1V ± 15% |
| Continuous output current per channel | 10A         |
| Peak output current [^1]              | 20A         |
| UART connection voltage [^2]          | 3.3–5V      |

[^1]: Can be sustained for 1 second, on a single channel.
[^2]: If the board is controlled solely via the UART connection, this voltage must be supplied via the UART connector.

Designs
-------

You can access the schematics and source code of the firmware on the motor board in the following places.
You do not need this information to use the board but it may be of interest to some people.

 * [Full Schematics](/resources/kit/motor-schematic.pdf)
 * [Firmware Source](https://www.studentrobotics.org/cgit/boards/motor-v4-fw.git/)
 * [Hardware Designs](https://www.studentrobotics.org/cgit/boards/motor-v4-hw.git/)
