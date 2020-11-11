# -*- coding: utf-8 -*-

import os, sys, site

activate_this = '/home/f/factorexru/.venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
site.addsitedir('/home/f/factorexru/.venv/lib/python2.7/site-packages')
sys.path.insert(1,'/home/f/factorexru/factorex.ru/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'factorex.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

