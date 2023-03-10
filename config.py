# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    APP_ID = int(os.environ.get("7143337"))
    API_HASH = os.environ.get("1afa55a5f3bf7058c843d1b290f79c49")
    BOT_TOKEN = os.environ.get("6043283784:AAHLV11M9g3gaDj5dE-Sr5fKhSCd8CT-lOc")
    LOGS_CHANNEL = int(os.environ.get("-1001465954010"))
    BOT_OWNER = int(os.environ.get("1284818583"))
    MONGODB_URL = os.environ.get("MONGODB_URL")
    GOFILE_TOKEN = os.environ.get("GOFILE_TOKEN")
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6
