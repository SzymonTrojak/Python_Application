from .ambulance import Ambulance
from logger_config import logger

class AmbulanceQueue:
    def __init__(self):
        self.__queue = []
        self.logger = logger
        self.logger.info("AmbulanceQueue initialized")

    def __str__(self):
        self.logger.debug("AmbulanceQueue __str__ called")
        if len(self):
            return "\n".join([f"{' ' * (4 * idx)}{ambulance}" for idx, ambulance in enumerate(self.__queue)])
        else:
            return "Empty queue"

    def __iadd__(self, other):
        if isinstance(other, Ambulance):
            self.__queue.append(other)
            self.logger.info(f"Ambulance added to queue: {other}")
        else:
            self.logger.warning("Attempted to add non-Ambulance to queue")
        return self 
    
    def __len__(self):
        return len(self.__queue)
    
    def __getitem__(self, position):
        self.logger.debug(f"AmbulanceQueue __getitem__ called for position: {position}")
        return self.__queue[position]
