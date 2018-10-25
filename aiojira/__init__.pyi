from typing import Dict, Tuple, Any, List, Optional

from .resilientsession import ResilientSession


class Resource(object):
    displayName: Any
    key: Any
    name: Any
    filename: Any
    value: Any
    scope: Any
    votes: Any
    id: Any
    mimeType: Any
    closed: Any

    JIRA_BASE_URL: str

    def __init__(self, resource: str, options: Dict[str, str], session: ResilientSession,
                 base_url: Optional[str] = JIRA_BASE_URL):
        self._resource = resource
        self._options = options
        self._session = session
        self._base_url = base_url
        self.raw = None

    ...


class Project(Resource):
    def __init__(self, options: Dict[str, str], session: ResilientSession, raw: Dict = None):
        super().__init__('', options, session)

    ...


class Issue(Resource):
    def __init__(self, options: Dict[str, str], session: ResilientSession, raw: Dict = None):
        super().__init__('', options, session)

    ...


class JIRA(object):
    @staticmethod
    async def create(server: str = None, options: Dict = None, basic_auth: Tuple[str, str] = None,
                     oauth: Dict[str, str] = None, jwt: Dict = None, kerberos: bool = False,
                     kerberos_options: Dict[str, str] = None, validate: bool = False, get_server_info: bool = True,
                     async_: bool = False, async_workers: int = 5, logging: bool = True, max_retries: int = 3,
                     proxies: Any = None, timeout: int = None, auth: str = None):
        ...

    async def projects(self) -> List[Project]: ...


class JIRAError: ...