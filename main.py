'''
Github link: https://github.com/jonasfreyr/Assignment-8

# # # # # # #
#   #   #   #
# # # _ # # #
#   #   |   #
# # | # | # #
#   |   |   #
# # # # # # #



indexX = 1
indexY = 1

ROW1 = "N|NES|E|"
ROW2 = "N|WS|EW|"
ROW3 = "V|NS|WS|"

Notum strengi til að halda utan um rows og erum með tvö index
Notum síðan | til að skipta upp ROW í cells
'''


def get_row(indexY, row1, row2, row3):
    if indexY == 1:
        return row1

    elif indexY == 2:
        return row2

    elif indexY == 3:
        return row3

def print_directions(directions):
    string = ""
    for direction in directions:
        if direction == "N":
            string += f"({direction})orth"

        elif direction == "S":
            string += f"({direction})outh"

        elif direction == "E":
            string += f"({direction})ast"

        elif direction == "W":
            string += f"({direction})est"

        string += " or "

    # Til að taka út síðasta "or" og bæta við "."
    return string[:-4] + "."

def get_directions(indexX, row, seperator):
    index = 0
    counter = 0
    last_divider = 0
    for char in row:
        if char == seperator:
            counter += 1

            if counter == indexX:
                return row[last_divider:index]

            else:
                last_divider = index + 1

        index += 1

    return

def can_move_to_direction(indexX, row, direction):
    directions = get_directions(indexX, row, "|")

    return direction in directions

def get_new_position_for_direction(direction, indexX, indexY):
    if direction == "N":
        return indexX, indexY + 1
    elif direction == "S":
        return indexX, indexY - 1
    elif direction == "W":
        return indexX + 1, indexY
    elif direction == "E":
        return indexX - 1, indexY



indexX = 1
indexY = 1
ROW1 = "N|N|V|"
ROW2 = "NES|WS|NS|"
ROW3 = "SW|EW|ES|"
while True:
    curr_row = get_row(indexY, ROW1, ROW2, ROW3)

    if get_directions(indexX, curr_row, "|") == "V":
        print("Victory!")
        break

    print("You can travel:", print_directions(get_directions(indexX, curr_row, "|")))

    direction = input("Direction: ")
    direction = direction.upper()

    if can_move_to_direction(indexX, curr_row, direction):
        indexX, indexY = get_new_position_for_direction(direction, indexX, indexY)
    else:
        print("Not a valid direction!")
