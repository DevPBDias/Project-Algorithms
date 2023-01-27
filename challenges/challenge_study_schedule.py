def study_schedule(permanence_period, target_time):
    count = 0
    try:
        for first_hour, last_hour in permanence_period:
            if first_hour <= target_time <= last_hour:
                count += 1
        return count
    except TypeError:
        return None
