import sqlite3
import datetime

from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage, Image
from tkinter import filedialog

from PIL import ImageTk, Image
import os
import webbrowser


datern = datetime.datetime.today()


print('------------ program started -----------', datern)
main = Tk()

def mainscoreboard():

    def helplabelIN(event):
        helplabel['text'] = '[TAB] - scoreboard\n[left CTRL] - control panel'

    def helplabelOUT(event):
        helplabel['text'] = ' '


    main_sb = Toplevel(main)    
    main_sb.title('main scoreboard navigation page')
    main_sb.geometry('1920x1080+0+0')
    main_sb.iconphoto(True, mainicon)

    global mainsb_bg
    mainsb_bg = ImageTk.PhotoImage(Image.open('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\backgrounds\\main game file\\audience perspective 1 - main.jpg'))
    mainsb_canvas = Canvas(main_sb, width=1920, height=1080)
    mainsb_canvas.pack(fill='both')
    mainsb_canvas.create_image(0, 0, anchor='nw', image=mainsb_bg)

    helpbutton = Button(main_sb, text='?', font=('Consolas', 30), bg="#585858", activebackground="#585858", fg='BLACK', activeforeground='BLACK',
                        cursor='hand2', relief=FLAT)
    helpbutton.bind('<Enter>', helplabelIN)
    helpbutton.bind('<Leave>', helplabelOUT)
    helpbutton.place(x=1700, y=850)

    helplabel = Label(main_sb, text=' ', font=('Consolas', 12), bg='#585858', fg='BLACK', justify=LEFT)
    helplabel.place(x=1500, y=910)

    q_indicator1 = Frame(main_sb, width=53, height=20, bg='#585858')
    q_indicator1.place(x=833, y=788)
    q_indicator2 = Frame(main_sb, width=53, height=20, bg='#585858')
    q_indicator2.place(x=893, y=788)
    q_indicator3 = Frame(main_sb, width=53, height=20, bg='#585858')
    q_indicator3.place(x=951, y=788)
    q_indicator4 = Frame(main_sb, width=53, height=20, bg='#585858')
    q_indicator4.place(x=1010, y=788)

