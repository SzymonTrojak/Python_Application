from .incident import Incident
from logger_config import logger

class IncidentQueue:
    def __init__(self):
        self.__queue = []
        self.logger = logger
        self.logger.info("Initialized IncidentQueue.")

    def __getitem__(self, position):
        self.logger.debug(f"Getting item at position {position}.")
        return self.__queue[position]

    def __setitem__(self, position, value):
        self.logger.debug(f"Setting item at position {position}.")
        self.__queue[position] = value

    def __iter__(self):
        self.logger.debug("Iterating over IncidentQueue.")
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.__queue):
            result = self.__queue[self._index]
            self._index += 1
            self.logger.debug(f"Next item: {result}.")
            return result
        else:
            self.logger.debug("End of iteration.")
            raise StopIteration

    def __contains__(self, incident):
        self.logger.debug(f"Checking if incident {incident} is in IncidentQueue.")
        return incident in self.__queue

    def __repr__(self):
        self.logger.debug("Representing IncidentQueue.")
        return f"IncidentQueue({self.__queue!r})"

    def __str__(self):
        self.logger.debug("Printing IncidentQueue.")
        if len(self):
            return "\n".join([f"{' ' * (4 * idx)}{incident}" for idx, incident in enumerate(self.__queue)])
        else:
            return "Empty queue"

    def __add__(self, other):
        if isinstance(other, Incident):
            new_queue = IncidentQueue()
            new_queue.__queue = self.__queue[:]
            new_queue += other
            self.logger.debug(f"Adding incident {other} to IncidentQueue.")
            return new_queue
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Incident):
            new_queue = IncidentQueue()
            new_queue += other
            new_queue.__queue += self.__queue
            self.logger.debug(f"Adding incident {other} to the right of IncidentQueue.")
            return new_queue
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Incident):
            self.__queue.append(other)
            self.logger.info(f"Added incident {other} using __iadd__.")
        return self

    def __call__(self, id):
        self.logger.debug(f"Calling IncidentQueue with ID {id}.")
        for incident in self.__queue:
            if incident.id == id:
                self.logger.debug(f"Found incident with ID {id}.")
                return incident
        self.logger.error(f"No incident with ID {id} found.")
        raise ValueError("Brak incydentu z takim ID")

    def __lt__(self, other):
        self.logger.debug("Comparing lengths of IncidentQueue.")
        return len(self.__queue) < len(other.__queue)

    def __gt__(self, other):
        self.logger.debug("Comparing lengths of IncidentQueue.")
        return len(self.__queue) > len(other.__queue)

    def __bool__(self):
        self.logger.debug("Checking if IncidentQueue is empty.")
        return bool(self.__queue)

    def __len__(self):
        self.logger.debug("Getting length of IncidentQueue.")
        return len(self.__queue)

if __name__ == "__main__":
    queue = IncidentQueue()
    incident1 = Incident(1, "Wypadek drogowy koscielna 52")
    incident2 = Incident(2, "wyciagniecie topielca rzeka Wisla")
    incident4 = Incident(4, "Pozar budynku 20 AGH")

    print(f"---------- wyświetlanie za pomocą __str__ ----------")
    print(queue)

    print(f"---------- dodanie za pomocą __iadd__ ----------")
    queue += incident1
    queue += incident2
    print(queue)

    print(f"---------- dodanie za pomocą __add__ ----------")
    queue = queue + incident4
    print(queue)

    print(f"---------- dostęp za pomocą __getitem__ ----------")
    print(queue[0])

    print(f"---------- sprawdzenie za pomocą __contains__ ----------")
    print(incident1 in queue)

    print(f"---------- iteracja za pomocą __iter__ i __next__ ----------")
    for incident in queue:
        print(incident)

    print(f"---------- dodawanie prawostronne za pomocą __radd__ ----------")
    new_incident = Incident(3, "Test incident")
    queue = new_incident + queue

    print(f"---------- test za pomocą __bool__ ----------")
    if queue:
        print("Queue is not empty.")

    print(f"---------- długość kolejki za pomocą __len__ ----------")
    print(len(queue))

    print(f"---------- wyszukiwanie za pomocą __call__ ----------")
    print(queue(1))
