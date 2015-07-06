from .base import *

try:
	from .local import *
	live = True

except:
	live = False

if live:
	from .production import *