def gsuplayerdata():
    print('--------- input player data page ---------', datern)
    global playsetup_bg

    def addplayer():

        def addplayer_click():
        
            
            mainbase = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\database\\basketball_maindb.db')
            titlebase = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\database\\basketball_titledb.db')
            cur = mainbase.cursor()
            cur2 = titlebase.cursor()

            cur2.execute("SELECT * from dbstrings")
            loop = cur2.fetchall()

            temp = ""

            for i in loop:
                 temp += i[0]

            read = loop[-1][0]
            cur.execute(f"""INSERT INTO {read} VALUES(
                        :fname,
                        :lname,
                        :school,
                        :birthday,
                        :height,
                        :weight,
                        :bmi,
                        :team,
                        :region,
                        :role
            )""",{
                'fname': fn,
                'lname': ln,
                'school': sc,
                'birthday': bd,
                'height':h,
                'weight':w,
                'bmi':bmi,
                'team':tn,
                'region':r,
                'role': rol
            })


            titlebase.commit()
            titlebase.close()
            mainbase.commit()
            mainbase.close()

            print('player added succesfully')
            fn_entry.delete(0, END)
            ln_entry.delete(0, END)
            sc_entry.delete(0, END)
            height_entry.delete(0, END)
            weight_entry.delete(0, END)
            team_name.delete(0, END)
            region.delete(0, END)

            bd_entry['state'] = NORMAL
            bmi_entry['state'] = NORMAL
            role['state'] = NORMAL

            bd_entry.delete(0, END)
            bmi_entry.delete(0, END)
            role.delete(0, END)

            bd_entry['state'] = DISABLED
            bmi_entry['state'] = DISABLED
            role['state'] = DISABLED

            """
            cen1.get()
            cen2.get()
            pf1.get()
            pf2.get()
            sf1.get()
            sf2.get()
            pg1.get()
            pg2.get()
            sg1.get()
            sg2.get()

            ['Center',
            'Power Forward',
            'Small Forward',
            'Point Guard',
            'Shooting Guard',
            'substitute player']
            """

            if wt.get() == 'click here to choose which team':
                
                if messagebox.showerror(title='error args', message='no team selected please check the todo list manually'):
                    pass
            
            else:

                if wt.get() == 'team 1':

                    if rol == 'Center':
                        cen1.set(1)
                    
                    elif rol == 'Power Forward':
                        pf1.set(1)

                    elif rol == 'Small Forward':
                        sf1.set(1)

                    elif rol == 'Point Guard':
                        pg1.set(1)

                    elif rol == 'Shooting Guard':
                        sg1.set(1)

                    elif rol == 'substitute player':
                        pass
            
                elif wt.get() == 'team 2':

                    if rol == 'Center':
                        cen2.set(1)
                    
                    elif rol == 'Power Forward':
                        pf2.set(1)

                    elif rol == 'Small Forward':
                        sf2.set(1)

                    elif rol == 'Point Guard':
                        pg2.set(1)

                    elif rol == 'Shooting Guard':
                        sg2.set(1)

                    elif rol == 'substitute player':
                        pass

            confirm_player.destroy()           
            

        birthdayviewer()
        bmi_viewerfunction()
        role_viewerfunction()

        fn = fn_entry.get()
        ln = ln_entry.get()
        sc = sc_entry.get()
        h = height_entry.get()
        w = weight_entry.get()
        tn = team_name.get()
        r = region.get()
        bd = bd_entry.get()
        bmi = bmi_entry.get()
        rol = role.get()


        wholename = fn +' '+ ln 

        confirm_player = Toplevel(main)
        confirm_player.geometry('500x500+120+0')
        confirm_player.resizable(FALSE, FALSE)
        confirm_player.transient(main)
        confirm_player.title('CONFIRM TO ADD PLAYER')
        confirm_player.iconphoto(True, mainicon)
        global addplayer_bg
        addplayer_bg = ImageTk.PhotoImage(Image.open('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\backgrounds\\main game file\\addplayer_GSU.png'))
        addplayer_canv = Canvas(confirm_player, width=500, height=500)
        addplayer_canv.pack(fill='both')
        addplayer_canv.create_image(0, 0, anchor='nw', image=addplayer_bg)

        confirm_add = Button(confirm_player, text='confirm add >', relief=SOLID, bg='#b7630b', activebackground='#b7630b', activeforeground='WHITE',
                             cursor='hand2', command=addplayer_click)
        confirm_add.place(x=395, y=455)


        entry_name = Entry(confirm_player, fg='BLACK', bg='#B7630B', font=('Gill Sans MT', 11),
                     cursor='xterm', width=45, relief=SOLID, highlightbackground="BLACK", borderwidth=0,)
        entry_name.place(x=20, y=92)
        entry_school = Entry(confirm_player, fg='BLACK', bg='#B7630B', font=('Gill Sans MT', 11),
                     cursor='xterm', width=45, relief=SOLID, highlightbackground="BLACK", borderwidth=0)
        entry_school.place(x=20, y=122)
        entry_birthday = Entry(confirm_player, fg='BLACK', bg='#B7630B', font=('Gill Sans MT', 11),
                     cursor='xterm', width=45, relief=SOLID, highlightbackground="BLACK", borderwidth=0)
        entry_birthday.place(x=20, y=152)
        entry_sex = Entry(confirm_player, fg='BLACK', bg='#B7630B', font=('Gill Sans MT', 11),
                     cursor='xterm', width=45, relief=SOLID, highlightbackground="BLACK", borderwidth=0)
        entry_sex.place(x=20, y=182)

        entry_height = Entry(confirm_player, fg='BLACK', bg='#B7630B', font=('Gill Sans MT', 11),
                     cursor='xterm', width=45, relief=SOLID, highlightbackground="BLACK", borderwidth=0)
        entry_height.place(x=20, y=212)
        entry_weight = Entry(confirm_player, fg='BLACK', bg='#B7630B', font=('Gill Sans MT', 11),
                     cursor='xterm', width=45, relief=SOLID, highlightbackground="BLACK", borderwidth=0)
        entry_weight.place(x=20, y=242)
        entry_bmi = Entry(confirm_player, fg='BLACK', bg='#B7630B', font=('Gill Sans MT', 11),
                     cursor='xterm', width=45, relief=SOLID, highlightbackground="BLACK", borderwidth=0)
        entry_bmi.place(x=20, y=272)

        entry_team = Entry(confirm_player, fg='BLACK', bg='#B7630B', font=('Gill Sans MT', 11),
                     cursor='xterm', width=45, relief=SOLID, highlightbackground="BLACK", borderwidth=0)
        entry_team.place(x=20, y=302)
        entry_region = Entry(confirm_player, fg='BLACK', bg='#B7630B', font=('Gill Sans MT', 11),
                     cursor='xterm', width=45, relief=SOLID, highlightbackground="BLACK", borderwidth=0)
        entry_region.place(x=20, y=332)
        entry_role = Entry(confirm_player, fg='BLACK', bg='#B7630B', font=('Gill Sans MT', 11),
                     cursor='xterm', width=45, relief=SOLID, highlightbackground="BLACK", borderwidth=0)
        entry_role.place(x=20, y=362)

        entry_name.insert(0, wholename)
        entry_school.insert(0, sc)
        entry_birthday.insert(0, bd)
        #entry_sex.insert(0, sex)
        entry_height.insert(0, h)
        entry_weight.insert(0, w)
        entry_bmi.insert(0, bmi)
        entry_team.insert(0, tn)
        entry_region.insert(0, r)
        entry_role.insert(0, rol)

    def confirm_players():
        if messagebox.askokcancel(title= 'CONFIRM PLAYER SETUP', message= 'do a double check!,\nall of these will be submitted and you will proceed to the scoreboard'):


            c1 = cen1.get()
            c2 = cen2.get()
            p1 = pf1.get()
            p2 = pf2.get()
            s1 = sf1.get()
            s2 = sf2.get()
            pp1 = pg1.get()
            pp2 = pg2.get()
            ss1 = sg1.get()
            ss2 = sg2.get()

            if c1 == 1 and c2 == 1 and p1 == 1 and p2 == 1 and s1 == 1 and s2 == 1 and pp1 == 1 and pp2 == 1 and ss1 == 1 and ss2 == 1:
                print('no error')
                mainscoreboard()


            else:

                if messagebox.showerror(title= 'MISSING A PLAYER', message= 'i think you have missed a player or maybe you forgot to check\nthe boxes you are instructed to check'):
                    pass

                else:
                    pass

        else:
            pass


    def backtohomepage():
        if messagebox.askyesno(title= 'go back to homepage', message= 'your progress will be lost!, \n do you really want to leave this page?'):
            playsetup.destroy()

        else:
            pass

    def clearallentries():
        if messagebox.askokcancel(title= 'removing everything you have entered', message= 'do you really want to remove everything?'):
            fn_entry.delete(0, END)
            ln_entry.delete(0, END)
            sc_entry.delete(0, END)
            height_entry.delete(0, END)
            weight_entry.delete(0, END)
            team_name.delete(0, END)
            region.delete(0, END)


        else:
            messagebox.showinfo(title= 'progress restored', message= 'entries reset cancelled')

    def role_viewerfunction():
        norolepicked = 'choose a role below'
        rolefetch = rolevar.get()

        if rolefetch == 'PLAYER GAME ROLE/POSITION      ':
            role['state'] = NORMAL
            
            role.delete(0, END)
            role.insert(0, norolepicked)
            
            role['state'] = DISABLED
        else:
            role['state'] = NORMAL
            
            role.delete(0, END)
            role.insert(0, rolefetch)
            
            role['state'] = DISABLED

    def bmi_viewerfunction():
        
        classification = ['underweight -18.5', 'normal 18.5+', 'overweight 25+', 'obesity(class-1) 30+', 'obesity(class-2) 35+', 'obesity(class-3) 40+']

        inheight = height_entry.get()
        inweight = weight_entry.get()

        try:
            ftconv = float(inheight) * 0.3048

            #bmi
            bmi_res = float(inweight) / float(ftconv) ** 2
            bmi_displaytext = ''

            #evaluate_bmi

            if bmi_res > 40:
                bmi_displaytext = classification[5]

            elif bmi_res > 35:
                bmi_displaytext = classification[4]

            elif bmi_res > 30:
                bmi_displaytext = classification[3]

            elif bmi_res > 25:
                bmi_displaytext = classification[2]

            elif bmi_res > 18.5:
                bmi_displaytext = classification[1]

            elif bmi_res < 18.5:
                bmi_displaytext = classification[0]
        except:
            bmi_displaytext = '>  invalid input'

        bmi_entry['state'] = NORMAL

        bmi_entry.delete(0, END)
        bmi_entry.insert(0, bmi_displaytext)

        bmi_entry['state'] = DISABLED

    def birthdayviewer():
        defaultbd = "no inputs yet"
        m = monthvar.get()
        d = dayvar.get()
        y = yearvar.get()

        bd = m, d, y
        bdtext = bd

        if m == "MONTH" and d == "DAY" and y == "YEAR":
            bd_entry['state'] = NORMAL

            bd_entry.delete(0, END)
            bd_entry.insert(0, defaultbd)

            bd_entry['state'] = DISABLED    

        else:
            bd_entry['state'] = NORMAL

            bd_entry.delete(0, END)
            bd_entry.insert(0, bdtext)

            bd_entry['state'] = DISABLED

    def male_com():
        #global male
        #m = male.get()
        #male = ''
        #if m == 1:
           #female.set(0)
            #print('Male')
        pass
    
    def female_com():
        #global female
        #f = female.get()
        #female = ''
        #if f == 1:
            #male.set(0)
            #print("female")
        pass

    playsetup = Toplevel(main)
    playsetup.geometry('1080x720+120+0')
    playsetup.title('SET UP PLAYER DATA')
    playsetup.resizable(False, False)
    playsetup.transient(main)
    playsetup.iconphoto(True, mainicon)

    playsetup_bg = ImageTk.PhotoImage(Image.open('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\backgrounds\\main game file\\playersetupGUI.jpg'))
    playsetup_canv = Canvas(playsetup, width=1080, height=720)
    playsetup_canv.pack(fill='both')
    playsetup_canv.create_image(0, 0, anchor='nw', image=playsetup_bg)

    male = IntVar()
    female = IntVar()

    monthvar = StringVar()
    monthvar.set('MONTH')
    dayvar = StringVar()
    dayvar.set('DAY')
    yearvar = StringVar()
    yearvar.set('YEAR')
    
    rolevar = StringVar()
    rolevar.set('PLAYER GAME ROLE/POSITION      ')


    #entryboxes

    fn_entry = Entry(playsetup, fg='#FFFFFF', bg='#B7630B', font=('Gill Sans MT', 11),
                     cursor='xterm', width=38, relief=SOLID, highlightbackground="BLACK", borderwidth=0)
    fn_entry.place(x=318, y=50)

    ln_entry = Entry(playsetup, fg='#FFFFFF', bg='#B7630B', font=('Gill Sans MT', 11),
                     cursor='xterm', width=38, relief=SOLID, highlightbackground="BLACK", borderwidth=0)
    ln_entry.place(x=642, y=50)

    sc_entry = Entry(playsetup, fg='#FFFFFF', bg='#B7630B', font=('Gill Sans MT', 11),
                     cursor='xterm', width=38, relief=SOLID, highlightbackground="BLACK", borderwidth=0)
    sc_entry.place(x=318, y=150)


    #second_row

    height_entry = Entry(playsetup, fg='#FFFFFF', bg='#B7630B', font=('Gill Sans MT', 11),
                         cursor='xterm', width=40, relief=SOLID, highlightbackground="BLACK", borderwidth=0)
    height_entry.place(x=320, y=290)

    weight_entry = Entry(playsetup, fg='#FFFFFF', bg='#B7630B', font=('Gill Sans MT', 11),
                         cursor='xterm', width=40, relief=SOLID, highlightbackground="BLACK", borderwidth=0)
    weight_entry.place(x=702, y=290)
    
    
    #Third_row 
    
    team_name = Entry(playsetup, fg='#FFFFFF', bg='#B7630B', font=('Gill Sans MT', 11),
                      cursor='xterm', width=38, relief=SOLID, highlightbackground="BLACK", borderwidth=0)
    team_name.place(x=320, y=535)
    
    region = Entry(playsetup, fg='#FFFFFF', bg='#B7630B', font=('Gill Sans MT', 11),
                   cursor='xterm', width=38, relief=SOLID, highlightbackground="BLACK", borderwidth=0)
    region.place(x=320, y=625)


    #disabled_entry

    bd_entry = Entry(playsetup, fg='#FFFFFF', bg='#B7630B', font=('Gill Sans MT', 11),
                     cursor='xterm', width=20, relief=SOLID, highlightbackground="BLACK", borderwidth=0, disabledbackground='#B7630B', disabledforeground='#FFFFFF', state=DISABLED)
    bd_entry.place(x=645, y=190)

    bd_view = Button(playsetup, text='view', bg='#af5d07', font=("Consolas", 10), activebackground='#af5d07', activeforeground='WHITE',
                     relief=SOLID, cursor='hand2', borderwidth=0, command=birthdayviewer)
    bd_view.place(x=813, y=188, height=25)

    bmi_entry = Entry(playsetup, fg='RED', bg='#B7630B', font=('Gill Sans MT', 13),
                      cursor='xterm', width=23, relief=SOLID, highlightbackground="BLACK", borderwidth=0, disabledbackground='#B7630B', disabledforeground='RED', state=DISABLED)
    bmi_entry.place(x=320, y=380)

    bmi_view = Button(playsetup, text='view', bg='#af5d07', font=("Consolas", 12), activebackground='#af5d07', activeforeground='WHITE',
                      relief=SOLID, cursor='hand2', borderwidth=0, command = bmi_viewerfunction)
    bmi_view.place(x=613, y=380, height=25)
    
    role = Entry(playsetup, fg='#FFFFFF', bg='#B7630B', font=('Gill Sans MT', 12),
                     cursor='xterm', width=38, relief=SOLID, highlightbackground="BLACK", borderwidth=0, disabledbackground='#B7630B', disabledforeground='#FFFFFF', state=DISABLED)
    role.place(x=665, y=535)
    
    role_view = Button(playsetup, text='view', bg='#af5d07', font=("Consolas", 11), activebackground='#af5d07', activeforeground='WHITE',
                      relief=SOLID, cursor='hand2', borderwidth=0, command=role_viewerfunction)
    role_view.place(x=1005, y=535, height=25)

    table_entry = Entry(playsetup, fg='#B7630B', bg='#B7630B', font=('Gill Sans MT', 12),
                        cursor='xterm', width=38, relief=SOLID, highlightbackground="BLACK", borderwidth=0)
    table_entry.place(x=700, y=400)
    


    #dajshd

    sx_picker = Checkbutton(playsetup, bg='#B7630B', text='MALE', font=('Consolas', 13), variable=male,
                            activebackground='#B7630B', activeforeground='BLACK', onvalue=1, offvalue=0, command=male_com)
    sx_picker.place(x=877, y=145)

    sx2_picker = Checkbutton(playsetup, bg='#B7630B', text='FEMALE', font=('Consolas', 13), variable=female,
                             activebackground='#B7630B', activeforeground='BLACK', onvalue=1, offvalue=0, command=female_com)
    sx2_picker.place(x=940, y=145)

    #dropdownmenu

    month_drop = OptionMenu(playsetup, monthvar, 'Jan', 'feb', 'mar', 'apr', 'may',
                            'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec')
    month_drop.config(bg='#B7630B', activebackground='#B7630B', font=('Consolas', 10),
                      fg='#FFFFFF', activeforeground='#FFFFFF', borderwidth=0, relief='solid', highlightthickness=0, indicatoron=0)
    month_drop.place(x=643, y=150)

    options = []
    for i in range(1,32):
        options.append(str(i))

    day_drop = OptionMenu(playsetup, dayvar, *options)
    day_drop.config(bg='#B7630B', activebackground='#B7630B', font=('Consolas', 10), fg='#FFFFFF',
                    activeforeground='#FFFFFF', borderwidth=0, relief='solid', highlightthickness=0, indicatoron=0)
    day_drop.place(x=720, y=150)

    yearoptions = []
    for j in range(1980, 2010):
        yearoptions.append(str(j))

    year_drop = OptionMenu(playsetup, yearvar, *yearoptions)
    year_drop.config(bg='#B7630B', activebackground='#B7630B', font=('Consolas', 10),
                     fg='#FFFFFF', activeforeground='#FFFFFF', borderwidth=0, relief='solid', highlightthickness=0, indicatoron=0)
    year_drop.place(x=779, y=150)
    
    #role
    
    roleoptions = ['Center',
                   'Power Forward',
                   'Small Forward',
                   'Point Guard',
                   'Shooting Guard',
                   'substitute player']
    rolemenu = OptionMenu(playsetup, rolevar, *roleoptions)
    rolemenu.config(bg='#B7630B', activebackground='#B7630B', font=('Consolas', 10),
                    fg='#FFFFFF', activeforeground='#FFFFFF', borderwidth=0, relief='solid', highlightthickness=0, indicatoron=0)
    rolemenu.place(x=730, y=575)


    #roleindicator_variable___

    cen1 = IntVar()
    cen2 = IntVar()

    pf1 = IntVar()
    pf2 = IntVar()

    sf1 = IntVar()
    sf2 = IntVar()

    pg1 = IntVar()
    pg2 = IntVar()

    sg1 = IntVar()
    sg2 = IntVar()
    

    #checkboxes_indicator per role and team...

    center_team1 = Checkbutton(playsetup, bg='#B7630B', text='center_team1', font=('Consolas', 11), variable=cen1, 
                               activebackground='#B7630B', activeforeground='BLACK', onvalue=1, offvalue=0)
    center_team1.place(x=15, y=55)
    center_team2 = Checkbutton(playsetup, bg='#B7630B', text='center_team2', font=('Consolas', 11), variable=cen2, 
                               activebackground='#B7630B', activeforeground='BLACK', onvalue=1, offvalue=0)
    center_team2.place(x=15, y=80)

    power_forward_team1 = Checkbutton(playsetup, bg='#B7630B', text='power_forward_team1', font=('Consolas', 11), variable=pf1,
                                      activebackground='#B7630B', activeforeground='BLACK', onvalue=1, offvalue=0)
    power_forward_team1.place(x=15, y=110)
    power_forward_team2 = Checkbutton(playsetup, bg='#B7630B', text='power_forward_team2', font=('Consolas', 11), variable=pf2,
                                      activebackground='#B7630B', activeforeground='BLACK', onvalue=1, offvalue=0)
    power_forward_team2.place(x=15, y=140)

    small_forward_team1 = Checkbutton(playsetup, bg='#B7630B', text='small_forward_team1', font=('Consolas', 11), variable=sf1,
                                      activebackground='#B7630B', activeforeground='BLACK', onvalue=1, offvalue=0)
    small_forward_team1.place(x=15, y=170)
    small_forward_team2 = Checkbutton(playsetup, bg='#B7630B', text='small_forward_team2', font=('Consolas', 11), variable=sf2,
                                      activebackground='#B7630B', activeforeground='BLACK', onvalue=1, offvalue=0)
    small_forward_team2.place(x=15, y=200)

    point_guard_team1 = Checkbutton(playsetup, bg='#B7630B', text='point_guard_team1', font=('Consolas', 11), variable=pg1,
                                      activebackground='#B7630B', activeforeground='BLACK', onvalue=1, offvalue=0)
    point_guard_team1.place(x=15, y=230)
    point_guard_team2 = Checkbutton(playsetup, bg='#B7630B', text='point_guard_team2', font=('Consolas', 11), variable=pg2,
                                      activebackground='#B7630B', activeforeground='BLACK', onvalue=1, offvalue=0)
    point_guard_team2.place(x=15, y=260)

    shooting_guard_team1 = Checkbutton(playsetup, bg='#B7630B', text='shooting_guard_team1', font=('Consolas', 11), variable=sg1,
                                      activebackground='#B7630B', activeforeground='BLACK', onvalue=1, offvalue=0)
    shooting_guard_team1.place(x=15, y=290)
    shooting_guard_team2 = Checkbutton(playsetup, bg='#B7630B', text='shooting_guard_team2', font=('Consolas', 11), variable=sg2,
                                      activebackground='#B7630B', activeforeground='BLACK', onvalue=1, offvalue=0)
    shooting_guard_team2.place(x=15, y=320)
    
    #GSU - window navigation buttons

    back_to_homepage = Button(playsetup, text= 'back to homepage <', bg= '#B7630B', activebackground= '#B7630B',
                              font= ('Consolas', 11), fg= 'BLACK', activeforeground= 'WHITE', relief=SOLID, borderwidth=0, command=backtohomepage)
    back_to_homepage.place(x=15, y=590)

    clear_entries = Button(playsetup, text= 'clear all <', bg= '#B7630B', activebackground= '#B7630B',
                           font= ('Consolas', 11), fg= 'BLACK', activeforeground= 'WHITE', relief=SOLID, borderwidth=0, command= clearallentries)
    clear_entries.place(x=15, y=615)

    confirm_setup = Button(playsetup, text= 'confirm set-up <', bg= '#B7630B', activebackground= '#B7630B',
                           font= ('Consolas', 11), fg= 'BLACK', activeforeground= 'WHITE', relief=SOLID, borderwidth=0, command=confirm_players)
    confirm_setup.place(x=15, y=640)

    add_player = Button(playsetup, text= '> add player', bg= '#B7630B', activebackground= '#B7630B',
                        font= ('Consolas', 11), fg= 'BLACK', activeforeground= 'WHITE', relief=SOLID, borderwidth=1, command=addplayer)
    add_player.place(x=945, y=640)

    #labels

    tutorlabel = Label(playsetup, text= 'after you add a player check the\nbox above depending of\nwhat role of the player you added\n \nthis is essential because\n the system will not let you continue\nif you missed a checkbox',
                       font=('Consolas', 10), fg='BLACK', bg='#B7630B')
    tutorlabel.place(x=15, y=420)

    wt = StringVar()
    wt.set('click here to choose which team')
    team_options = ['team 1',
                    'team 2']
    whichteam = OptionMenu(playsetup, wt, *team_options)
    whichteam.config(bg='#B7630B', activebackground='#B7630B', font=('Consolas', 10),
                     fg='#FFFFFF', activeforeground='#FFFFFF', borderwidth=0, relief='solid', highlightthickness=0, indicatoron=0)
    whichteam.place(x=710, y=610)

    def proceed():
        mainscoreboard()

    temporarybutton = Button(playsetup, text='proceed', command=proceed)
    temporarybutton.place(x=0, y=0)

    
