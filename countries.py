#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Frank Time:2018/11/30

from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])