from logger_config import logger

class Incident:
    __max_id = 0

    def __init__(self, description, priorty, time, reporter, location):
        self.id = Incident.__max_id
        self.description = description
        self.priorty = priorty
        self.time = time
        self.reporter = reporter
        self.location = location
        self.ambulance = None
        Incident.__max_id += 1
        self.logger = logger
        self.logger.info(f"Created new Incident: {self}")

    def __repr__(self):
        return f"Incident(id={self.id!r}, description={self.description!r}, priorty={self.priorty!r}, time={self.time!r}, reporter={self.reporter!r})"

    def __str__(self):
        return f"Incident {self.id}: {self.description}, priorty={self.priorty}, {self.time}, reported by: {self.reporter}"

if __name__ == "__main__":
    incident = Incident(
        description="Wypadek drogowy",
        priorty=1,
        time="30.06.2024 14:30",
        reporter="John Doe",
        location=(50.061944, 19.936944)
    )

    print(repr(incident))
    print(str(incident))
