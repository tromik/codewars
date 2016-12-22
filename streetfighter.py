def street_fighter_selection(vfighters, initial_position, moves):
    top = fighters[0]
    bottom = fighters[1]
    init_1, init_2 = initial_position
    
    for i in moves:
        if i == "up":
            if init_1 != 0:
                current_row = top
        elif i == "down":
            if init_1 != 1:
                current_row = bottom
    print current





fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]


opts = ["up","down","right","left"]

moves = ["down", "up", "left", "left", "up", "right"]

street_fighter_selection(fighters,(0,0), moves)
