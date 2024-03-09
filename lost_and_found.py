import json

USE = 'e'
EMPTY = ''
FLOOR = '_'
EXIT = 'X'
DOOR = 'D'
SECRET = 'S'
WALL = '*'
ITEMS = 'i'
STARTING_LOCATION = 'start'
PLAYER = '\u1330'

def load_map(map_file_name):
    """
        When a map file name is passed the file will load the grid and return it.
        Should you modify this function? No you shouldn't.

    :param map_file_name: a string representing the file name.
    :return: a 2D list which contains the current map.
    """
    with open(map_file_name) as map_file:
        the_map = json.loads(map_file.read())

    return the_map





def show_me_the_map(the_game_map):
    placemat = []
    for i in range(len(the_game_map)):
        x = the_game_map[i]
        for j in range(len(x)):
            placemat.append(x[j]['symbol'])

    for i in range(len(the_game_map)):
        print(str(i) + '   ', end='')
        x = the_game_map[i]

        for j in range(len(x)):
            if 'start' not in placemat:
                the_game_map[0][0]['symbol'] = 'start'

            if x[j]['symbol'] == 'start':
                print('\u1330', end='')

            elif x[j]['symbol'] == 's':
                print('*', end='')
                # if is an s then if interacted with it will turn into a door
            elif x[j]['items'] != []:
                print('i', end='')

            else:
                print(x[j]['symbol'], end='')
        print()



def tell_me_the_cordinates(the_game_map):
    yx_cord = []
    for i in range(len(the_game_map)):
        x = the_game_map[i]
        for j in range(len(x)):
            if x[j]['symbol'] == 'start':
                y_cord = i
                x_cord = j
                yx_cord.append(y_cord)
                yx_cord.append(x_cord)
    return yx_cord


