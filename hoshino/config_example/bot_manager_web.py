import os
from .__bot__ import HOST, PORT

ICP_CONTENT = os.environ.get('ICP_CONTENT') if os.environ.get('ICP_CONTENT') else ''
PUBLIC_ADDRESS = os.environ.get('PUBLIC_ADDRESS') if os.environ.get('PUBLIC_ADDRESS') else f"http://{HOST}:{PORT}"
PASSWORD = os.environ.get('BOT_MANAGER_WEB_PASSWORD') if os.environ.get('BOT_MANAGER_WEB_PASSWORD') else '123456'