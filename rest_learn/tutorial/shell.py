# -*- coding: utf-8 -*-
import os
import sys
import django
import pprint

#
pathname = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, pathname)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
django.setup()
#
from django.forms.models import model_to_dict
from blog.models import *
from snippets.models import *

#

b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
b.save()
