from environs import Env
from dotenv import load_dotenv
import os


PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

load_dotenv()

env = Env()


class Settings: 
    APK = env.str("PATH")  # 'usr//local//path_to_apk//test.apk'
    APK = PATH(APK)
    HOST = env.str("HOST")
