def street_fighter_selection(vfighters, initial_position, moves):
    init_1, init_2 = initial_position
    char_list = []

    if not len(moves):
        return []

    for i in moves:
        if i == "up":
            if init_1 != 0:
                init_1 = 0
        elif i == "down":
            if init_1 != 1:
                init_1 = 1
        elif i == "right":
            if init_2 == 5:
                init_2 = 0
            else:
                init_2 += 1
        else:
            if init_2 == 0:
                init_2 = 5
            else:
                init_2 -= 1

        char_list.append(vfighters[init_1][init_2])

    return char_list

fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]

top_row = ', '.join(fighters[0]).replace(', ', ' | ')
bottom_row = ', '.join(fighters[0]).replace(', ', ' | ')

print 'C H A R A C T E R   S E L E C T'
print top_row
print bottom_row

opts = ["up","down","right","left"]

# moves = ["down", "up", "left", "left", "up", "right"]
moves = ["up", "up", "down", "left", "left", "right", "left", "right", "right"]

print street_fighter_selection(fighters,(1,4), moves)
