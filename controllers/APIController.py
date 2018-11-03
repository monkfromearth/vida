# -*- coding: utf-8 -*-

# Renders all the global functions, wrappers and variables

from universe import *

from libraries.vida import Vida

def authorize():
	status = True; message = "You're connected to Vida."; content = {}
	content['csrf_token'] = Repo.csrfToken()
	return jsonify(Repo.api('api:authorize', status, message, content))


def languages():
	status = True; message = "These are the languages supported by Vida."; content = {}
	content['list'] = Vida.languages
	content['codes'] = Vida.languages.keys()
	content['names'] = Vida.languages.values()
	return jsonify(Repo.api('api:help#languages', status, message, content))

def transliterate():
	status = False; message = "Couldnt transliterate the text."; content = {}
	try:
		source = request.args.get('source', 'eng')
		target = request.args.get('target', 'hin')
		text = request.args.get('text', '')
		if len(text) == 0: raise Exception("Please provide some text to transliterate.")
		vida = Vida(text.encode('utf-8'), source, target)
		transliteration = vida.run()
		status = transliteration['status']
		message = transliteration['message']
		content = transliteration['content']
	except Exception as e: Repo.exception(e)
	return jsonify(Repo.api('api:engine#transliterate', status, message, content))