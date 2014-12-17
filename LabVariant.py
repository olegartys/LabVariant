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
import json

def calculateTaskNumber (var, kol) :
	"""Calculates task number with formula using variant and count of tasks"""
	return (int(var) % int(kol)) + 1

class LabVariant :
	# Variant number
	global text_var_entry
	text_var_entry = 92
	# List with task numbers
	global task_numbers
	task_numbers = [1, 1, 1]
	
	def showAbout (self, *args) :
		dialog = Gtk.AboutDialog ()
		dialog.set_program_name ("LabVariant")
		dialog.set_copyright ("Copyright (c) 2014")
		authors = ["Oleg Lyovin <olegartys@gmail.com>"]
		dialog.set_authors (authors)
		
		dialog.run ()
		dialog.destroy ()
	
	class Handler :
		"""Callback handlers for widgets"""
		@staticmethod
		def onDestroy (*args) :
			Gtk.main_quit ()
		
		@staticmethod
		def onEntryChanged (obj, window) :
			entry = window.entry
			label = window.label
			text_var_entry = window.var_entry.get_text ()
			for i in range (len (entry)):
				x = entry[i].get_text ()
				if (len (x) != 0) and (len (text_var_entry) != 0 ) :
					task_numbers[i] = int (entry[i].get_text ())
					label[i].set_text(str(calculateTaskNumber(text_var_entry, task_numbers[i])))
				else :
					label[i].set_text (str(calculateTaskNumber(text_var_entry, task_numbers[i])))
			window.refreshTree ()
			
	def refreshTree (self) :
		"""Refreshes tree when something has changed"""
		store = self.tree.get_model ()
		for row in store : 
			var = row[0]
			row[3] = calculateTaskNumber (var, task_numbers[0])
			row[4] = calculateTaskNumber (var, task_numbers[1])
			row[5] = calculateTaskNumber (var, task_numbers[2])
	
	def createTree (self) :	
		"""Creates tree"""	
		store = Gtk.ListStore (int, int, str, int, int, int)
		f = open ("base.json", "r")
		students_base = json.loads (f.read ())
		for token in students_base :
			store.append ([token['variant'], token['group'], token['name'], 
									calculateTaskNumber(text_var_entry, task_numbers[0]), 
									calculateTaskNumber(text_var_entry, task_numbers[1]), 
									calculateTaskNumber(text_var_entry, task_numbers[2])])
		tree = Gtk.TreeView (store)
		
		renderer = Gtk.CellRendererText ()
		renderer.set_property ("xalign", 1)
		column = Gtk.TreeViewColumn ("\t№\nварианта", renderer, text=0)
		column.set_sort_column_id(0)
		column.width = 20
		column.set_resizable (True)
		tree.append_column (column)
		
		column = Gtk.TreeViewColumn ("\t№\n  группы", renderer, text=1)
		column.set_sort_column_id(1)
		column.set_resizable (True)
		tree.append_column (column)
		
		column = Gtk.TreeViewColumn ("ФИО", renderer, text=2)
		column.set_sort_column_id(2)
		column.set_resizable (True)
		tree.append_column (column)
		
		column = Gtk.TreeViewColumn ("№1", renderer, text=3)
		column.set_sort_column_id(3)
		column.set_resizable (True)
		tree.append_column (column)
		
		column = Gtk.TreeViewColumn ("№2", renderer, text=4)
		column.set_sort_column_id(4)
		column.set_resizable (True)
		tree.append_column (column)
		
		column = Gtk.TreeViewColumn ("№3", renderer, text=5)
		column.set_sort_column_id(5)
		column.set_resizable (True)
		tree.append_column (column)
		return tree
							
	def __init__ (self) :
		builder = Gtk.Builder ()
		builder.add_from_file ("LabVariant.glade")
		self.window = builder.get_object ("window1")
		self.window.connect ("destroy", self.Handler.onDestroy)
		self.window.connect ("delete_event", self.Handler.onDestroy)
		
		# Getting entries and labels form *.glade		
		self.entry = []
		self.label = []
		for i in range (3) :
			self.entry.append (builder.get_object ("entry0" + str(i)))
			self.entry[i].set_text (str(task_numbers[i]))
			
			self.label.append (builder.get_object ("label0" + str(i)))	
			self.label[i].set_text (str(calculateTaskNumber(text_var_entry, task_numbers[i])))
		# Connect signals for entries
		for i in range (3) : self.entry[i].connect ("changed", self.Handler.onEntryChanged, self)
		
		# Initialize variant entry
		self.var_entry = builder.get_object ("var_entry")
		self.var_entry.set_text (str(text_var_entry))
		self.var_entry.connect ("changed", self.Handler.onEntryChanged, self)
		
		# Initialize tree
		self.scrolled_window = builder.get_object ("scrolledwindow1")
		self.tree = self.createTree ()
		self.scrolled_window.add (self.tree)
		
		#Initialize menu
		self.menu_about = builder.get_object ("imagemenuitem10")
		self.menu_about.connect ("activate", self.showAbout) 
		
		
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

