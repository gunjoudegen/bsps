import sqlite3
import tkinter as tk

def create_table(table_name):
    conn = sqlite3.connect('D:\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Saved Files (previous game)\\test data base.db')
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE {table_name} (
                    players text,
		            sub_players text,
		            team text,
		            scores integer,
		            assists integer,
		            fouls integer,
		            team_points integer,
		            team_fouls integer,
		            timeouts integer,
		            date integer)''')
    conn.commit()
    conn.close()

def create_table_wrapper():
    table_name = str(table_name_entry.get())
    create_table(table_name)

root = tk.Tk()
root.title('Create Table')
tk.Label(root, text='Enter table name:').grid(row=0, column=0)
table_name_entry = tk.Entry(root)
table_name_entry.grid(row=0, column=1)
tk.Button(root, text='Create Table', command=create_table_wrapper).grid(row=1, column=0, columnspan=2)

label = tk.Label(root, text='format: month/day/year no spaces')
label.grid(row=1, column=2)
root.mainloop()