def what_does_it_do(where_go,the_game_map, inventory):
    y_cord, x_cord = tell_me_the_cordinates(the_game_map)
    for i in range(len(the_game_map)):
        for j in range(len(the_game_map[i])):


            if where_go == 'w':
                if (y_cord - 1) >= 0:
                    if the_game_map[y_cord - 1][x_cord]['symbol'] == 'd':
                        return the_game_map
                    elif the_game_map[y_cord - 1][x_cord]['symbol'] == '*':
                        return the_game_map
                    elif the_game_map[y_cord - 1][x_cord]['symbol'] == 's':
                        return the_game_map
                    elif the_game_map[y_cord - 1][x_cord]['symbol'] == 'x':
                        return True
                    else:
                        the_game_map[y_cord][x_cord]['symbol'] = '_'
                        the_game_map[y_cord - 1][x_cord]['symbol'] = 'start'
                        return the_game_map
                else:
                     return the_game_map


            elif where_go == 's':
                if (y_cord + 1) < len(the_game_map):
                    if the_game_map[y_cord + 1][x_cord]['symbol'] == 'd':
                        return the_game_map
                    elif the_game_map[y_cord + 1][x_cord]['symbol'] == '*':
                        return the_game_map
                    elif the_game_map[y_cord + 1][x_cord]['symbol'] == 's':
                        return the_game_map
                    elif the_game_map[y_cord + 1][x_cord]['symbol'] == 'x':
                        return True
                    else:
                        the_game_map[y_cord][x_cord]['symbol'] = '_'
                        the_game_map[y_cord + 1][x_cord]['symbol'] = 'start'
                        return the_game_map
                else:
                     return the_game_map



            elif where_go == 'a':
                if (x_cord - 1) >= 0:
                    if the_game_map[y_cord][x_cord - 1]['symbol'] == 'd':
                        return the_game_map
                    elif the_game_map[y_cord][x_cord - 1]['symbol'] == '*':
                        return the_game_map
                    elif the_game_map[y_cord][x_cord - 1]['symbol'] == 's':
                        return the_game_map
                    elif the_game_map[y_cord][x_cord - 1]['symbol'] == 'x':
                        return True
                    else:
                        the_game_map[y_cord][x_cord]['symbol'] = '_'
                        the_game_map[y_cord][x_cord - 1]['symbol'] = 'start'
                        return the_game_map
                else:
                     return the_game_map

            elif where_go == 'd':
                if (x_cord + 1) < len(the_game_map[i]):
                    if the_game_map[y_cord][x_cord + 1]['symbol'] == 'd':
                        return the_game_map
                    elif the_game_map[y_cord][x_cord + 1]['symbol'] == '*':
                        return the_game_map
                    elif the_game_map[y_cord][x_cord + 1]['symbol'] == 's':
                        return the_game_map
                    elif the_game_map[y_cord][x_cord + 1]['symbol'] == 'x':
                        return True
                    else:
                        the_game_map[y_cord][x_cord]['symbol'] = '_'
                        the_game_map[y_cord][x_cord + 1]['symbol'] = 'start'
                        return the_game_map
                else:
                     return the_game_map





            elif where_go == 'e':
                if (y_cord - 1) >= 0:
                    if the_game_map[y_cord - 1][x_cord]['symbol'] == 's':
                        the_game_map[y_cord - 1][x_cord]['symbol'] = 'd'
                        return the_game_map
                    elif the_game_map[y_cord - 1][x_cord]['symbol'] == 'd':
                        if "requires" in (the_game_map[y_cord - 1][x_cord]):
                            if the_game_map[y_cord - 1][x_cord]["requires"]:
                                for i in range(len(the_game_map[y_cord - 1][x_cord]['requires'])):
                                    if the_game_map[y_cord - 1][x_cord]['requires'][i] in inventory:
                                        the_game_map[y_cord - 1][x_cord]['symbol'] = '_'
                                        return the_game_map
                                    else:
                                        return the_game_map
                        else:
                            the_game_map[y_cord - 1][x_cord]['symbol'] = '_'
                            return the_game_map

                if (y_cord + 1) < len(the_game_map):
                    if the_game_map[y_cord + 1][x_cord]['symbol'] == 's':
                        the_game_map[y_cord + 1][x_cord]['symbol'] = 'd'
                        return the_game_map
                    elif the_game_map[y_cord + 1][x_cord]['symbol'] == 'd':
                        if "requires" in (the_game_map[y_cord + 1][x_cord]):
                            if the_game_map[y_cord + 1][x_cord]["requires"]:
                                for i in range(len(the_game_map[y_cord + 1][x_cord]['requires'])):
                                    if the_game_map[y_cord + 1][x_cord]['requires'][i] in inventory:
                                        the_game_map[y_cord + 1][x_cord]['symbol'] = '_'
                                        return the_game_map
                                    else:
                                        return the_game_map
                        else:
                            the_game_map[y_cord + 1][x_cord]['symbol'] = '_'
                            return the_game_map

                if (x_cord - 1) >= 0:
                    if the_game_map[y_cord][x_cord - 1]['symbol'] == 's':
                        the_game_map[y_cord][x_cord - 1]['symbol'] = 'd'
                        return the_game_map
                    elif the_game_map[y_cord][x_cord - 1]['symbol'] == 'd':
                        if "requires" in (the_game_map[y_cord][x_cord - 1]):
                            if the_game_map[y_cord][x_cord - 1]["requires"]:
                                for i in range(len(the_game_map[y_cord][x_cord - 1]['requires'])):
                                    if the_game_map[y_cord][x_cord - 1]['requires'][i] in inventory:
                                        the_game_map[y_cord][x_cord - 1]['symbol'] = '_'
                                        return the_game_map
                                    else:
                                        return the_game_map
                        else:
                            the_game_map[y_cord][x_cord - 1]['symbol'] = '_'
                            return the_game_map

                if (x_cord + 1) < len(the_game_map[i]):
                    if the_game_map[y_cord][x_cord + 1]['symbol'] == 's':
                        the_game_map[y_cord][x_cord + 1]['symbol'] = 'd'
                        return the_game_map
                    elif the_game_map[y_cord][x_cord + 1]['symbol'] == 'd':
                        if "requires" in (the_game_map[y_cord][x_cord + 1]):
                            if the_game_map[y_cord][x_cord + 1]["requires"]:
                                for i in range(len(the_game_map[y_cord][x_cord + 1]['requires'])):
                                    if the_game_map[y_cord][x_cord + 1]['requires'][i] in inventory:
                                        the_game_map[y_cord][x_cord + 1]['symbol'] = '_'
                                        return the_game_map
                                    else:
                                        return the_game_map
                        else:
                            the_game_map[y_cord][x_cord + 1]['symbol'] = '_'
                            return the_game_map

                if (x_cord + 1) < len(the_game_map[i]) and (y_cord + 1) < len(the_game_map):
                    if the_game_map[y_cord + 1][x_cord + 1]['symbol'] == 's':
                        the_game_map[y_cord + 1][x_cord + 1]['symbol'] = 'd'
                        return the_game_map
                    elif the_game_map[y_cord + 1][x_cord + 1]['symbol'] == 'd':
                        if "requires" in (the_game_map[y_cord + 1][x_cord + 1]):
                            if the_game_map[y_cord + 1][x_cord + 1]["requires"]:
                                for i in range(len(the_game_map[y_cord + 1][x_cord + 1]['requires'])):
                                    if the_game_map[y_cord + 1][x_cord + 1]['requires'][i] in inventory:
                                        the_game_map[y_cord + 1][x_cord + 1]['symbol'] = '_'
                                        return the_game_map
                                    else:
                                        return the_game_map
                        else:
                            the_game_map[y_cord + 1][x_cord + 1]['symbol'] = '_'
                            return the_game_map

                if (x_cord - 1) >= 0 and (y_cord + 1) < len(the_game_map):
                    if the_game_map[y_cord + 1][x_cord - 1]['symbol'] == 's':
                        the_game_map[y_cord + 1][x_cord - 1]['symbol'] = 'd'
                        return the_game_map
                    elif the_game_map[y_cord + 1][x_cord - 1]['symbol'] == 'd':
                        if "requires" in (the_game_map[y_cord + 1][x_cord - 1]):
                            if the_game_map[y_cord + 1][x_cord - 1]["requires"]:
                                for i in range(len(the_game_map[y_cord + 1][x_cord - 1]['requires'])):
                                    if the_game_map[y_cord + 1][x_cord - 1]['requires'][i] in inventory:
                                        the_game_map[y_cord + 1][x_cord - 1]['symbol'] = '_'
                                        return the_game_map
                                    else:
                                        return the_game_map
                        else:
                            the_game_map[y_cord + 1][x_cord - 1]['symbol'] = '_'
                            return the_game_map

                if (x_cord - 1) >= 0 and (y_cord - 1) >= 0:
                    if the_game_map[y_cord - 1][x_cord - 1]['symbol'] == 's':
                        the_game_map[y_cord - 1][x_cord - 1]['symbol'] = 'd'
                        return the_game_map
                    elif the_game_map[y_cord - 1][x_cord - 1]['symbol'] == 'd':
                        if "requires" in (the_game_map[y_cord - 1][x_cord - 1]):
                            if the_game_map[y_cord - 1][x_cord - 1]["requires"]:
                                for i in range(len(the_game_map[y_cord - 1][x_cord - 1]['requires'])):
                                    if the_game_map[y_cord - 1][x_cord - 1]['requires'][i] in inventory:
                                        the_game_map[y_cord - 1][x_cord - 1]['symbol'] = '_'
                                        return the_game_map
                                    else:
                                        return the_game_map
                        else:
                            the_game_map[y_cord - 1][x_cord - 1]['symbol'] = '_'
                            return the_game_map


                if (x_cord + 1) < len(the_game_map[i]) and (y_cord - 1) >= 0:
                    if the_game_map[y_cord - 1][x_cord + 1]['symbol'] == 's':
                        the_game_map[y_cord - 1][x_cord + 1]['symbol'] = 'd'
                        return the_game_map
                    elif the_game_map[y_cord - 1][x_cord + 1]['symbol'] == 'd':
                        if "requires" in (the_game_map[y_cord - 1][x_cord + 1]):
                            if the_game_map[y_cord - 1][x_cord + 1]["requires"]:
                                for i in range(len(the_game_map[y_cord - 1][x_cord + 1]['requires'])):
                                    if the_game_map[y_cord - 1][x_cord + 1]['requires'][i] in inventory:
                                        the_game_map[y_cord - 1][x_cord + 1]['symbol'] = '_'
                                        return the_game_map
                                    else:
                                        return the_game_map
                        else:
                            the_game_map[y_cord - 1][x_cord + 1]['symbol'] = '_'
                            return the_game_map

