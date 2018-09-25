from typing import Dict, Tuple, Any, List


class Resource(object): ...

class Project(Resource): ...

class JIRA(object):
    @staticmethod
    async def create(server: str = None, options: Dict = None, basic_auth: Tuple[str, str] = None,
                     oauth: Dict[str, str] = None, jwt: Dict = None, kerberos: bool = False,
                     kerberos_options: Dict[str, str] = None, validate: bool = False, get_server_info: bool = True,
                     async_: bool = False, async_workers: int = 5, logging: bool = True, max_retries: int = 3,
                     proxies: Any = None, timeout: int = None, auth: str = None):
        ...

    async def projects(self) -> List[Project]: ...