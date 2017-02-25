

class CoordinateBounds(object):

    def __init__(self, minimum, maximum):
        self.min = minimum
        self.max = maximum

    def __str__(self):
        return "(%s, %s)" % (self.min, self.max)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Track(object):

    def __init__(self,
                 ascending_height=None,
                 avg_heart_rate=None,
                 calories=None,
                 date=None,
                 descending_height=None,
                 description=None,
                 distance=None,
                 duration=None,
                 laps=[],
                 max_heart_rate=None,
                 max_height=None,
                 max_speed=None,
                 memory_block_index=None,
                 min_height=None,
                 name=None,
                 no_laps=None,
                 no_track_points=None,
                 track_id=None,
                 track_points=[]
                 ):
        self.ascending_height = ascending_height
        self.avg_heart_rate = avg_heart_rate
        self.calories = calories
        self.date = date
        self.descending_height = descending_height
        self.description = description
        self.distance = distance
        self.duration = duration
        self.id = track_id
        self.max_heart_rate = max_heart_rate
        self.max_height = max_height
        self.max_speed = max_speed
        self.memory_block_index = memory_block_index
        self.min_height = min_height
        self.name = name
        self.no_laps = no_laps
        self.no_track_points = no_track_points
        self.track_points = track_points
        self.laps = laps

    def bounds(self):
        raise NotImplementedError

    def compatible_to(self, other):
        def c(a, b):
            return a is None or b is None or a == b
        return (
            c(self.ascending_height, other.ascending_height) and
            c(self.avg_heart_rate, other.avg_heart_rate) and
            c(self.calories, other.calories) and
            c(self.date, other.date) and
            c(self.descending_height, other.descending_height) and
            c(self.distance, other.distance) and
            c(self.duration, other.duration) and
            c(self.id, other.id) and
            c(self.max_heart_rate, other.max_heart_rate) and
            c(self.max_height, other.max_height) and
            c(self.max_speed, other.max_speed) and
            c(self.memory_block_index, other.memory_block_index) and
            c(self.min_height, other.min_height) and
            c(self.no_laps, other.no_laps) and
            c(self.no_track_points, other.no_track_points))

    def comlete(self):
        return len(self.track_points) == self.no_track_points

    def update_track_point_times(self):
        interval = datetime.timedelta(0)
        for tp in self.track_points:
            interval += tp.interval
            tp.time = self.date + interval
