class Time:
    """
    Represents the time of day.

    attributes: hour, minute, second
    """
    # inside class Time:

    def __init__(self, hour=0, minute=0, second=0): 
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)

    # inside class Time:

    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def print_time(self):
        print('{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second))

    def time_to_int(self):
        """Computes the number of seconds since midnight.

        time: Time object.
        """
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds):
        """Adds seconds to a Time object."""
        result = Time()
        result.hour, result.minute, result.second = self.hour, self.minute, self.second
        result.second += seconds

        if result.second >= 60:
            result.second -= 60
            result.minute += 1

        if result.minute >= 60:
            result.minute -= 60
            result.hour += 1
        return result

    # inside class Time:

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()
    
    # To use this method, you have to invoke it on one object 
    # and pass the other as an argument:


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """

    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)

    return Time(hour, minute, second)



start = Time()
start.hour = 15
start.minute = 18
start.second = 50

start.print_time()
print(start.time_to_int())

end = start.increment(2000)
end.print_time()
print(end.is_after(start))

traffic = Time(0, 30, 0)

expected_time = Time(10, 15, 0)

print(traffic)
print(expected_time)

print(start + traffic)
# traffic.print_time()
# expected_time.print_time()
# print(start.is_as_expected(traffic, expected_time))

# default_time = Time()
# default_time.print_time()
