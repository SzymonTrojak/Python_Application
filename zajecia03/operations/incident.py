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

    def __repr__(self):
        return f"Incident(id={self.id!r}, description={self.description!r}, priorty={self.priorty!r}, time={self.time!r}, reporter={self.reporter!r})"

    def __str__(self):
        return f"Incident {self.id}: {self.description}, priorty={self.priorty}, {self.time}, reported by: {self.reporter}"