def play_game(the_game_map):
    end_game = False
    show_me_the_map(the_game_map)
    inventory = []

    while end_game == False:
        y_cord, x_cord = tell_me_the_cordinates(the_game_map)
        if the_game_map[y_cord][x_cord]['items'] != []:
            for i in range(len(the_game_map[y_cord][x_cord]['items'])):
                inventory.append(the_game_map[y_cord][x_cord]['items'][i])
                the_game_map[y_cord][x_cord]['items'] = []


        command_list = ['a','s','w','d','q','e']
        print('Your inventory is:' , ' '.join(inventory))
        where_go = input('Enter Move (wasd) (e to activate doors or secrets, q to exit the game): ')
        while where_go not in command_list:
            show_me_the_map(the_game_map)
            print('Your inventory is:', ' '.join(inventory))
            where_go = input('Enter Move (wasd) (e to activate doors or secrets, q to exit the game): ')
        if where_go in command_list:
            if where_go == 'q':
                print('You have died')
                end_game = True
            if what_does_it_do(where_go, the_game_map, inventory) != True:
                show_me_the_map(the_game_map)
            else:
                print('You won!')
                end_game = True


if __name__ == '__main__':
    map_file_name = input('What map do you want to load? ')
    the_game_map = load_map(map_file_name)
    if the_game_map:
        play_game(the_game_map)