def gsuwindow():
    print('--------- gameset up opened ---------', datern)
    global gsumain_bg

    gsu_main = Toplevel(main)
    gsu_main.transient(main)
    gsu_main.title('Game set-up, set-up players and important details')
    gsu_main.geometry('1080x720+120+0')
    gsu_main.resizable(False, False)
    gsu_main.iconphoto(True, mainicon)

    gsumain_bg = ImageTk.PhotoImage(Image.open('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\backgrounds\\main game file\\createtable GSU.jpg'))
    gsumain_canv = Canvas(gsu_main, width=1080, height=720)
    gsumain_canv.pack(fill='both')
    gsumain_canv.create_image(0, 0, anchor='nw', image= gsumain_bg)




    def submitgsu():
        print('----- gsu submit authentication ----', datern)

        def tablename_wrap(table_name):
            mainbase = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\database\\basketball_maindb.db')
            titlebase = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\database\\basketball_titledb.db')
            maincursor = mainbase.cursor()
            titlecursor = titlebase.cursor()

            maincursor.execute(f"""CREATE TABLE {table_name} (
                                first_name text,
                                last_name text,
                                school text,
                                birthday text,
                                height integer,
                                weight integer,
                                BMI integer,
                                team text,
                                region text,
                                role text


                            )""")


            #titlecursor.execute("CREATE TABLE dbstrings ( titledates text )")
            titlecursor.execute("INSERT INTO dbstrings VALUES (:table_name)",
                                {
                                    'table_name': stringtype
                                }
                                )

            event.delete(0, END)
            month.delete(0, END)
            day.delete(0, END)
            year.delete(0, END)

            mainbase.commit()
            titlebase.commit()
            mainbase.close()
            titlebase.close()

            #opening the player data input page
            gsuplayerdata()

        """
        doctype string;
        mainbase = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\database\\basketball_maindb.db')
        titlebase = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\database\\basketball_titledb.db')
        maincursor = mainbase.cursor()
        titlecursor = titlebase.cursor()

        mainbase.commit()
        titlebase.commit()
        mainbase.close()
        titlebase.close()
        """

        preview1['state'] = NORMAL
        preview2['state'] = NORMAL
        preview3['state'] = NORMAL

        preview1.delete(0, END)
        preview2.delete(0, END)
        preview3.delete(0, END)

        ev = event.get()
        mo = month.get()
        da = day.get()
        ye = year.get()


        preview_screen = ev + ' ' + mo + ' ' + da + ' ' + ye
        preview1.insert(0, preview_screen)

        astable = ev + mo + da + ye
        preview2.insert(0, astable)


        astring = ev + mo + da + ye
        preview3.insert(0, astring)

        table_name = preview2.get()
        stringtype = preview3.get()
        tablename_wrap(table_name)


        preview1['state'] = DISABLED
        preview2['state'] = DISABLED
        preview3['state'] = DISABLED


