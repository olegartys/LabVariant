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
	global text_var_entry
	text_var_entry = 92
	
	class Handler :
		"""Callback handlers for widgets"""
		def onDestroy (self, *args) :
			Gtk.main_quit ()
			
		def onEntryChanged (self, obj, window) :
			entry = window.entry
			label = window.label
			text_var_entry = window.var_entry.get_text()
			for i in range(len(entry)):
				x = entry[i].get_text()
				if (len (x) != 0) and (len (text_var_entry) != 0 ) :
					label[i].set_text(str((int(text_var_entry) % int(x)) + 1))
				else :
					label[i].set_text ("Не определено")
							
	def __init__ (self) :
		builder = Gtk.Builder ()
		builder.add_from_file ("LabVariant.glade")
		self.window = builder.get_object ("window1")
		self.window.connect ("destroy", self.Handler().onDestroy)
		self.window.connect ("delete_event", self.Handler().onDestroy)

		
		# Getting entries and labels form *.glade		
		self.entry = []
		self.label = []
		for i in range (3) :
			self.entry.append (builder.get_object ("entry0" + str(i)))
			self.entry[i].connect ("changed", self.Handler().onEntryChanged, self)
			self.label.append (builder.get_object ("label0" + str(i)))	
			self.label[i].set_text ("Не определено")
		self.var_entry = builder.get_object ("var_entry")
		self.var_entry.connect ("changed", self.Handler().onEntryChanged, self)
		self.var_entry.set_text (str(text_var_entry))
		
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

