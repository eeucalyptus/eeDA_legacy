# eeDA

eeDA is intended to be an industry-suited electrical design aid for circuit design and PCB layouts.

## Purpose

There are a lot of open source circuit design and layout tools out there in the internet. The software that outshines all of them is [KiCad](http://kicad-pcb.org/). Despite its enormous scope, it is often really counter-intuitive (library system, split feature set for different render modes, bad 3D model handling, to name just a few points). eeDA is intended to be more intuitive, while competing with the feature set and providing better compatibility for external tools, like mechanical construction, etc.

## Goals

eeDA is designed under the following concerns:
### Intuitive
Everything is supposed to work is you think it would. No hidden magic, except when expected...
### Easy
Nobody wants to read docs for the same task over and over again. If you read it once, you will never look it up again.
### For everybody
eeDA is supposed to be used by hobbyists, makers, professionals and artists, no matter how experienced you are. eeDA will never expect you to be a guru. However, eeDA will also never assume you are a novice.
### Performance
eeDA is optimized for performance. The speed of your machine should not limit your productivity.

## Dependencies
eeDA depends on the following libraries:

- PyQt5
- PyYAML
- PIL (Pillow)
- PyOpenGL

You need to install them manually or using pip, in order to run eeDA.

## Installation
We did not implement a proper installation routine, yet.
Just run `python __main__.py` from the app directory - and you're in!

## Tests

To run the unit tests, simply run `python -m unittest tests` from the app directory.

## Authors
The project is being developed by
* **Eike Schwarzwald** - Initiator, backend logic - [eeucalyptus](https://github.com/eeucalyptus)
* **Gavin Lüdemann** - OpenGL, Qt - [Musicted](https://github.com/Musicted)
