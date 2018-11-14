import sys

from aioify import aioify
import jira
import poetry_version


__version__ = poetry_version.extract(source_file=__file__)


aiojira = aioify(obj=jira, name=__name__, skip=['Issue', 'Project'])

sys.modules[__name__] = aiojira
from aiojira import *
