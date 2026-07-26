import gspread
from pathlib import Path
from oauth2client.service_account import ServiceAccountCredentials


def get_credentials_file():
    """
    Access JSON file contaning credentials for integration
    """
    for item in (Path.cwd()/"worksheet").iterdir():
        if "automacaotarefacorreios" in item.name:
            return item.name


def get_worksheet(name):
    creds_f = get_credentials_file()

    # Set the access permissions for integration services
    permissions = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    # Set credentials
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        filename = (
            Path.cwd()/"worksheet"/creds_f
        ).as_posix(), 
        scopes = permissions
    )

    # Set session with integration
    client = gspread.authorize(creds)

    # Access workspace
    workspace = client.open(title = name)

    # Access worksheet
    worksheet = workspace.get_worksheet_by_id(
        id = 10171118
    )

    return worksheet