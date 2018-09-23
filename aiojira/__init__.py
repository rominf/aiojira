import sys

from aioify import aioify
import jira


__version__ = '0.1.0'


aiojira = aioify(obj=jira, name='aiojira')

sys.modules[__name__] = aiojira
from aiojira import *
