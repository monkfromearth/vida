# -*- coding: utf-8 -*-

# Error Controller

# Renders all the global functions, wrappers and variables
from universe import *

def show(code, message):
	format = request.args.get('format') or request.form.get('format')
	print format 
	return render("error", code=code, message=message), code