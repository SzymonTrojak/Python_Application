from .ambulance import Ambulance

class AmbulanceQueue:
    def __init__(self):
        self.__queue = []

    def __str__(self):
        if len(self):
            return "\n".join([f"{' ' * (4 * idx)}{ambulance}" for idx, ambulance in enumerate(self.__queue)])
        else:
            return "Empty queue"

    def __iadd__(self, other):
        if isinstance(other, Ambulance):
            self.__queue.append(other)
        return self 
    
    def __len__(self):
        return len(self.__queue)
    
    def __getitem__(self, position):
        return self.__queue[position]