#-------------------------------------------------------#

    def cancel_exit():
        print('----------- Cancel button pressed ------------', datern)

        if messagebox.askyesno(title='do you want to go back to home page?', message='do you really want to cancel progress?'):
            print('--------- going back to home page ----------', datern)
            gsu_main.destroy()

        else:
            print('--------- condition not met -----------', datern)

    def prv_rest():
        print('---------- resetting -----------', datern)

        if messagebox.askyesno(title='Do you want to reset entries?', message='DO YOU REALLY WANT TO RESET ENTRIES?'):

            preview1['state'] = NORMAL
            preview2['state'] = NORMAL
            preview3['state'] = NORMAL

            preview1.delete(0, END)
            preview2.delete(0, END)
            preview3.delete(0, END)

            preview1['state'] = DISABLED
            preview2['state'] = DISABLED
            preview3['state'] = DISABLED

            event.delete(0, END)
            month.delete(0, END)
            day.delete(0, END)
            year.delete(0, END)
            
        else:
            pass



    def preview_entries():
        print('-------- previewing entries ---------', datern)

        preview1['state'] = NORMAL
        preview2['state'] = NORMAL
        preview3['state'] = NORMAL

        preview1.delete(0, END)
        preview2.delete(0, END)
        preview3.delete(0, END)

        ev = event.get()
        mo = month.get()
        da = day.get()
        ye = year.get()

        preview_screen = ev + ' ' + mo + ' ' + da + ' ' + ye
        preview1.insert(0, preview_screen)

        astable = ev + mo + da + ye
        preview2.insert(0, astable)


        astring = ev + ' ' + mo + ' ' + da + ' ' + ye
        preview3.insert(0, astring)

        preview1['state'] = DISABLED
        preview2['state'] = DISABLED
        preview3['state'] = DISABLED

    #Database opening and closing

    #entry boxes

    event = Entry(gsu_main, fg='BLACK', bg='#C87018', font=('Gill Sans MT', 11),
                   cursor='xterm', width=60, relief=SOLID, highlightbackground="BLACK", borderwidth=1)
    event.place(x=520, y=140)

    month = Entry(gsu_main, fg='BLACK', bg='#C87018', font=('Gill Sans MT', 11),
                   cursor='xterm', width=60, relief=SOLID, highlightbackground="BLACK", borderwidth=1)
    month.place(x=520, y=240)

    day = Entry(gsu_main, fg='BLACK', bg='#C87018', font=('Gill Sans MT', 11),
                   cursor='xterm', width=60, relief=SOLID, highlightbackground="BLACK", borderwidth=1)
    day.place(x=520, y=340)

    year = Entry(gsu_main, fg='BLACK', bg='#C87018', font=('Gill Sans MT', 11),
                   cursor='xterm', width=60, relief=SOLID, highlightbackground="BLACK", borderwidth=1)
    year.place(x=520, y=415)

    
    preview1 = Entry(gsu_main, fg='#FFFFFF', bg='#A3570B', font=('Gill Sans MT', 13), disabledbackground='#A3570B', disabledforeground='#FFFFFF',
                     cursor='xterm', width=47, relief=SOLID, highlightbackground="BLACK", borderwidth=0, state='disabled')
    preview1.place(x=65, y=545)

    preview2 = Entry(gsu_main, fg='#FFFFFF', bg='#A3570B', font=('Gill Sans MT', 13), disabledbackground='#A3570B', disabledforeground='#FFFFFF',
                      cursor='xterm', width=27, relief=SOLID, highlightbackground="BLACK", borderwidth=0, state='disabled')
    preview2.place(x=65, y=630)

    preview3 = Entry(gsu_main, fg='#FFFFFF', bg='#A3570B', font=('Gill Sans MT', 13), disabledbackground='#A3570B', disabledforeground='#FFFFFF',
                      cursor='xterm', width=27, relief=SOLID, highlightbackground="BLACK", borderwidth=0, state='disabled')
    preview3.place(x=352, y=630)
    

    #buttons

    button1 = Button(gsu_main, text='>       submit', bg='#B7630B', font=("Consolas", 13), activebackground='#B0600B', activeforeground='BLACK',
                     relief=FLAT, cursor='hand2', borderwidth=0, command = submitgsu)
    button1.place(x=900, y=478)

    button2 = Button(gsu_main, text='>        reset', bg='#B7630B', font=("Consolas", 13), activebackground='#B0600B', activeforeground='BLACK',
                     relief=FLAT, cursor='hand2', borderwidth=0, command=prv_rest)
    button2.place(x=900, y=508)

    button3 = Button(gsu_main, text='>       cancel', bg='#B7630B', font=("Consolas", 13), activebackground='#B0600B', activeforeground='BLACK',
                     relief=FLAT, cursor='hand2', borderwidth=0, command=cancel_exit)
    button3.place(x=900, y=538)

    button4 = Button(gsu_main, text='>      preview', bg='#B7630B', font=("Consolas", 13), activebackground='#B0600B', activeforeground='BLACK',
                     relief=FLAT, cursor='hand2', borderwidth=0, command=preview_entries)
    button4.place(x=900, y=568)


#game set up - GSU
def gamestartlogin():
    print('-------- login to start set-up -------', datern)
    global gsu_bg
    global gsusubmit_icon
    global gsureset_icon
    global gsucancel_icon

    def auth_gsu():
        print('-------- authenticating login ----------', datern)
        gsu_window.grab_release()

        con = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Administrator_Info\\administrators_username.db')
        con2 = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Administrator_Info\\administrators_password.db')
        dial = con.cursor()
        dial2 = con2.cursor()
            #dial.execute("""CREATE TABLE usernames (username text)""")
            #dial2.execute("""CREATE TABLE passwords (password text)""")

        dial.execute("SELECT * from usernames")
        dial2.execute("SELECT * from passwords")

        dialfetch = dial.fetchall()
        dialfetch2 = dial2.fetchall()

        gsu_un = gsu_username.get()
        gsu_pw =  gsu_password.get()

        username = ''
        password = ''

        for iU in dialfetch:
            username += str(iU)


        for iP in dialfetch2:
            password += str(iP)


        if gsu_un == '' and gsu_pw == '':
            
            if messagebox.showerror(title='invalid keyword', message='theres no such things as empty admin pass'):

                gsu_window.grab_set_global()
            
        else:

            if gsu_un in username and gsu_pw in password:
                print('---------- login successfull ------------', datern)
                gsu_username.delete(0, END)
                gsu_password.delete(0, END)
                gsuwindow()

                gsu_window.destroy()

            else:
                print('-------- admin not verified --------', datern)

                if messagebox.showerror(title='Invalid Keywords', message='ACCESS DENIED!'):
                    gsu_username.delete(0, END)
                    gsu_password.delete(0, END)
                    gsu_window.grab_set_global()
                else:
                    gsu_username.delete(0, END)
                    gsu_password.delete(0, END)
                    gsu_window.grab_set_global()

        con.commit()
        con2.commit()
        con.close()
        con2.close()



    def gsuentry_reset():
        print('---------- resetting entry boxes ----------', datern)
        gsu_window.grab_release()

        if messagebox.askyesno(title='reset all entered keywords', message='do you really want to reset entry boxes'):
            print('--------- successfully resetted  ---------', datern)
            gsu_username.delete(0, END)
            gsu_password.delete(0, END)
            gsu_window.grab_set_global()
        
        else:
            gsu_window.grab_set_global()
            print('-----------  reset cancelled  -------------', datern)


    
    def gsu_exit():
        print('--------- exiting game set up login ---------', datern)
        gsu_window.grab_release()

        if messagebox.askokcancel(title='back to home page', message='do you really want to cancel login?'):
            print('------- exitted from login page --------', datern)
            gsu_window.destroy()
        
        else:
            print('----- exit cancelled -------', datern)
            gsu_window.grab_set_global()






    gsu_window = Toplevel(main)
    gsu_window.title('login to start setting up the game')
    gsu_window.transient(main)
    gsu_window.geometry('1080x720+120+0')
    gsu_window.resizable(False, False)
    gsu_window.iconphoto(True, mainicon)
    gsu_window.grab_set_global()

    gsu_bg = ImageTk.PhotoImage(Image.open('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\MAIN BASKETBALL FOLDER\\Thumbnails\\backgrounds\\main game file\\log_in GSU.jpg'))
    gsu_canv = Canvas(gsu_window, width=1080, height=720)
    gsu_canv.pack(fill='both')
    gsu_canv.create_image(0, 0, anchor='nw', image=gsu_bg)


    #entry box
    gsu_username = Entry(gsu_window, fg='BLACK', bg='#C87018', font=('Gill Sans MT', 13),
                         cursor='xterm', width=40, relief=SOLID, highlightbackground="BLACK", borderwidth=1)
    gsu_username.place(x=580, y=265)

    gsu_password = Entry(gsu_window, fg='BLACK', bg='#C87018', font=('Gill Sans MT', 13),
                         cursor='xterm', width=40, relief=SOLID, highlightbackground="BLACK", borderwidth=1, show='*')
    gsu_password.place(x=580, y=390)

    #buttons
    gsusubmit_icon = PhotoImage(file = 'D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\icons\\submit icon.png')
    gsu_submit = Button(gsu_window, text='submit', bg='#B7630B', activebackground='#B7630B', fg='BLACK', activeforeground='BLACK', relief='flat',
                        cursor='hand2', font=('Consolas', 13), image= gsusubmit_icon, compound='right', command=auth_gsu)
    gsu_submit.place(x=580, y=450, height=33)

    gsureset_icon = PhotoImage(file= 'D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\icons\\reset GSU.png')
    gsu_reset = Button(gsu_window, text='reset',bg='#B7630B', activebackground='#B7630B', fg='BLACK', activeforeground='BLACK', relief='flat',
                       cursor='hand2', font=('Consolas', 13), image= gsureset_icon, compound='right', command=gsuentry_reset)
    gsu_reset.place(x=710, y=450, height=33)

    gsucancel_icon = PhotoImage(file = 'D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\icons\\cancel GSU.png')
    gsu_cancel = Button(gsu_window, text='cancel',bg='#B7630B', activebackground='#B7630B', fg='BLACK', activeforeground='BLACK', relief='flat',
                        cursor='hand2', font=('Consolas', 13), image= gsucancel_icon, compound='right', command=gsu_exit)
    gsu_cancel.place(x=835, y=450, height=33)


def startgame():
    print('------------ opening game set-up -------------', datern)



