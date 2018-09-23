# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['aiojira']

package_data = \
{'': ['*']}

install_requires = \
['aioify', 'jira>=2.0,<3.0']

dependency_links = \
['git+ssh://git@github.com/rominf/aioify.git']

setup_kwargs = {
    'name': 'aiojira',
    'version': '0.1.3',
    'description': 'Asynchronous Jira library',
    'long_description': "# aiojira - asynchronous Jira Python library\nAsynchronous Jira Python library - asynchronous wrapper for https://github.com/pycontribs/jira\n\n## Installation\nTo install from PyPI: https://pypi.org/project/aiojira/ run:\n```shell\n$ pip install aiojira\n```\n\n## Usage\nFor documentation refer to https://jira.readthedocs.io, because `aiojira` uses the same API as `jira` with 2 exceptions:\n1. All functions are converted to coroutines, that means you have to add `await` keyword before all function calls.\n2. To asynchronously create classes from `aiojira` use static method `create`.\n\nExample:\n```python\nimport asyncio\nimport aiojira\n\n\nserver = 'https://jira.example.com/'\nauth = ('user', 'password')\n\nJIRA = asyncio.run(aiojira.JIRA.create(server=server, basic_auth=auth))\nprojects = asyncio.run(JIRA.projects())\nprint(projects)\n```\n",
    'author': 'Roman Inflianskas',
    'author_email': 'r.inflyanskas@zmeke.com',
    'url': 'https://github.com/rominf/aiojira',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'dependency_links': dependency_links,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
