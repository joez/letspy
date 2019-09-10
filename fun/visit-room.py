#!/usr/bin/env python3


def can_visit_all(rooms):
    """Can we visit all the rooms
    
    Start from room 0, each may have keys for the next one
    """
    total = len(rooms)
    visited = [False] * total
    visited[0] = True
    todo = [0]
    while todo:
        n = todo.pop()
        print(f'visit room {n}')
        for key in rooms[n]:
            if 0 <= key < total and not visited[key]:
                todo.append(key)
                print(f'find key for room {key}')
                visited[key] = True
    return all(visited)


if __name__ == '__main__':
    rooms = []
    for room in input('Input keys for each room: ').split(','):
        rooms.append(list(map(int, room.split())))
    print('Can visit all the rooms?', can_visit_all(rooms))
