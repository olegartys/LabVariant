#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  LabVariant.py
#  
#  Copyright 2014 olegartys <olegartys@gmail.com>
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

from gi.repository import Gtk

class LabVariant :
	class Handler :
		"""Callback handlers for widgets"""
		def onDestroy (self, *args) :
			Gtk.main_quit ()
			print (args)
		def onEntryChanged (self, *entry) : 
			for i in entry :
				print (i.get_text())
	
	global text_var_entry
	text_var_entry = 92		
	def __init__ (self) :
		builder = Gtk.Builder ()
		builder.add_from_file ("LabVariant.glade")
		self.window = builder.get_object ("window1")
		self.window.connect ("destroy", self.Handler().onDestroy)
				
		self.entry = []
		self.entry.append (builder.get_object ("entry00"))
		k = 1
		for i in self.entry : i.set_text (str(2*k)); k += 1
		self.entry[0].connect ("changed", self.Handler().onEntryChanged, *self.entry)
		self.label = []
		for i in range (3) :
			self.entry.append (builder.get_object ("entry0" + str(i+1)))
			self.entry[i+1].connect ("changed", self.Handler().onEntryChanged, *self.entry)
			self.label.append (builder.get_object ("label0" + str(i)))
		
		
		
	def run (self) :
		"""Run program"""
		self.window.show_all ()
		Gtk.main ()

def main():
	app = LabVariant ()
	app.run ()
	return 0

if __name__ == '__main__':
	main()

