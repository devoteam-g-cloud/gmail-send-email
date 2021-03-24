from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


class GoogleService:
    """Google API Service"""

    def __init__(
            self,
            service_name: str,
            version: str,
            subject: str = None,
            num_retries: int = None,
            scopes=None,
            service_account_path=None
    ):
        """
        GoogleService constructor
        :param service_name: google service name (drive, gmail, calendar, ...)
        :param version: version of the api (v4 for drive, v1 for gmail...)
        :param subject: email of the delegated account, the account to impersonate. Can be none if not needed (no
        need of a delegated account to read a spreadsheet for example, just to share the spreadsheet to the
        service account email)
        :param num_retries: custom attribute, we use it for exponential backoff purposes
        :param scopes: array of strings, scopes needed to do your actions
        :param service_account_path: local path to your service account json key
        """
        self.service_name = service_name
        self.version = version
        self.credentials = Credentials.from_service_account_file(
            service_account_path,
            scopes=scopes,
            subject=subject,
        )
        self.service = self.build(self.service_name, self.version)
        self.num_retries = num_retries

    def build(self, service: str, version: str):
        """build the service from name, version and credentials"""
        return build(
            service, version, credentials=self.credentials, cache_discovery=False
        )