def LoadSavedFiles():
    global archive_bg
    print('----------- LOAD SAVED FILE PAGE OPENED -----------', datern)


    def refreshhoverIN(event):
        refreshbtn['bg'] = '#C87018'
        archive_canv.itemconfig(archive_hover, text='Refresh Archive list/page...')

    def refreshhoverOUt(event):
        refreshbtn['bg'] = '#B7630B'
        archive_canv.itemconfig(archive_hover, text='')

    def openarchoverIN(event):
        open_gamerec['bg'] = '#C87018'
        archive_canv.itemconfig(archive_hover, text='Open a record from archive list...')

    def openarchoverOUT(event):
        open_gamerec['bg'] = '#B7630B'
        archive_canv.itemconfig(archive_hover, text='')

    def deletetablehoverIN(event):
        deletetable['bg'] = '#C87018'
        archive_canv.itemconfig(archive_hover, text='delete a table from the list...')

    def deletetablehoverOUT(event):
        deletetable['bg'] = '#B7630B'
        archive_canv.itemconfig(archive_hover, text='')
    

    archive = Toplevel(main)
    archive.transient(main)
    archive.title('LOAD SAVED FILES')
    archive.geometry('1080x720+120+0')
    archive.iconphoto(True, mainicon)
    archive.resizable(False, False)
    

    archive_bg = ImageTk.PhotoImage(Image.open('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDes\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\backgrounds\\Archive Page.jpg'))
    archive_canv = Canvas(archive, width=1080, height=720)
    archive_canv.pack(fill='both')
    archive_canv.create_image(0, 0, anchor='nw', image=archive_bg)
    archive_hover = archive_canv.create_text(40, 570, anchor='w', justify=LEFT, text='')
    archive_list = archive_canv.create_text(40, 150,  anchor='w', font=('Centaur', 12), justify=LEFT,
                                            text='test .....................................................................................')
    #open database - record start at 40, 150 Ljust anchorWEST

    

    # buttons 

    refreshbtn = Button(archive, text='|Refresh|', bg='#B7630B', activebackground='#B7630B', fg='BLACK', activeforeground='BLACK', relief=FLAT, 
                        cursor='hand2', font=('Consolas', 13))
    refreshbtn.bind('<Enter>', refreshhoverIN)
    refreshbtn.bind('<Leave>', refreshhoverOUt)
    refreshbtn.place(x=140, y=620, height=30)

    open_gamerec = Button(archive, text='|Open game records|', bg='#B7630B', activebackground='#B7630B', fg='BLACK', activeforeground='BLACK', relief=FLAT,
                          cursor='hand2', font=('Consolas', 13))
    open_gamerec.bind('<Enter>', openarchoverIN)
    open_gamerec.bind('<Leave>', openarchoverOUT)
    open_gamerec.place(x=225, y=620, height=30)

    deletetable = Button(archive, text='|delete table|', bg='#B7630B', activebackground='#B7630B', fg='BLACK', activeforeground='BLACK', relief=FLAT,
                          cursor='hand2', font=('Consolas', 13))
    deletetable.bind('<Enter>', deletetablehoverIN)
    deletetable.bind('<Leave>', deletetablehoverOUT)
    deletetable.place(x=400, y=620, height=30)


def mainlogin_page():
    global login_pageBG
    print('--------- LOGIN PAGE FOCUS -----------', datern)

    def confirm_loginHoverIN(event):
        confirm_login['bg'] = '#C87018'
        login_pagecanv.itemconfig(text_label, text='confirm verification...')

    def confirm_loginHoverOUT(event):
        confirm_login['bg'] = '#B7630B'
        login_pagecanv.itemconfig(text_label, text='login page - verify you are an admin to continue...')


    def cancel_loginHoverIN(event):
        cancel_login['bg'] = '#C87018'
        login_pagecanv.itemconfig(text_label, text='cancel verification - back to previous page...')

    def cancel_loginHoverOUT(event):
        cancel_login['bg'] = '#B7630B'
        login_pagecanv.itemconfig(text_label, text='login page - verify you are an admin to continue...')


    def reset_loginHoverIN(event):
        reset_login['bg'] = '#C87018'
        login_pagecanv.itemconfig(text_label, text='reset entries - removes everything you typed here...')

    def reset_loginHoverOUT(event):
        reset_login['bg'] = '#B7630B'
        login_pagecanv.itemconfig(text_label, text='login page - verify you are an admin to continue...')

#COMMAND AREA

    def cancel_loginEXIT():
        print('-------- do you want to exit -----------', datern)
        login_page.grab_release()

        if messagebox.askyesno(title='DO YOU WANT TO CANCEL LOGIN', message='DO YOU WANT TO GO BACK TO THE PREVIOUS PAGE?'):
            print('-------- EXITING PAGE ---------', datern)
            login_page.destroy()

        else:
            print('------- login page exit cancelled -------', datern)
            login_page.grab_set_global()

    def reset_loginCommand():
        print('------- resetting entries --------', datern)
        login_page.grab_release()

        if messagebox.askokcancel(title='REMOVING ALL ENTERED ENTRIES', message='DO YOU WANT TO RESET ENTRY BOX?'):
            print('------- entries cleared --------', datern)
            login_username.delete(0, END)
            login_password.delete(0, END)

            login_page.grab_set_global()


        else:
            print('-------- reset cancel ---------', datern)
            login_page.grab_set_global()


    def submission_login():
        print('-------- submitting information to verify ---------', datern)
        login_page.grab_release()

        con = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Administrator_Info\\administrators_username.db')
        con2 = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Administrator_Info\\administrators_password.db')
        dial = con.cursor()
        dial2 = con2.cursor()
            #dial.execute("""CREATE TABLE usernames (username text)""")
            #dial2.execute("""CREATE TABLE passwords (password text)""")

        dial.execute("SELECT * from usernames")
        dial2.execute("SELECT * from passwords")

        global username
        global password

        username = ''
        password = ''

        fetched_username = dial.fetchall()
        fetched_password = dial2.fetchall()

        for indexU in fetched_username:
            username += str(indexU)


        for indexP in fetched_password:
            password += str(indexP)

        user = login_username.get()
        passw = login_password.get()

        if user == '' and passw == '':
            if messagebox.showerror(title='verification denied', message='NOT RECOGNIZED AS ADMIN TRY AGAIN'):
                login_password.delete(0, END)
                login_page.grab_set_global()

        else:
            if user in username and passw in password:
                print('------ information verified as Admin -------', datern)
                LoadSavedFiles()
                login_page.destroy()


            else:
                print('------- password not recognized as admin ------', datern)

                if messagebox.showerror(title='verification denied', message='NOT RECOGNIZED AS ADMIN TRY AGAIN'):
                    login_password.delete(0, END)
                    login_page.grab_set_global()

        
        con.commit()
        con2.commit()
        con.close()
        con2.close()


    login_page = Toplevel(main)
    login_page.geometry('1080x720+120+0')
    login_page.resizable(False, False)
    login_page.transient(main)
    login_page.title('ADMINISTRATOR LOGIN')
    login_page.iconphoto(True, mainicon)
    login_page.grab_set_global()

    login_pageBG = ImageTk.PhotoImage(Image.open('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\backgrounds\\Login page.jpg'))
    login_pagecanv = Canvas(login_page, width=1080, height=720)
    login_pagecanv.pack(fill='both')
    login_pagecanv.create_image(0, 0, anchor='nw', image=login_pageBG)
    text_label = login_pagecanv.create_text(65, 470, anchor='w', justify=LEFT, font=('Consolas', 10), text='login page - verify you are an admin to continue...')

#BUTTONS FOR LOGIN PAGE

    confirm_login = Button(login_page, text= 'confirm', font=('Consolas', 12), bg='#B7630B', activebackground='#B7630B', width=20,
                           fg='BLACK', activeforeground='BLACK', cursor='hand2', borderwidth=1, highlightbackground='BLACK', relief=SOLID, command=submission_login)
    confirm_login.bind('<Enter>', confirm_loginHoverIN)
    confirm_login.bind('<Leave>', confirm_loginHoverOUT)
    confirm_login.place(x=250, y=500)

    cancel_login = Button(login_page, text= 'cancel', font=('Consolas', 12), bg='#B7630B', activebackground='#B7630B', width=20,
                          fg='BLACK', activeforeground='BLACK', cursor='hand2', borderwidth=1, highlightbackground='BLACK', relief=SOLID, command=cancel_loginEXIT)
    cancel_login.bind('<Enter>', cancel_loginHoverIN)
    cancel_login.bind('<Leave>', cancel_loginHoverOUT)
    cancel_login.place(x=440, y=500)

    reset_login = Button(login_page, text= 'reset', font=('Consolas', 12), bg='#B7630B', activebackground='#B7630B', width=20,
                         fg='BLACK', activeforeground='BLACK', cursor='hand2', borderwidth=1, highlightbackground='BLACK', relief=SOLID, command=reset_loginCommand)
    reset_login.bind('<Enter>', reset_loginHoverIN)
    reset_login.bind('<Leave>', reset_loginHoverOUT)
    reset_login.place(x=350, y=533)


#ENTRY BOX

    login_username = Entry(login_page, fg='BLACK', bg='#C87018', font=('Gill Sans MT', 12),
                           cursor='xterm', width=37, relief=SOLID, highlightbackground="BLACK", borderwidth=1)
    global l_usernameFetch
    l_usernameFetch = login_username.get()
    login_username.place(x=240, y=225)

    login_password = Entry(login_page, fg='BLACK', bg='#C87018', font=('Gill Sans MT', 12),
                           cursor='xterm', width=37, relief=SOLID, highlightbackground="BLACK", borderwidth=1, show='*')
    global l_passwordFetch
    l_passwordFetch = login_password.get()
    login_password.place(x=240, y=305)



