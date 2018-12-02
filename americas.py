#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Frank Time:2018/11/30

# import pygal
import pygal.maps.world

# wm = pygal.Worldmap()
wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'

wm.add('north America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl' 'co', 'ec', 'gf',
                         'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')