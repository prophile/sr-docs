---
description: Explains how to use the vision parts of the Student Robotics' robot API.
layout: default
title: Vision
---
Vision
======

The `sr.robot` library contains support for detecting libkoki markers with the provided webcam.
Markers are attached to various items in the Student Robotics arena.
Each marker encodes a number in a machine-readable way, which means that robots can identify these objects.
For information on which markers codes are which, see the [markers page](/docs/programming/sr/vision/markers).

Using knowledge of the physical size of the different markers and the characteristics of the webcam,
 libkoki can calculate the position of markers in 3D space relative to the camera.
Therefore, if the robot can see a marker that is at a fixed location in the arena,
 a robot can calculate its exact position in the arena.

The `sr.robot` library provides all of this power through a single function, `R.see`:
{% highlight python %}
from sr.robot import *
R = Robot()
markers = R.see()
{% endhighlight %}
When called, this function takes a photo through the webcam and searches for markers within it.
It returns a list of `Marker` objects, each of which describes one of the markers that were found in the image.
A detailed description of the attributes of Marker objects is provided [later in this page](#Marker).

Here's an example that will repeatedly print out the distance to each flag marker that the robot can see:
{% highlight python %}
from sr.robot import *
R = Robot()

while True:
    markers = R.see()
    print "I can see", len(markers), "markers:"

    for m in markers:
        if m.info.marker_type == MARKER_FLAG:
            print " - Flag {0} is {1} metres away".format( m.info.offset, m.dist )
{% endhighlight %}

[Choosing Resolution](/docs/programming/sr/vision/#ChoosingResolution) {#ChoosingResolution}
-------------------
By default, the `R.see` function will take a photo at a resolution of 800x600.
The resolution that this image is taken at can be changed using the optional `res` argument:
{% highlight python %}
# Take a photo at 1280 x 1024
markers = R.see( res=(1280,1024) )
{% endhighlight %}
There are currently two kinds of webcam issued with SR kit: the Logitech C500 and C270.
They support the following resolutions:


|   Resolution			| C500	|  C270
|-------------------------------|-------|----------
|  160 x 120			| yes	| yes
|  176 x 144			| yes	| yes
|  320 x 176			|	| yes
|  320 x 240			| yes	| yes
|  352 x 288			| yes	| yes
|  432 x 240			|	| yes
|  544 x 288			|	| yes
|  640 x 360			| yes	|
|  640 x 400			| yes	|
|  640 x 480			| yes	| yes
|  752 x 416			|	| yes
|  800 x 448			|	| yes
| **800 x 600** (Default)	| yes	| yes
|  864 x 480			|	| yes
|  960 x 544			|	| yes
|  960 x 720			| yes	| yes
|  1280 x 576			|	| yes
|  1280 x 720			| yes	| yes
|  1280 x 800			| yes	|
|  1280 x 960			| 	| yes
|  1280 x 1024			| yes	|

There are advantages and disadvantages to switching resolution.
Smaller images will process faster, but markers will be less likely to be detected within them.
Additionally, the act of changing resolution takes a significant amount of time.
The optimum resolution to use in a given situation is best determined through experiment.

[Objects of the Vision System](/docs/programming/sr/vision/#vision_objects) {#vision_objects}
==============================

[`Marker`](/docs/programming/sr/vision/#Marker) {#Marker}
----------
A `Marker` object contains information about a *detected* marker.
It has the following attributes:

info
:   A [`MarkerInfo`](#MarkerInfo) object containing information about the type of marker that was detected.

centre
:   A [`Point`](#Point) describing the position of the centre of the marker.

vertices
:   A list of 4 [`Point`](#Point) instances, each representing the position of the black corners of the marker.

dist
:   An alias for `centre.polar.length`

rot_y
:   An alias for `centre.polar.rot_y`

orientation
:   An [`Orientation`](#Orientation) instance describing the orientation of the marker.

res
:   The resolution of the image that was taken from the webcam.
    A 2-item tuple: (width, height).

timestamp
:   The timestamp at which the image was taken (a float).

[`MarkerInfo`](/docs/programming/sr/vision/#MarkerInfo) {#MarkerInfo}
--------------
The `MarkerInfo` object contains information about a marker.
It has the following attributes:

code
:   The numeric code of the marker.

marker_type
:   The type of object that this marker represents.
:   One of:

    * `MARKER_ARENA`
    * `MARKER_ROBOT`
    * `MARKER_FLAG`

offset
:   The offset of the numeric code of the marker from the lowest numbered marker of its type.
    (e.g. Markers 28 and 29, which are the lowest numbered markers that represent robots, have offsets of 0 and 1 respectively.)

size
:   The size of the marker in metres.
    This is the length of the side of the main black body of the marker.

[`Point`](/docs/programming/sr/vision/#Point) {#Point}
---------
A `Point` object describes a position in three different ways.
These are accessed through the following attributes:

image
:   The pixel coordinates of the point in the image, with the origin (0,0) in the top-left of the image.
    This has two attributes: `x` and `y`.

world
:   The Cartesian coordinates of the point in 3D space in metres, with three attributes: `x`, `y`, and `z`.

polar
:   The polar coordinates of the point in 3D space.
:   This has three attributes:

    length
    :   The distance to the point.

    rot_x
    :   Rotation about the x-axis in degrees.

    rot_y
    :   Rotation about the y-axis in degrees.

:   For example, the following code displays the polar coordinate of a `Point` object `p`:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print "length", p.polar.length
    print "rot_x", p.polar.rot_x
    print "rot_y", p.polar.rot_y
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

[`Orientation`](/docs/programming/sr/vision/#Orientation) {#Orientation}
---------------
An `Orientation` object describes the orientation of a marker.  It has three attributes:

rot_x
:   Rotation of the marker about the x-axis.

rot_y
:   Rotation of the marker about the y-axis.

rot_z
:   Rotation of the marker about the z-axis.

