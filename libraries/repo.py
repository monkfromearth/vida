from flask import request, jsonify, session
from Crypto.Hash import MD5, SHA256
import random, string, sys, os, time

class Repo:

	@staticmethod
	def token(N = 12):
		''' Generates a random base64 string with defined length '''
		return ''.join(random.choice(string.ascii_letters + string.digits + '-_') for _ in range(N))

	@staticmethod
	def random():
		''' Generates a random MD5 token '''
		return MD5.new(os.urandom(8)).hexdigest()

	@staticmethod
	def hash(data, algo='md5'):
		''' Generates a hash without salt '''
		if algo is 'md5':
			return MD5.new(data).hexdigest()
		elif algo is 'sha256': 
			return SHA256.new(data).hexdigest()

	@staticmethod
	def csrfToken():
		''' Sets a CSRF Token for the current session '''
		csrf_token = session.get('csrf_token')
		if csrf_token is None:
			csrf_token = Repo.random()
			session['csrf_token'] = csrf_token
		return csrf_token

	@staticmethod
	def time():
		''' Returns the UNIX Timestamp as int '''
		return int(time.time())

	@staticmethod
	def exception(e):
		''' Handles command line exception displaying line error '''
		print "Exception: ", str(e)
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(exc_type, fname, exc_tb.tb_lineno)

	@staticmethod
	def api(kind, status, message, content = {}):
		''' Returns a dict with the kind of API '''
		return {
			'kind':'vida-%s' % kind,
			'status':status,
			'message':message,
			'content':content
		}