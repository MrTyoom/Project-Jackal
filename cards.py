from constants import *
from collections import namedtuple
import constants


coord = namedtuple("Coord", "x y")
prt1 = [_ for _ in range(3)]
prt2 = [_ for _ in range(3, 6)]


def update_const():
    constants.MOVE += 1
    constants.TMP = 0


def some_sum(x: list):
    return sum([1 for _ in x if isinstance(_, Pirate)])


def update_tile(was: Tile, go: Tile, pirate: Pirate):
    go.pirates[pirate.number] = pirate
    was.pirates[pirate.number] = 0


def gold(was: Tile, go: Tile, pirate: Pirate):
    if go.closed:
        go.closed = 0
        go.pirates[pirate.number] = pirate
        pirate.gold += 1
        go.gold += go.code - 13
        was.pirates[pirate.number] = 0
    else:
        go.pirates[pirate.number] = pirate
        was.pirates[pirate.number] = 0


def nothing(was: Tile, go: Tile, pirate: Pirate):
    if go.closed:
        go.closed = 0

    update_tile(was, go, pirate)


def cannibal(was: Tile, go: Tile, pirate: Pirate):
    if go.closed:
        go.closed = 0

    was.pirates[pirate.number] = 0
    GLOBAL_PIRATES[pirate.number].live = 0


# may be make thing, that pirate don't go for this tile, just tile opens and pirate stays where he was
def croc(was: Tile, go: Tile, pirate: Pirate):
    if go.closed:
        go.closed = 0

    # try to put pirate in the new tile, and then go back
    update_tile(was, go, pirate)

    go.pirates[pirate.number] = 0
    was.pirates[pirate.number] = pirate


def horse(was: Tile, go: Tile, pirate: Pirate):
    if go.closed:
        go.closed = 0
        update_tile(was, go, pirate)

        print("write, where do you want to go")
        info = list(map(int, input().split()))

        tile = coord(x=info[0], y=info[1])

        if tile.x > len(WORLD_MAP[0]) - 1 or tile.x < 0 or tile.y > len(WORLD_MAP) - 1 or tile.y < 0 or \
                WORLD_MAP[tile.x][tile.y] == 0:
            print('Wrong tile, please check correctness')

        if go.x + 1 == tile.x:
            if go.y + 2 == tile.y:
                return WORLD_MAP[tile.x][tile.y]

            if go.y - 2 == tile.y:
                return WORLD_MAP[tile.x][tile.y]

        if go.x - 1 == tile.x:
            if go.y + 2 == tile.y:
                return WORLD_MAP[tile.x][tile.y]
            if go.y - 2 == tile.y:
                return WORLD_MAP[tile.x][tile.y]

        if go.x - 2 == tile.x:
            if go.y - 1 == tile.y:
                return WORLD_MAP[tile.x][tile.y]
            if go.y + 1 == tile.y:
                return WORLD_MAP[tile.x][tile.y]

        if go.x + 2 == tile.x:
            if go.y - 1 == tile.y:
                return WORLD_MAP[tile.x][tile.y]
            if go.y + 1 == tile.y:
                return WORLD_MAP[tile.x][tile.y]

        print("You enter incorrect data, please, try again")


def cannon(was: Tile, go: Tile, pirate: Pirate):
    if go.closed:
        go.closed = 0

    update_tile(was, go, pirate)

    WORLD_MAP[0][go.x].pirates[pirate.number] = pirate
    go.pirates[pirate.number] = 0


def castle(was: Tile, go: Tile, pirate: Pirate):
    if go.closed:
        go.closed = 0
        update_tile(was, go, pirate)
    else:
        if pirate.team == 1:
            if some_sum(go.pirates[3:]) > 0:
                print("you can't go in the castle because opponent captured it")
            else:
                update_tile(was, go, pirate)

        else:
            if some_sum(go.pirates[:3]) > 0:
                print("you can't go in the castle because opponent captured it")
            else:
                update_tile(was, go, pirate)


