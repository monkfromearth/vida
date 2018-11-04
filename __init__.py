from flask import Flask, request, session, abort
import config.app as APP

# Controllers

import controllers.HomeController as HomeController
import controllers.ErrorController as ErrorController
import controllers.APIController as APIController

site = Flask(__name__, static_folder="assets")

# Enables no-caching

@site.after_request
def add_header(r):
    r.headers['Cache-Control'] = 'public, max-age=604800'
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r


@site.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


route = site.add_url_rule # different name for definition

# Guest Routes

route('/', 'welcome', HomeController.welcome, methods=['GET', 'POST'])

# Api Routes

route('/api/authorize', 'api:authorize', APIController.authorize, methods=['GET', 'POST'])

route('/api/help/languages', 'api:help#languages', APIController.languages, methods=['GET', 'POST'])

route('/api/engine/transliterate', 'api:engine#transliterate', APIController.transliterate, methods=['GET', 'POST'])

# Error Routes

@site.errorhandler(400)
def bad_request(e): return ErrorController.show(400, e)

@site.errorhandler(500)
def internal_error(e): return ErrorController.show(500, e)

@site.errorhandler(501)
def not_implemented(e): return ErrorController.show(501, e)

@site.errorhandler(502)
def bad_gateway(e): return ErrorController.show(502, e)

@site.errorhandler(503)
def service_unavailable(e): return ErrorController.show(503, e)

@site.errorhandler(504)
def gateway_timeout(e): return ErrorController.show(504, e)

@site.errorhandler(401)
def unauthorized(e): return ErrorController.show(401, e)

@site.errorhandler(403)
def not_allowed(e): return ErrorController.show(403, e)

@site.errorhandler(404)
def page_not_found(e): return ErrorController.show(404, e)

if __name__ == "__main__":
    site.jinja_env.cache = {}
    site.secret_key = APP.SECRET_KEY
    site.jinja_env.auto_reload = True
    site.config['TEMPLATES_AUTO_RELOAD'] = True
    site.run(host=APP.HOST, port=APP.PORT, debug=APP.DEBUG, threaded=APP.THREADED)