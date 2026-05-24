import logging
from utils.singleton import Singleton

class Logger(metaclass=Singleton):
    def __init__(self, level, format, handlers):
        logging.basicConfig(level=level, format=format, handlers=handlers)
        self.logger = logging.getLogger(__name__)

    def get_logger(self) -> logging.Logger:
        return self.logger

logger = Logger(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("backend.log"), logging.StreamHandler()]
).get_logger()