#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Frank Time:2018/12/1

import pygal
# import pygal.maps.world

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx':113423000})

wm.render_to_file('na_populations.svg')