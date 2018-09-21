# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['jira_async']

package_data = \
{'': ['*']}

install_requires = \
['jira>=2.0,<3.0']

setup_kwargs = {
    'name': 'jira-async',
    'version': '0.1.0',
    'description': 'Asynchronous Jira library',
    'long_description': None,
    'author': 'Roman Inflianskas',
    'author_email': 'r.inflyanskas@zmeke.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
