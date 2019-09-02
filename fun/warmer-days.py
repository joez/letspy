#!/usr/bin/env python3


def warmer_days(temperatures):
    index_todo = []  # index of the day to search for a warmer one
    days = [0]*len(temperatures)  # 0 means no possible days to wait
    for i in range(len(temperatures)):
        while index_todo and temperatures[i] > temperatures[index_todo[-1]]:
            index_of_cold = index_todo.pop()
            days[index_of_cold] = i - index_of_cold
        index_todo.append(i)
    return days


if __name__ == '__main__':
    temperatures = list(map(int, input('Input temperatures: ').split()))
    days_to_wait = warmer_days(temperatures)
    print('Days to wait for warmer: ' + str(days_to_wait))