def manageaccount():
    print('--------- successfully opened account manager window ---------- \n ---------- user attention locked ----------', datern)
    global account_managerBG


    def authentication():
        print('------- authentication page open ---------\n ----------- attention grabbed ----------------', datern)
        global auth_bg

        def DatabaseIN():
    #DATABASE
            authen.grab_release()
        
            print('---------Adding account to queue--------------', datern)
            con = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Administrator_Info\\administrators_username.db')
            con2 = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Administrator_Info\\administrators_password.db')
            dial = con.cursor()
            dial2 = con2.cursor()
        #dial.execute("""CREATE TABLE usernames (username text)""")
        #dial2.execute("""CREATE TABLE passwords (password text)""")

            dial.execute("INSERT INTO usernames VALUES (:usernames)", {'usernames': usernameADD.get()})
            dial2.execute("INSERT INTO passwords VALUES (:passwords)", {'passwords': passwordADD.get()})

            #erase past inputs 

            usernameADD.delete(0, END)
            passwordADD.delete(0, END)
            confirmPASS.delete(0, END)




            if messagebox.showwarning(title='Account added', message='Account successfully added click ok to reload'):
                authen.destroy()
                account_manager.grab_set_global()

            else:
                pass

            con.commit()
            con2.commit()
            con.close()
            con2.close()

#databaseshesh

        def submitauthenIN(event):
            submitauth['bg'] = '#C87018'
            auth_canvas.itemconfig(hover_auth, text='submit and proceed to the next step...')

        def submitauthenOUT(event):
            submitauth['bg'] = '#B7630B'
            auth_canvas.itemconfig(hover_auth, text='Verify that you are an admin before we add this as new account...')


        def resetauthenIN(event):
            resetauth['bg'] = '#C87018'
            auth_canvas.itemconfig(hover_auth, text='Reset Entries...')

        def resetauthenOUT(event):
            resetauth['bg'] = '#B7630B'
            auth_canvas.itemconfig(hover_auth, text='Verify that you are an admin before we add this as new account...')


        def exitauthenIN(event):
            exit_auth['bg'] = '#C87018'
            auth_canvas.itemconfig(hover_auth, text='Exit - back to account manager page...')

        def exitauthenOUT(event):
            exit_auth['bg'] = '#B7630B'
            auth_canvas.itemconfig(hover_auth, text='Verify that you are an admin before we add this as new account...')



        def submitauthentication():
            print('--------- submitting authentication to verify ------------', datern)          

            u = auth_Username.get()
            i = auth_Password.get()

            con = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Administrator_Info\\administrators_username.db')
            con2 = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Administrator_Info\\administrators_password.db')
            dial = con.cursor()
            dial2 = con2.cursor()
            #dial.execute("""CREATE TABLE usernames (username text)""")
            #dial2.execute("""CREATE TABLE passwords (password text)""")

            dial.execute("SELECT * from usernames")
            dial2.execute("SELECT * from passwords")

            global username
            global password

            username = ''
            password = ''

            fetched_username = dial.fetchall()
            fetched_password = dial2.fetchall()

            for indexU in fetched_username:
                username += str(indexU)


            for indexP in fetched_password:
                password += str(indexP)


            authen.grab_release()
            
            if u in username and i in password:
                print('--------- appending info -----------------', datern)

                DatabaseIN()
            
            else:
                if messagebox.showerror(title='admin not found', message='not recognized as admin \nTry Again'):
                    auth_Password.delete(0, END)
                    authen.grab_set_global()

            con.commit()
            con2.commit()
            con.close()
            con2.close()

        def resetauthentication():
            print('---------- reseting all entryboxes ------------', datern)
            authen.grab_release()

            if messagebox.askyesno(title='Clear entrybox', message='do you really want to clear entries?'):
                auth_Username.delete(0, END)
                auth_Password.delete(0, END)
                authen.grab_set_global()

            else:
                authen.grab_set_global()
                account_manager.grab_set_global()
                pass



        def exitauthentication():
            print('--------------- exitting authenication page ----------------', datern)
            authen.grab_release()
            if messagebox.askyesno(title='leaving Verification page...', message='do you really want to leave Verifcation Page?'):
                authen.destroy()

            else:
                authen.grab_set_global()
                pass



        authen = Toplevel(main)
        authen.title('Login authentication')
        authen.geometry('1080x720+120+0')
        authen.resizable(False, False)
        authen.transient(main)
        authen.iconphoto(True, mainicon)
        authen.grab_set_global()


        auth_bg = ImageTk.PhotoImage(Image.open('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\backgrounds\\Authentication page.jpg'))
        auth_canvas = Canvas(authen, width=1080, height=720)
        auth_canvas.pack(fill='both')
        auth_canvas.create_image(0, 0, anchor= 'nw', image=auth_bg)
        hover_auth = auth_canvas.create_text(280, 470, anchor=W, justify=LEFT, font=('Gill Sans MT', 10), text='Verify that you are an admin before we add this as new account...')



        auth_Username = Entry(authen, fg='BLACK', bg='#C87018', font=('Gill Sans MT', 10),
                               cursor='xterm', width=45, relief=SOLID, highlightbackground="BLACK", highlightthickness=1)
        auth_Username.place(x=280, y=290)
        auth_Password = Entry(authen, fg='BLACK', bg='#C87018', font=('Gill Sans MT', 10),
                               cursor='xterm', width=45, relief=SOLID, highlightbackground="BLACK", highlightthickness=1, show='*')
        auth_Password.place(x=280, y=380)

    #buttons confirm, cancel and reset


        submitauth = Button(authen, text='submit', font=('Gill Sans MT', 13), bg='#B7630B', fg='BLACK',
                            activebackground='#B7630B', activeforeground='BLACK', cursor='hand2', borderwidth=1, relief=SOLID, width=10, justify=CENTER, command=submitauthentication)
        submitauth.place(x=280, y=420, height=33)
        submitauth.bind('<Enter>', submitauthenIN)
        submitauth.bind('<Leave>', submitauthenOUT)
        
        resetauth = Button(authen, text='reset', font=('Gill Sans MT', 13), bg='#B7630B', fg='BLACK',
                           activebackground='#B7630B', activeforeground='BLACK', cursor='hand2', borderwidth=1, relief=SOLID, width=10, justify=CENTER, command=resetauthentication)
        resetauth.place(x=390, y=420, height=33)
        resetauth.bind('<Enter>', resetauthenIN)
        resetauth.bind('<Leave>', resetauthenOUT)

        exit_auth = Button(authen, text='cancel', font=('Gill Sans MT', 13), bg='#B7630B', fg='BLACK',
                           activebackground='#B7630B', activeforeground='BLACK', cursor='hand2', borderwidth=1, relief=SOLID, width=10, justify=CENTER, command=exitauthentication)
        exit_auth.place(x=502, y=420, height=33)
        exit_auth.bind('<Enter>', exitauthenIN)
        exit_auth.bind('<Leave>', exitauthenOUT)


    def submitadminADD():
        print('----------- opening submit authentication page -----------------', datern)
        account_manager.grab_release()

        enteredpass = passwordADD.get()
        passconfirmation = confirmPASS.get()

        if enteredpass == passconfirmation:
            print('------- Password and password confirmation match -------', datern)

            if messagebox.askyesno(title='confirmation', message='do you want to continue?'):
                print('------- opening authentication page --------', datern)
                authentication()

            else:
                print('--------- authentication page open forfeit ---------', datern)
                account_manager.grab_set_global()

        else:
            print('------- Password and password confirmation did not match -------', datern)

            messagebox.showerror(title='invalid keyword', message='you password did not match!')
            passwordADD.delete(0, END)
            confirmPASS.delete(0, END)

            account_manager.grab_set_global()
    

    def backtohomepage():
        print('----------- successfully got back to homepage --------- \n ---------- user attention unlocked --------------', datern)
        account_manager.grab_release()
        account_manager.destroy()

    def resetentry():
        print('----------- reset or not ----------- \n ------------- user attention unlocked -------------', datern)
        account_manager.grab_release()
        
        if messagebox.askyesno(title= 'reset entry inputs', message= 'you will lose all of the stuff you inputted !'):
            usernameADD.delete(0, END)
            passwordADD.delete(0, END)
            confirmPASS.delete(0, END)

            print('---------- entry reset success ---------- \n ---------- user attention locked -------------', datern)
            account_manager.grab_set_global()

        else:
            account_manager.grab_set_global()
            print('--------- nothing has changed ------------ \n ---------- attention locked ---------', datern)


    def cancel_input():
        print('---------user cancel askyesno --------------', datern)
        account_manager.grab_release()
        if messagebox.askyesno(title='cancel entry', message='this process wont do anything to the entered keywords !'):
            print('--------- cancelation successfull -------------- \n ----------- attention locked ---------------', datern)
            account_manager.grab_set_global()
        else:
            print('--------- cancelation successfull -------------- \n ----------- attention locked ---------------', datern)
            account_manager.grab_set_global()
            pass
    
    
    def showadmins():
        print('----------choosing to show admins or not --------------', datern)
        account_manager.grab_release()
        if messagebox.askyesno(title='show active administrators', message='show the active administrators'):
            print('-----------administrators shown---------------', datern)
            account_manager.grab_set_global()

            con = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Administrator_Info\\administrators_username.db')
            con2 = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Administrator_Info\\administrators_password.db')
            dial = con.cursor()
            dial2 = con2.cursor()            

                #dial.execute("""CREATE TABLE usernames (username text)""")
                #dial2.execute("""CREATE TABLE passwords (password text)""")

            dial.execute("SELECT *, oid FROM usernames")
            username_records = dial.fetchall()

            dial2.execute("SELECT *, oid FROM passwords")
            password_records = dial2.fetchall()
#B7630B

            looped_record = ''
            for record in username_records:
                looped_record += str(record[1]) + '\t' + str(record[0]) + '\t' + '-' + str(datern) + '\n'


            
            label_frame = Frame(account_manager, width=300, height=400, bg='#B7630B')
            label_frame.place(x=230, y=200)

            frame_label = Label(label_frame, font=('Consolas', 8), text=looped_record, bg='#B7630B', fg= '#FFFFFF', justify= LEFT)
            frame_label.pack(padx=20, pady=20)


            con.commit()
            con2.commit()
            con.close()
            con2.close()


        else:
            print('--------- show Administrators cancelled----------', datern)
            account_manager.grab_set_global()


