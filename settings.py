from environs import Env
from dotenv import load_dotenv


load_dotenv()

env = Env()


class Settings: 
    APK = env.str("APK")  # 'usr/local/path_to_apk/test.apk'
    HOST = env.str("HOST")  # '127.0.0.1:4724'
