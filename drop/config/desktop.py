# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Drop",
			"color": "grey",
			"icon": "fa fa-tint",
			"type": "module",
			"label": _("Drop")
		},
		{
			"module_name": "Soil",
			"color": "red",
			"icon": "octicon octicon-folder",
			"type": "module",
			"label": _("Soil")
		}
	]
