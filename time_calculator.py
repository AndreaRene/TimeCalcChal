def add_time(start, duration, weekday = 'default'):
    start_time, meridiem = start.split()
    start_hour, start_min = map(int, start_time.split(':'))
    dur_hour, dur_min = map(int, (duration.split(':')))
    days, modulus = divmod(dur_hour, 24)
  
    if meridiem == 'PM' and start_hour != 12:
        start_hour += 12
    elif meridiem == 'AM' and start_hour == 12:
        start_hour = 0

    new_hour = start_hour + modulus
    new_min = start_min + dur_min

    if start_min + dur_min >= 60:
        new_min -= 60
        new_hour += 1
    if new_hour >= 24:
        new_hour -= 24
        days += 1

    meridiem = ['AM', 'PM'][new_hour // 12]
    new_hour %= 12
    new_hour = 12 if new_hour == 0 else new_hour
  
    new_time_list = [f'{new_hour}:{new_min:02} {meridiem}']

    day_switch = {
        0 : 'monday',
        1 : 'tuesday',
        2 : 'wednesday',
        3 : 'thursday',
        4 : 'friday',
        5 : 'saturday',
        6 : 'sunday'
    }
    if weekday != 'default':
        day_index = [v for k, v in day_switch.items()].index(weekday.lower())
        new_day_index = (day_index + days) % 7
        new_day = day_switch[new_day_index]
        new_time_list.append(f', {new_day.capitalize()}')


    if days == 1:
        new_time_list.append(' (next day)')
    elif days > 1:
        new_time_list.append(f' ({days} days later)')

    return ''.join(new_time_list).strip()
