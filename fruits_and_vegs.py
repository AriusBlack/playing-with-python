from Seasonal import seasonal
import sqlite3
import time

# def import_list():
fruit_veg = {}
# fruit_veg = pointer#import list from database

if __name__ == '__main__':


    fruit_veg = {}
    for i in range(100):
        fruit_veg = seasonal(fruit_veg)


# view list, browse by season or region depending on present month

def save_list(fruit_veg):
    #save list to database
    pass