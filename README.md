# aiojira - asynchronous Jira Python library
Asynchronous Jira Python library - asynchronous wrapper for https://github.com/pycontribs/jira

## Installation
To install from PyPI: https://pypi.org/project/aiojira/ run:
```shell
$ pip install aiojira
```

## Usage
For documentation refer to https://jira.readthedocs.io, because `aiojira` uses the same API as `jira` with 2 exceptions:
1. All functions are converted to coroutines, that means you have to add `await` keyword before all function calls.
2. To asynchronously create classes from `aiojira` use static method `create`.

Example:
```python
import asyncio
import aiojira


server = 'https://jira.example.com/'
auth = ('user', 'password')

JIRA = asyncio.run(aiojira.JIRA.create(server=server, basic_auth=auth))
projects = asyncio.run(JIRA.projects())
print(projects)
```
