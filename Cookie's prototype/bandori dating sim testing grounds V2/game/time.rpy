
$ import variables as var

#to advance time, use 'call advance()'

label advance(increment = 1):
    python:
        while increment > 0:
            if time[0] == end_of_day:
                day += 1
                if day > 29 and not (month / 2) == 0:
                    day = 1
                    month +=1
                    months.append(months.pop(0))
                elif day > 30 and (month / 2) == 0:
                    day = 1
                    month +=1
                    months.append(months.pop(0))
            time.append(time.pop(0))
            increment -= 1
    return
