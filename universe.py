from flask import render_template, request, url_for, redirect, jsonify, flash, session, abort
from htmlmin.minify import html_minify
from libraries.repo import Repo
import config.app as APP

def render(name,**kwargs):
    platform = {
        'CSRF_TOKEN':Repo.csrfToken()
    }
    configs = {
        'SITE_NAME':APP.SITE_NAME
    }
    data = html_minify(render_template(name+".html", platform=platform, configs=configs, **kwargs))
    if request.is_xhr :
        for r in ['<html>','<head>','</head>','<body>','</body>','</html>']: data = data.replace(r,'')
    return data