#DELETE A RECORD IN DATABASE
    def deleteadmin():
        global del_AdminBG
        print('-------deleting admin---------', datern)
        account_manager.grab_release()

        def Confirm_del():
            print('---------- EVALUATING BEFORE CONTINUING -----------', datern)
            del_username = del_adminUN.get()
            del_password = del_adminPW.get()
            del_ID = IDto_del.get()
            del_Admin.grab_release()

            con = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Administrator_Info\\administrators_username.db')
            con2 = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Administrator_Info\\administrators_password.db')
            dial = con.cursor()
            dial2 = con2.cursor()
            #dial.execute("""CREATE TABLE usernames (username text)""")
            #dial2.execute("""CREATE TABLE passwords (password text)""")

            dial.execute("SELECT * from usernames")
            dial2.execute("SELECT * from passwords")

            global username
            global password

            username = ''
            password = ''

            fetched_username = dial.fetchall()
            fetched_password = dial2.fetchall()

            for indexU in fetched_username:
                username += str(indexU)


            for indexP in fetched_password:
                password += str(indexP)

       
            if del_username in username and del_password in password:
                print('-------- evaluation returns True --------', datern)

                con = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Administrator_Info\\administrators_username.db')
                con2 = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Administrator_Info\\administrators_password.db')
                dial = con.cursor()
                dial2 = con2.cursor()            
                    #dial.execute("""CREATE TABLE usernames (username text)""")
                    #dial2.execute("""CREATE TABLE passwords (password text)""")

                dial.execute("DELETE from usernames WHERE oid=" + del_ID)
                dial2.execute("DELETE from passwords WHERE oid=" + del_ID)

                print('-------- account removed -----------', datern)


                if messagebox.showinfo(title='ACCOUNT SUCCESSFULLY REMOVED', message='account successfully removed, \nyou will automatically proceed back to account manager'):
                    print('--------- going back to account manager ------------', datern)
                    del_Admin.destroy()
                
                else:
                    del_Admin.destroy()

            else:
                print('-------- evaluation returns false --------', datern)
                if messagebox.showerror(title='INVALID KEYWORDS', message='Username and Password not Recognized'):
                    del_Admin.grab_set_global()

                else:
                    del_Admin.grab_set_global()

            con.commit()
            con2.commit()
            con.close()
            con2.close()
            

        def Reset_del():
            print('------- removing entries --------', datern)
            del_Admin.grab_release()

            if messagebox.askyesno(title='reset entries', message='do you really want to reset entries'):
                print('------- removing all entries -------', datern)

                del_adminUN.delete(0, END)
                del_adminPW.delete(0, END)
                IDto_del.delete(0, END)

                print('------- ENTRIES SUCCESSFULLY REMOVED --------', datern)
                del_Admin.grab_set_global()



            else:
                print('------ reset cancelled -------', datern)
                del_Admin.grab_set_global()
            

        def Cancel_del():
            print('------account deletion cancelled-------', datern)
            del_Admin.destroy()
            account_manager.grab_set_global()


        del_Admin = Toplevel(main)
        del_Admin.geometry('500x300+700+230')
        del_Admin.resizable(False, False)
        del_Admin.title('VERIFY TO DELETE')
        del_Admin.transient(main)
        del_Admin.iconphoto(True, mainicon)
        del_Admin.grab_set_global()

        
        del_AdminBG = ImageTk.PhotoImage(Image.open('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\backgrounds\\DeleteAdmin page.jpg'))
        del_Admincanv = Canvas(del_Admin, width=500, height=300)
        del_Admincanv.pack(fill='both')
        del_Admincanv.create_image(0, 0, anchor='nw', image=del_AdminBG)
        

    #ENTRY FOR ADMIN DELETE

        del_adminUN = Entry(del_Admin, fg='BLACK', bg='#C87018', font=('Gill Sans MT', 8),
                            cursor='xterm', width=50, relief=SOLID, highlightbackground="#FF6100", highlightthickness=1)
        del_adminUN.place(x=100, y=77)

        del_adminPW = Entry(del_Admin, fg='BLACK', bg='#C87018', font=('Gill Sans MT', 8),
                            cursor='xterm', width=50, relief=SOLID, highlightbackground="#FF6100", highlightthickness=1, show='*')
        del_adminPW.place(x=100, y=137)

        IDto_del = Entry(del_Admin, fg='BLACK', bg='#C87018', font=('Gill Sans MT', 8),
                         cursor='xterm', width=50, relief=SOLID, highlightbackground="#FF6100", highlightthickness=1)
        IDto_del.place(x=100, y=197)

    #BUTTONS FOR ADMIN DELETE

        confirm_del = Button(del_Admin, text='confirm', font=('Gill Sans MT', 10), bg='#B7630B', fg='BLACK',
                             activebackground='#B7630B', activeforeground='BLACK', cursor='hand2', borderwidth=1, compound=LEFT, relief=SOLID, width=20, command=Confirm_del)
        
        reset_del = Button(del_Admin, text='reset', font=('Gill Sans MT', 10), bg='#B7630B', fg='BLACK',
                           activebackground='#B7630B', activeforeground='BLACK', cursor='hand2', borderwidth=1, compound=LEFT, relief=SOLID, width=20, command=Reset_del)
        
        cancel_del = Button(del_Admin, text='cancel', font=('Gill Sans MT', 10), bg='#B7630B', fg='BLACK',
                            activebackground='#B7630B', activeforeground='BLACK', cursor='hand2', borderwidth=1, compound=LEFT, relief=SOLID, width=20, command=Cancel_del)
        
        confirm_del.place(x=25, y=255, height=33)
        reset_del.place(x=175, y=255, height=33)
        cancel_del.place(x=325, y=255, height=33)



    #Hovers sdkaasdadad

    def confirmaddIN(event):
        submit_credentials['bg'] = '#C87018'
        accounts_canvas.itemconfig(acchovermessage, text = 'add account as administrator - directs you to authentication log-in...')

    def confirmaddOUT(event):
        submit_credentials['bg'] = '#B7630B'
        accounts_canvas.itemconfig(acchovermessage, text = 'This is where you can manage administrator accounts...')

    def canceladdIN(event):
        cancel_credentials['bg'] = '#C87018'
        accounts_canvas.itemconfig(acchovermessage, text = 'cancel account adding - nothing will change...')

    def canceladdOUT(event):
        cancel_credentials['bg'] = '#B7630B'
        accounts_canvas.itemconfig(acchovermessage, text = 'This is where you can manage administrator accounts...')

    def resetaddIN(event):
        reset_credentials['bg'] = '#C87018'
        accounts_canvas.itemconfig(acchovermessage, text = 'removes everything in entry boxes...')

    def resetaddOUT(event):
        reset_credentials['bg'] = '#B7630B'
        accounts_canvas.itemconfig(acchovermessage, text = 'This is where you can manage administrator accounts...')

    def backtohomeIN(event):
        backto_home['bg'] = '#C87018'
        accounts_canvas.itemconfig(acchovermessage, text = 'bring you back to the main menu...')

    def backtohomeOUT(event):
        backto_home['bg'] = '#B7630B'
        accounts_canvas.itemconfig(acchovermessage, text = 'This is where you can manage administrator accounts...')


    def showadminIN(event):
        showhidden_admin['bg'] = '#C87018'
        accounts_canvas.itemconfig(acchovermessage, text = 'show Active administrators...')

    def showadminOUT(event):
        showhidden_admin['bg'] = '#B7630B'
        accounts_canvas.itemconfig(acchovermessage, text = 'This is where you can manage administrator accounts...')


    def deleteselaccIN(event):
        deleteselected_admin['bg'] = '#C87018'
        accounts_canvas.itemconfig(acchovermessage, text = 'delete a registered admin account ...')

    def deleteselacOUT(event):
        deleteselected_admin['bg'] = '#B7630B'
        accounts_canvas.itemconfig(acchovermessage, text = 'This is where you can manage administrator accounts...')


    account_manager = Toplevel(main)
    account_manager.title('Manage Administrator Acc')
    account_manager.geometry('1080x720+120+0')
    account_manager.resizable(False, False)
    account_manager.iconphoto(True, mainicon)
    account_manager.grab_set_global()
    account_manager.transient(main)

    account_managerBG = ImageTk.PhotoImage(Image.open('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\backgrounds\\Acc_manager page.jpg'))
    accounts_canvas = Canvas(account_manager, width=1080, height=720)
    accounts_canvas.pack(fill='both')
    accounts_canvas.create_image(0, 0, anchor='nw', image=account_managerBG)
    acchovermessage = accounts_canvas.create_text(10, 455, text='This is where you can manage administrator accounts...', font=('Consolas', 10), justify=LEFT, anchor=W)


    # entry boxes
        #add accounts - key <blank>ADD
    
    usernameADD = Entry(account_manager, fg='BLACK', bg='#C87018', font=('Gill Sans MT', 8),
                        cursor='xterm', width=37, relief=SOLID, highlightbackground="#FF6100", highlightthickness=1)
    
    passwordADD = Entry(account_manager, fg='BLACK', bg='#C87018', font=('Gill Sans MT', 8),
                        cursor='xterm', width=37, relief=SOLID, highlightbackground="#FF6100", highlightthickness=1, show='*')
    
    confirmPASS = Entry(account_manager, fg='BLACK', bg='#C87018', font=('Gill Sans MT', 8),
                        cursor='xterm', width=37, relief=SOLID, highlightbackground="#FF6100", highlightthickness=1, show='*')
    
    usernameADD.place(x=800, y=246)
    passwordADD.place(x=800, y=338)
    confirmPASS.place(x=800, y=430)

    #entry box 
        #command buttons - Key: <blank>_<blank>
        
    submit_credentials = Button(account_manager, text='confirm', font=('Gill Sans MT', 13), bg='#B7630B', fg='BLACK',
                             activebackground='#B7630B', activeforeground='BLACK', cursor='hand2', borderwidth=1, compound=LEFT, relief=SOLID, command=submitadminADD)
    submit_credentials.bind('<Enter>', confirmaddIN)
    submit_credentials.bind('<Leave>', confirmaddOUT)
    
    cancel_credentials = Button(account_manager, text='cancel', font=('Gill Sans MT', 13), bg='#B7630B', fg='BLACK',
                                activebackground='#B7630B', activeforeground='BLACK', cursor='hand2', borderwidth=1, compound=LEFT, relief=SOLID, command=cancel_input)
    cancel_credentials.bind('<Enter>', canceladdIN)
    cancel_credentials.bind('<Leave>', canceladdOUT)
    
    reset_credentials = Button(account_manager, text='reset', font=('Gill Sans MT', 13), bg='#B7630B', fg='BLACK',
                               activebackground='#B7630B', activeforeground='BLACK', cursor='hand2', borderwidth=1, compound=LEFT, relief=SOLID, command=resetentry)
    reset_credentials.bind('<Enter>', resetaddIN)
    reset_credentials.bind('<Leave>', resetaddOUT)
    
    submit_credentials.place(x=800, y=470, height=33)
    cancel_credentials.place(x=880, y=470, height=33)
    reset_credentials.place(x=950, y=470, height=33)

    #SideBar Buttons
        #command sidebar button cancel window focus -

    backto_home = Button(account_manager, text='Back to Home  ', font=('Gill Sans MT', 13), bg='#B7630B', fg='BLACK',
                         activebackground='#B7630B', activeforeground='BLACK', cursor='hand2', borderwidth=0, image= exit_icon, compound=LEFT, command=backtohomepage)
    backto_home.bind("<Enter>", backtohomeIN)
    backto_home.bind("<Leave>", backtohomeOUT)

    showhidden_admin = Button(account_manager, text='- refresh admin list.  ', font=('Gill Sans MT', 13), bg='#B7630B', fg='BLACK',
                               activebackground='#B7630B', activeforeground='BLACK', cursor='hand2', borderwidth=0, compound=LEFT, command=showadmins)
    showhidden_admin.bind('<Enter>', showadminIN)
    showhidden_admin.bind('<Leave>', showadminOUT)
    
    deleteselected_admin = Button(account_manager, text='- delete administrator.  ', font=('Gill Sans MT', 13), bg='#B7630B', fg='BLACK',
                                  activebackground='#B7630B', activeforeground='BLACK', cursor='hand2', borderwidth=0, compound=LEFT, command=deleteadmin)
    deleteselected_admin.bind('<Enter>', deleteselaccIN)
    deleteselected_admin.bind('<Leave>', deleteselacOUT)

    backto_home.place(x=10, y=200, height=33)
    showhidden_admin.place(x=10, y=240, height=33)
    deleteselected_admin.place(x=10, y=273, height=33)


    #leave this as Final line for this function

