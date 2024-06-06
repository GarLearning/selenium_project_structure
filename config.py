from os import getenv, path
from dotenv import load_dotenv

load_dotenv(path.realpath(".env"))

class Config:
    """
    .env variables
    """
    chrome_path = getenv('CHROME_PATH')