def castle_girl(was: Tile, go: Tile, pirate: Pirate):
    if go.closed:
        go.closed = 0

        update_tile(was, go, pirate)
        if pirate.team == 1:
            lst = prt1
        else:
            lst = prt2

        for prt in lst:
            if GLOBAL_PIRATES[prt].live == 0:
                GLOBAL_PIRATES[prt].live = 1
                break
    else:
        if some_sum(go.pirates) > 0:
            if pirate.team == 1:
                if some_sum(go.pirates[3:]) > 0:
                    print("you can't go in the castle because opponent captured it")
                else:
                    update_tile(was, go, pirate)
            else:
                if some_sum(go.pirates[:3]) > 0:
                    print("you can't go in the castle because opponent captured it")
                else:
                    update_tile(was, go, pirate)
        else:
            update_tile(was, go, pirate)


def trap(was: Tile, go: Tile, pirate: Pirate):
    if go.closed:
        go.closed = 0

        update_tile(was, go, pirate)
        pirate.move_possib = 0

    else:
        if some_sum(go.pirates) == 0:
            update_tile(was, go, pirate)
        elif some_sum(go.pirates) == 1:
            if some_sum(go.pirates[3:]) > 0:
                if pirate.team == 1:

                    # try to beat pirate from tile
                    for k in go.pirates:
                        if isinstance(k, Pirate):
                            WORLD_MAP[SHIP2_COORD['x']][SHIP2_COORD['y']].pirates[
                                k.number] = k  # pirate go back to the ship
                            go.pirates[k.number] = 0
                            break
                else:
                    # reveal teammate
                    for k in go.pirates:
                        if isinstance(k, Pirate):
                            k.move_possib = 1
                            update_tile(was, go, pirate)
            else:
                if pirate.team == 1:
                    for k in go.pirates:
                        if isinstance(k, Pirate):
                            k.move_possib = 1
                            update_tile(was, go, pirate)
                else:
                    for k in go.pirates:
                        if isinstance(k, Pirate):
                            WORLD_MAP[SHIP1_COORD['x']][SHIP1_COORD['y']].pirates[k.number] = k
                            go.pirates[k.number] = 0
                            break

        else:
            if some_sum(go.pirates[3:]) > 0:
                if pirate.team == 1:
                    print("You can't go this tile")
                else:
                    update_tile(was, go, pirate)
            else:
                if pirate.team == 1:
                    update_tile(was, go, pirate)
                else:
                    print("You can't go this tile")


def labyrinth(was: Tile, go: Tile, pirate: Pirate, move: int):
    if go.closed:
        go.closed = 0

    update_tile(was, go, pirate)
    pirate.move_possib = move + 1


def barrel(was: Tile, go: Tile, pirate: Pirate):
    if go.closed:
        go.closed = 0

    update_tile(was, go, pirate)
    pirate.move_possib = 2


def balloon(was: Tile, go: Tile, pirate: Pirate):
    if go.closed:
        go.closed = 0

    update_tile(was, go, pirate)

    if pirate.team == 1:
        WORLD_MAP[SHIP1_COORD['y']][SHIP1_COORD['x']].pirates[pirate.number] = pirate
    else:
        WORLD_MAP[SHIP2_COORD['y']][SHIP2_COORD['x']].pirates[pirate.number] = pirate

    go.pirates[pirate.number] = 0


