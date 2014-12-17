#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tmp.py
#  
#  Copyright 2014 olegartys <olegartys@olegartysLaptop>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import json
import urllib2

def main():
	f = open ("base.json", "r")
	s = f.read ()
	data = json.loads (s)
	for i in data :
		print (i['name'])
	return 0

if __name__ == '__main__':
	main()

