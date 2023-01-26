# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# permanence_period[index] = student
# target_time = hour_repetition

def study_schedule(permanence_period, target_time):
    count = 0
    for first_hour, last_hour in permanence_period:
        if not first_hour or not last_hour:
            return None
        elif not isinstance(first_hour, int) or not isinstance(last_hour, int):
            return None
        elif not target_time:
            return None
        elif first_hour <= target_time <= last_hour:
            count += 1
    return count
