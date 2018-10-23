import sys

from aioify import aioify
import jira


__version__ = '0.1.1'


aiojira = aioify(obj=jira, name=__name__, skip=['Issue', 'Project'])

sys.modules[__name__] = aiojira
from aiojira import *
