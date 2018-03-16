#Display fruits and vegetables in season


import time
import sqlite3

season = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

fruit_type = ("Fruit", "Vegetable")

region = {
    "America" : ("East Coast", "West Coast", "Southern", "Latin"),
    "Europe" : ("West", "East", "Mediterranean"),
    "Asia" : ("East", "South East")
}

# Builder for fruit_veg list
def seasonal(fruit_veg):
    print ("Welcome to the builder, you can build your list of fruits here\n")
    answer = input("Would you like to create a new fruit or QUIT? \n")
    if answer != 'QUIT':

        name = get_name()
        t = get_type()
        r = get_region()
        s = get_season()
        info = (t, r, s)
        fruit_veg[name] = info

        for key in fruit_veg.keys():
            info = fruit_veg.get(key, None)
            prompt = "{} is a {} that grows in {} from {} to {}".format(
                key,
                info[0],
                '{} {}'.format(info[1][1], info[1][0]),
                info[2][0],
                info[2][-1],
            )
            print(prompt)

        return fruit_veg
    else:

        conn = sqlite3.connect("example.db")
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS seasonal
              (name text, type text, region text, subregion text, 
               season_start integer, season_end integer)""")
        conn.commit()
        conn.close()
        # cursor.execute("""INSERT INTO seasonal(name, type, region,
        #         subregion, season_start, season_end)""")
        exit(1)
#Setter for region
def get_region():
    for c, value in enumerate(region, 1):
        print("{}. {}".format(c, value))

    this_region = input("Choose a region:\n ").capitalize()
    sub = region[this_region]

    for c, value in enumerate(sub, 1):
        print("{}. {}".format(c, value))

    this_sub_region = input("Choose a sub region: \n ").title()
    print("region : {} - {}".format(this_region, this_sub_region))

    return (this_region, this_sub_region)

#Setter for name
def get_name():
    name = input("Enter a name: ").capitalize()
    print("You entered: {} \n".format(name))
    return name

def input_forever(prompt):
    picking = True
    while picking:
        inp = input(prompt)
        try:
            this_season = int(inp)
            picking = False
        except ValueError:
            print("Could not recognise input, not a valid int: '{}'".format(inp))
            continue
    return this_season

#Setter for season
def get_season():
    for c, value in enumerate(season, 1):
        print("{}. {}".format(c, value))

    this_season_start = input_forever("Pick a start season range(eg : 4:8 = April to August)\nSeason Beginning:\n ")
    this_season_end = input_forever("Season End: \n")

    this_season = season[this_season_start-1:this_season_end]
    print(" season : {}".format(this_season))

    return this_season

#Setter for type
def get_type():
    prompt = "Pick a type:\n{}, {}\n".format(fruit_type[0], fruit_type[1])
    this_type = input(prompt).capitalize()
    return this_type


if __name__ == '__main__':
    fruit_veg = {}
    for i in range(100):
        fruit_veg = seasonal(fruit_veg)