def closeapp():
    print('---------- user asked to exit program or not ------------', datern)
    if messagebox.askyesno(title='quit program', message='do really want to close the program?'):
        main.destroy()
        print('---------- program successfully stopped ---------------', datern)

    else:
        pass
        print('-------------- program continues user respond ;FALSE ----------------', datern)


con = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Administrator_Info\\administrators_username.db')
con2 = sqlite3.connect('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Administrator_Info\\administrators_password.db')
dial = con.cursor()
dial2 = con2.cursor()
#dial.execute("""CREATE TABLE usernames (username text)""")
#dial2.execute("""CREATE TABLE passwords (password text)""")

dial.execute("SELECT * from usernames")
dial2.execute("SELECT * from passwords")

global username
global password

username = ''
password = ''

fetched_username = dial.fetchall()
fetched_password = dial2.fetchall()

for indexU in fetched_username:
    username += str(indexU)


for indexP in fetched_password:
    password += str(indexP)




#----------------hover changes

def starthoverIN(event):
    start_button['bg'] = '#C87018'
    main_canvas.itemconfig(hover_message, text='start game window, set-up game and access main leaderboard and scoreboard...')

def starthoverOUT(event):
    start_button['bg'] = '#B7630B'
    main_canvas.itemconfig(hover_message, text='')


def loadhoverIN(event):
    loadgame_button['bg'] = '#C87018'
    main_canvas.itemconfig(hover_message, text='open previous games archives and access important game data...')

def loadhoverOUT(event):
    loadgame_button['bg'] = '#B7630B'
    main_canvas.itemconfig(hover_message, text='')


def settinghoverIN(event):
    settings_button['bg'] = '#C87018'
    main_canvas.itemconfig(hover_message, text='open application configuration for keybinds and control set-up to what ever you like...')

def settinghoverOUT(event):
    settings_button['bg'] = '#B7630B'
    main_canvas.itemconfig(hover_message, text='')


def accounthoverIN(event):
    accounts_button['bg'] = '#C87018'
    main_canvas.itemconfig(hover_message, text='Manage Administrator Account for Full Access...')

def accounthoverOUT(event):
    accounts_button['bg'] = '#B7630B'
    main_canvas.itemconfig(hover_message, text='')


def exithoverIN(event):
    exit_button['bg'] = '#C87018'
    main_canvas.itemconfig(hover_message, text='Exit to Desktop...')

def exithoverOUT(event):
    exit_button['bg'] = '#B7630B'
    main_canvas.itemconfig(hover_message, text='')


def creditshoverIN(event):
    credits_button['bg'] = '#C87018'
    main_canvas.itemconfig(hover_message, text='acknowledgement to all who helped build this application from scratch <3...')

def creditshoverOUT(event):
    credits_button['bg'] = '#B0600B'
    main_canvas.itemconfig(hover_message, text='')


def feedbackhoverIN(event):
    feedback_button['bg'] = '#C87018'
    main_canvas.itemconfig(hover_message, text='give us feedback on how we can improve the app <3...')

def feedbackhoverOUT(event):
    feedback_button['bg'] = '#B0600B'
    main_canvas.itemconfig(hover_message, text='')



#
main_bg = ImageTk.PhotoImage(Image.open('D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\backgrounds\\Main menu page.jpg'))
main_canvas = Canvas(main, width=1080, height=720)
main_canvas.pack(fill='both')
main_canvas.create_image(0, 0, anchor='nw', image=main_bg)
hover_message = main_canvas.create_text(55, 465, text='main menu, this where you can access all the features and etc...',
                                        font=('Consolas', 10), justify=LEFT, anchor=W)

#-----------------buttons

start_icon = PhotoImage(file= 'D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\icons\\Play Icon.png')
start_button = Button(main, text= '-    start game  ', font=('Consolas', 13), bg='#B7630B', activebackground='#B7630B',
                      fg='BLACK', activeforeground='BLACK', cursor='hand2', image=start_icon, compound=RIGHT, borderwidth=0, command=gamestartlogin)
start_button.bind('<Enter>', starthoverIN)
start_button.bind('<Leave>', starthoverOUT)
start_button.place(x=50, y=200, height=33)

loadgame_icon = PhotoImage(file= 'D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\icons\\Archive Icon.png')
loadgame_button = Button(main, text= '-    Load saved file  ', font=('Consolas', 13), bg='#B7630B', activebackground='#B7630B',
                         fg='BLACK', activeforeground='BLACK', cursor='hand2', image=loadgame_icon, compound=RIGHT, borderwidth=0, command=mainlogin_page)
loadgame_button.bind('<Enter>', loadhoverIN)
loadgame_button.bind('<Leave>', loadhoverOUT)
loadgame_button.place(x=50, y=233, height=33)

settings_icon = PhotoImage(file= 'D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\icons\\Setting Icon.png')
settings_button = Button(main, text= '-    settings  ', font=('Consolas', 13), bg='#B7630B', activebackground='#B7630B',
                         fg='BLACK', activeforeground='BLACK', cursor='hand2', image=settings_icon, compound=RIGHT, borderwidth=0, command=gsuplayerdata)
settings_button.bind('<Enter>', settinghoverIN)
settings_button.bind('<Leave>', settinghoverOUT)
settings_button.place(x=50, y=266, height=33)

accounts_icon = PhotoImage(file= 'D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\icons\\Profile Icon.png')
accounts_button = Button(main, text= '-    Manage Admin Accounts  ', font=('Consolas', 13), bg='#B7630B', activebackground='#B7630B',
                         fg='BLACK', activeforeground='BLACK', cursor='hand2', image=accounts_icon, compound=RIGHT, borderwidth=0, command=manageaccount)
accounts_button.bind('<Enter>', accounthoverIN)
accounts_button.bind('<Leave>', accounthoverOUT)
accounts_button.place(x=50, y=299, height=33)

exit_icon = PhotoImage(file= 'D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\icons\\Exit Icon.png')
exit_button = Button(main, text= '-    Exit to desktop  ', font=('Consolas', 13), bg='#B7630B', activebackground='#B7630B',
                     fg='BLACK', activeforeground='BLACK', cursor='hand2', image=exit_icon, compound=RIGHT, borderwidth=0, command=closeapp)
exit_button.bind('<Enter>', exithoverIN)
exit_button.bind('<Leave>', exithoverOUT)
exit_button.place(x=50, y=333, height=33)

feedback_icon = PhotoImage(file= 'D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\icons\\Feedback Icon.png')
feedback_button = Button(main, text= 'Give us Feedback ', font=('Consolas', 10), bg='#B0600B', activebackground='#B0600B',
                         fg='BLACK', activeforeground='BLACK', cursor='hand2', image=feedback_icon, compound=LEFT, borderwidth=0)
feedback_button.bind('<Enter>', feedbackhoverIN)
feedback_button.bind('<Leave>', feedbackhoverOUT)
feedback_button.place(x=880, y=510, height=33)

credits_icon = PhotoImage(file= 'D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\Thumbnails\\icons\\Credits Icon.png')
credits_button = Button(main, text= 'Credits ', font=('Consolas', 10), bg='#B0600B', activebackground='#B0600B',
                        fg='BLACK', activeforeground='BLACK', cursor='hand2', image=credits_icon, compound=LEFT, borderwidth=0)
credits_button.bind('<Enter>', creditshoverIN)
credits_button.bind('<Leave>', creditshoverOUT)
credits_button.place(x=945, y=543, height=33)

con.commit()
con2.commit()
con.close()
con2.close()
main.geometry('1080x720+120+0')
main.title('Basketball Sport Point System')
main.resizable(False, False)
mainicon = PhotoImage(file="D:\\Gunjou Desu\\Gunjou Acadsu\\GunjouDesu\\GunjouDesu\\data structure and algorithm\\MAIN BASKETBALL FOLDER\\sport point system\\bspsicon.ico")
main.iconphoto(True, mainicon)
main.mainloop()