def arrow(was: Tile, go: Tile, pirate: Pirate, code: int):
    if go.closed:
        go.closed = 0

    if code == 1 and constants.TMP == 1:
        update_tile(was, go, pirate)
        go.pirates[pirate.number] = 0
        WORLD_MAP[go.y][go.x + 1].pirates[pirate.number] = pirate
        update_const()
        return WORLD_MAP[go.y][go.x + 1]
    elif code == 2 and constants.TMP == 1:
        update_tile(was, go, pirate)
        go.pirates[pirate.number] = 0
        update_const()
        print('Choose where you want to go')
        a = input()
        if a == 'l':
            WORLD_MAP[go.y][go.x - 1].pirates[pirate.number] = pirate
            return WORLD_MAP[go.y][go.x - 1]
        else:
            WORLD_MAP[go.y][go.x + 1].pirates[pirate.number] = pirate
            return WORLD_MAP[go.y][go.x + 1]
    elif code == 3 and constants.TMP == 1:
        update_tile(was, go, pirate)
        go.pirates[pirate.number] = 0
        WORLD_MAP[go.y - 1][go.x + 1].pirates[pirate.number] = pirate
        update_const()
        return WORLD_MAP[go.y - 1][go.x + 1]
    elif code == 4 and constants.TMP == 1:
        update_tile(was, go, pirate)
        go.pirates[pirate.number] = 0
        update_const()
        print('Choose where you want to go')
        a = input()
        if a == 'r':
            WORLD_MAP[go.y - 1][go.x + 1].pirates[pirate.number] = pirate
            return WORLD_MAP[go.y - 1][go.x + 1].pirates[pirate.number]
        else:
            WORLD_MAP[go.y + 1][go.x - 1].pirates[pirate.number] = pirate
            return WORLD_MAP[go.y + 1][go.x - 1].pirates[pirate.number]
    elif code == 5 and constants.TMP == 1:
        update_tile(was, go, pirate)
        go.pirates[pirate.number] = 0
        update_const()
        print('Choose where you want to go')
        a = input()
        if a == 'r':
            WORLD_MAP[go.y][go.x + 1].pirates[pirate.number] = pirate
            return WORLD_MAP[go.y][go.x + 1].pirates[pirate.number]
        elif a == 'l':
            WORLD_MAP[go.y][go.x - 1].pirates[pirate.number] = pirate
            return WORLD_MAP[go.y][go.x - 1].pirates[pirate.number]
        elif a == 'u':
            WORLD_MAP[go.y + 1][go.x].pirates[pirate.number] = pirate
            return WORLD_MAP[go.y + 1][go.x].pirates[pirate.number]
        else:
            WORLD_MAP[go.y - 1][go.x].pirates[pirate.number] = pirate
            return WORLD_MAP[go.y - 1][go.x].pirates[pirate.number]
    elif code == 6 and constants.TMP == 1:
        update_tile(was, go, pirate)
        go.pirates[pirate.number] = 0
        update_const()
        print('Choose where you want to go')
        a = input()
        if a == 'u':
            WORLD_MAP[go.y + 1][go.x].pirates[pirate.number] = pirate
            return WORLD_MAP[go.y + 1][go.x].pirates[pirate.number]
        elif a == 'r':
            WORLD_MAP[go.y][go.x + 1].pirates[pirate.number] = pirate
            return WORLD_MAP[go.y][go.x + 1].pirates[pirate.number]
        else:
            WORLD_MAP[go.y - 1][go.x - 1].pirates[pirate.number] = pirate
            return WORLD_MAP[go.y - 1][go.x - 1].pirates[pirate.number]
    elif code == 7 and constants.TMP == 1:
        update_tile(was, go, pirate)
        go.pirates[pirate.number] = 0
        update_const()
        print('Choose where you want to go')
        a = input()
        if a == 'ru':
            WORLD_MAP[go.y - 1][go.x + 1].pirates[pirate.number] = pirate
            return WORLD_MAP[go.y - 1][go.x + 1].pirates[pirate.number]
        elif a == 'lu':
            WORLD_MAP[go.y - 1][go.x - 1].pirates[pirate.number] = pirate
            return WORLD_MAP[go.y - 1][go.x - 1].pirates[pirate.number]
        elif a == 'rd':
            WORLD_MAP[go.y + 1][go.x + 1].pirates[pirate.number] = pirate
            return WORLD_MAP[go.y + 1][go.x + 1].pirates[pirate.number]
        else:
            WORLD_MAP[go.y - 1][go.x + 1].pirates[pirate.number] = pirate
            return WORLD_MAP[go.y - 1][go.x + 1].pirates[pirate.number]


def plane(was: Tile, go: Tile, pirate: Pirate):
    if go.closed:
        go.closed = 0

    update_tile(was, go, pirate)
    print("Where you want to go")
    a, b = list(map(int, input().split()))

    WORLD_MAP[a - 1][b - 1].pirates[pirate.number] = pirate
    go.pirates[pirate.number] = 0
    return WORLD_MAP[a - 1][b - 1]

# def ice(was: Tile, go: Tile, pirate: Pirate):
#     pass
#
#

