import csv
from doctest import master
from tkinter.ttk import Label, Style, Combobox, Button
import PIL.Image
import pandas as pd
from PIL import ImageTk
from matplotlib import pyplot as plt

from pygubu import builder
from pygubu.widgets.scrolledframe import ScrolledFrame

try:
    import tkinter as tk  # for python 3
    from tkinter import messagebox, ttk
except:
    import Tkinter as tk  # for python 2
    import tkMessageBox as messagebox

import threading
import pygubu


def startUI():
    root = tk.Tk()
    root.title("NBA SEASON")
    app = Application(root)
    root.mainloop()
    return


with open('teamRecord.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


class Application:
    def __init__(self, master):
        global value, value1
        value1 = 0
        try:
            self.P_Base = ttk.Panedwindow(master, orient='vertical')
            self.frame1 = ttk.Frame(self.P_Base, padding="5")
            self.button1 = ttk.Button(self.frame1)
            self.button1.configure(takefocus=False, text='Team Stats', command=self.on_click)
            self.button1.pack(side='left')
            self.button2 = ttk.Button(self.frame1)
            self.button2.configure(text='Injuries')
            self.button2.pack(side='left')
            self.button2.configure(command=self.new_window)
            self.button3 = ttk.Button(self.frame1)
            self.button3.configure(text='Full Standings')
            self.button3.pack(side='left')
            self.button3.configure(command=self.on_click1)
            self.button4 = ttk.Button(self.frame1)
            self.button4.configure(text='Champions')
            self.button4.pack(side='left')
            self.button4.configure(command=self.on_click2)

            self.button1.pack(ipadx='5', ipady='5', padx='25', pady='5', side='left')
            self.button2.pack(ipadx='5', ipady='5', padx='25', pady='5', side='left')
            self.button3.pack(ipadx='5', ipady='5', padx='25', pady='5', side='left')
            self.button4.pack(ipadx='5', ipady='5', padx='25', pady='5', side='left')

            self.frame1.configure(height='200', relief='groove', width='200', borderwidth='3')
            self.frame1.pack(side='top')
            self.P_Base.add(self.frame1, weight='1')
            self.panedwindow2 = ttk.Panedwindow(self.P_Base, orient='horizontal')
            self.scrolledframe1 = ScrolledFrame(self.panedwindow2, scrolltype='both')
            self.listbox1 = tk.Listbox(self.scrolledframe1.innerframe)

            for i in range(len(data)):
                self.listbox1.insert(i, data[i])

            self.listbox1.configure(activestyle='dotbox', background='lightblue', borderwidth='2', cursor='arrow',
                                    font='TkFixedFont', foreground='black', height='30',
                                    highlightbackground='lightblue',
                                    highlightcolor='darkblue', justify='center', relief='groove',
                                    selectbackground='black',
                                    selectborderwidth='3', selectforeground='white', width='25')
            self.listbox1.pack(side='top')
            self.scrolledframe1.configure(usemousewheel=False, borderwidth='3')
            self.scrolledframe1.pack(side='top')
            self.panedwindow2.add(self.scrolledframe1, weight='15')
            self.label1 = ttk.Label(self.panedwindow2)
            self.label1.configure(text='label1')
            self.label1.pack(side='top')

            # Read the Image
            image = PIL.Image.open("1.png")

            # Reszie the image using resize() method
            resize_image = image.resize((335, 335))

            img = ImageTk.PhotoImage(resize_image)

            # create label and add resize image
            label1 = Label(image=img, justify="center", padding="5", borderwidth='3')
            label1.image = img
            label1.pack()

            self.panedwindow2.add(label1, weight='1')
            self.panedwindow2.configure(height='200', width='200')
            self.panedwindow2.pack(side='top')
            self.P_Base.add(self.panedwindow2, weight='50')
            self.notebook1 = ttk.Notebook(self.P_Base)

            self.frame5 = ttk.Frame(self.notebook1)

            self.frame2 = ttk.Frame(self.frame5)
            self.frame2.configure(height='25', width='200')
            self.frame2.pack(side='bottom', pady='5')
            style = ttk.Style()
            style.theme_use('default')
            style.configure("grey.Horizontal.TProgressbar", background='blue')
            self.progressbar2 = ttk.Progressbar(self.frame5, style='grey.Horizontal.TProgressbar')
            self.progressbar2.configure(length='500', maximum='100', orient='horizontal', takefocus=True)
            self.progressbar2.configure(value='50')
            self.progressbar2.pack(ipady='1', pady='5', side='top')
            style = Style()

            style.configure('TButton', font=('calibri', 10, 'bold'), borderwidth='4', background="lightblue")
            style.map('TButton',
                      foreground=[("pressed", "white"), ("active", "black")],
                      background=[("pressed", "!disabled", "green"), ("active", "lightgreen")], )

            self.label2 = ttk.Label(self.frame5)
            self.label2.configure(text=self.progressbar2['value'])
            self.label2.pack(side='top')

            self.progressbar3 = ttk.Progressbar(self.frame5)
            self.progressbar3.configure(length='500', maximum='100', orient='horizontal', takefocus=True)
            self.progressbar3.configure(value='50')
            self.progressbar3.pack(ipady='1', pady='5', side='top')

            self.label3 = ttk.Label(self.frame5)
            self.label3.configure(text=self.progressbar3['value'])
            self.label3.pack(side='top')

            self.combobox1 = Combobox(self.frame5)
            self.combobox1.pack(side='top', pady='5')
            self.combobox2 = Combobox(self.frame5)
            self.combobox2.pack(side='top')

            self.combobox1['values'] = ('GSW', 'ATL', 'BOS', 'BRK', 'CHO', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'HOU',
                                        'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL',
                                        'PHI', 'PHO'',POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS')

            self.combobox2['values'] = ('GSW', 'ATL', 'BOS', 'BRK', 'CHO', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'HOU',
                                        'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL',
                                        'PHI', 'PHO'',POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS')

            selectedteams = ['ATL']

            def on_select1(event):
                selected1 = event.widget.get()

                selectedteams.append(selected1)
                ratings1 = []
                dataset = pd.read_csv("teamRecord1.csv")
                for i in range(29):
                    ratings = dataset['Team'].values[i], dataset['Win'].values[i], dataset['Loss'].values[i], \
                              dataset['Offense'].values[i], dataset['Standings'].values[i], dataset['Stats'].values[i]
                    ratings1.append(ratings)

                titles = ['Team', 'Win', 'Loss', 'Offense', 'Standings', 'Stats']
                standings = pd.DataFrame(ratings1, columns=titles)
                for j in range(29):
                    if selectedteams[-1] in ratings1[j]:
                        value1 = ratings1[j][1]
                        value2 = ratings1[j][2]
                        value3 = ratings1[j][3]
                        value4 = ratings1[j][4]
                        value5 = ratings1[j][5]

                        self.checkbutton1 = ttk.Checkbutton(self.frame5)
                        self.checkbutton1.configure(offvalue='0', onvalue=value1, takefocus=False, text='Injuries')
                        self.checkbutton1.pack(side='left')
                        self.checkbutton1.configure(command=self.check1)
                        self.checkbutton1.pack(ipadx='0', padx='40')

                        self.checkbutton2 = ttk.Checkbutton(self.frame5)
                        self.checkbutton2.configure(offvalue='0', onvalue=value2, takefocus=False, text='Defense')
                        self.checkbutton2.pack(side='left')
                        self.checkbutton2.configure(command=self.check2)
                        self.checkbutton2.pack(ipadx='10', padx='10')

                        self.checkbutton3 = ttk.Checkbutton(self.frame5)
                        self.checkbutton3.configure(offvalue='0', onvalue=value3, takefocus=False, text='Offense')
                        self.checkbutton3.pack(side='left')
                        self.checkbutton3.configure(command=self.check3)
                        self.checkbutton3.pack(ipadx='10', padx='10')

                        self.checkbutton4 = ttk.Checkbutton(self.frame5)
                        self.checkbutton4.configure(offvalue='0', onvalue=value4, takefocus=False, text='Standings')
                        self.checkbutton4.pack(side='left')
                        self.checkbutton4.configure(command=self.check4)
                        self.checkbutton4.pack(ipadx='10', padx='10')

                        self.checkbutton5 = ttk.Checkbutton(self.frame5)
                        self.checkbutton5.configure(offvalue='0', onvalue=value5, takefocus=False, text='Stats')
                        self.checkbutton5.pack(side='left')
                        self.checkbutton5.configure(command=self.check5)
                        self.checkbutton5.pack(ipadx='10', padx='10')

            def on_select2(event):
                selected2 = event.widget.get()
                selectedteams.append(selected2)
                ratings2 = []
                dataset = pd.read_csv("teamRecord1.csv")
                for i in range(29):
                    ratings3 = dataset['Team'].values[i], dataset['Win'].values[i], dataset['Loss'].values[i], \
                               dataset['Offense'].values[i], dataset['Standings'].values[i], dataset['Stats'].values[i]
                    ratings2.append(ratings3)

                titles = ['Team', 'Win', 'Loss', 'Offense', 'Standings', 'Stats']
                standings = pd.DataFrame(ratings2, columns=titles)

                for j in range(29):
                    if selectedteams[-1] in ratings2[j]:
                        value6 = ratings2[j][1]
                        value7 = ratings2[j][2]
                        value8 = ratings2[j][3]
                        value9 = ratings2[j][4]
                        value10 = ratings2[j][5]

                self.checkbutton6 = ttk.Checkbutton(self.frame2)
                self.checkbutton6.configure(offvalue='0', onvalue=value6, takefocus=False, text='Injuries')
                self.checkbutton6.pack(side='left')
                self.checkbutton6.configure(command=self.check6)
                self.checkbutton6.pack(ipadx='10', padx='20')

                self.checkbutton7 = ttk.Checkbutton(self.frame2)
                self.checkbutton7.configure(offvalue='0', onvalue=value7, takefocus=False, text='Defense')
                self.checkbutton7.pack(side='left')
                self.checkbutton7.configure(command=self.check7)
                self.checkbutton7.pack(ipadx='10', padx='10')

                self.checkbutton8 = ttk.Checkbutton(self.frame2)
                self.checkbutton8.configure(offvalue='0', onvalue=value8, takefocus=False, text='Offense')
                self.checkbutton8.pack(side='left')
                self.checkbutton8.configure(command=self.check8)
                self.checkbutton8.pack(ipadx='10', padx='10')

                self.checkbutton9 = ttk.Checkbutton(self.frame2)
                self.checkbutton9.configure(offvalue='0', onvalue=value9, takefocus=False, text='Standings')
                self.checkbutton9.pack(side='left')
                self.checkbutton9.configure(command=self.check9)
                self.checkbutton9.pack(ipadx='10', padx='10')

                self.checkbutton10 = ttk.Checkbutton(self.frame2)
                self.checkbutton10.configure(offvalue='0', onvalue=value10, takefocus=False, text='Stats')
                self.checkbutton10.pack(side='left')
                self.checkbutton10.configure(command=self.check10)
                self.checkbutton10.pack(ipadx='10', padx='10')

            self.combobox1.bind('<<ComboboxSelected>>', on_select1)
            self.combobox2.bind('<<ComboboxSelected>>', on_select2)

            self.frame5.configure(height='200', width='200', borderwidth='3')
            self.frame5.pack(side='top')
            self.notebook1.add(self.frame5, text='Game Prediction')
            self.text1 = tk.Text(self.notebook1)
            self.text1.configure(background='teal', exportselection='true', height='10', insertunfocussed='solid')
            self.text1.configure(width='50')

            dat1 = pd.read_csv("nbagames.csv")
            dat1['Steals'].value_counts(sort=False)

            bins = pd.cut(dat1['Steals'], 4)
            bins.value_counts(sort=False)

            _text_ = bins.value_counts(sort=False)
            self.text1.insert('0.0', _text_)
            self.text1.pack(side='top')
            self.notebook1.add(self.text1, text='Steals Range')

            self.notebook1.configure(height='200', width='200')
            self.notebook1.pack(side='top')
            self.text1 = tk.Text(self.notebook1)
            self.text1.configure(background='teal', exportselection='true', height='10', insertunfocussed='solid')
            self.text1.configure(width='50')
            bins = pd.cut(dat1['TeamPoints'], 4)
            bins.value_counts(sort=False)

            _text_ = bins.value_counts(sort=False)
            self.text1.insert('0.0', _text_)
            self.text1.pack(side='top')
            self.notebook1.add(self.text1, text='TeamPoints Tips')

            self.P_Base.add(self.notebook1, weight='1')
            self.P_Base.configure(height='600', width='600')
            self.P_Base.pack(side='top')
        except:
            print()

    def on_click(self):
        self.newWindow = tk.Toplevel(master)
        self.app = Demo1(self.newWindow)



    def on_click1(self):
        self.newWindow = tk.Toplevel(master)
        self.app = Demo2(self.newWindow)


    def on_click2(self):
        import test1

    def check1(self):
        self.progressbar2['value'] = self.progressbar2['value'] + int(self.checkbutton1['onvalue']) - int(
            self.checkbutton1['offvalue'])
        self.progressbar3['value'] = self.progressbar3['value'] - int(self.checkbutton1['onvalue']) + int(
            self.checkbutton1['offvalue'])
        newvalue = self.checkbutton1['onvalue']
        self.checkbutton1['onvalue'] = self.checkbutton1['offvalue']
        self.checkbutton1['offvalue'] = newvalue
        self.label2.configure(text=self.progressbar2['value'])
        self.label3.configure(text=self.progressbar3['  value'])

    def check2(self):
        self.progressbar2['value'] = self.progressbar2['value'] - int(self.checkbutton2['onvalue']) + int(
            self.checkbutton2['offvalue'])
        self.progressbar3['value'] = self.progressbar3['value'] + int(self.checkbutton2['onvalue']) - int(
            self.checkbutton2['offvalue'])
        newvalue = self.checkbutton2['onvalue']
        self.checkbutton2['onvalue'] = self.checkbutton2['offvalue']
        self.checkbutton2['offvalue'] = newvalue
        self.label2.configure(text=self.progressbar2['value'])
        self.label3.configure(text=self.progressbar3['value'])

    def check3(self):
        self.progressbar2['value'] = self.progressbar2['value'] + int(self.checkbutton3['onvalue']) - int(
            self.checkbutton3['offvalue'])
        self.progressbar3['value'] = self.progressbar3['value'] - int(self.checkbutton3['onvalue']) + int(
            self.checkbutton3['offvalue'])
        newvalue = self.checkbutton3['onvalue']
        self.checkbutton3['onvalue'] = self.checkbutton3['offvalue']
        self.checkbutton3['offvalue'] = newvalue
        self.label2.configure(text=self.progressbar2['value'])
        self.label3.configure(text=self.progressbar3['value'])

    def check4(self):
        self.progressbar2['value'] = self.progressbar2['value'] + int(self.checkbutton4['onvalue']) - int(
            self.checkbutton4['offvalue'])
        self.progressbar3['value'] = self.progressbar3['value'] - int(self.checkbutton4['onvalue']) + int(
            self.checkbutton4['offvalue'])
        newvalue = self.checkbutton4['onvalue']
        self.checkbutton4['onvalue'] = self.checkbutton4['offvalue']
        self.checkbutton4['offvalue'] = newvalue
        self.label2.configure(text=self.progressbar2['value'])
        self.label3.configure(text=self.progressbar3['value'])

    def check5(self):
        self.progressbar2['value'] = self.progressbar2['value'] + int(self.checkbutton5['onvalue']) - int(
            self.checkbutton5['offvalue'])
        self.progressbar3['value'] = self.progressbar3['value'] - int(self.checkbutton5['onvalue']) + int(
            self.checkbutton5['offvalue'])
        newvalue = self.checkbutton5['onvalue']
        self.checkbutton5['onvalue'] = self.checkbutton5['offvalue']
        self.checkbutton5['offvalue'] = newvalue
        self.label2.configure(text=self.progressbar2['value'])
        self.label3.configure(text=self.progressbar3['value'])

    def check6(self):
        self.progressbar3['value'] = self.progressbar3['value'] + int(self.checkbutton6['onvalue']) - int(
            self.checkbutton6['offvalue'])
        self.progressbar2['value'] = self.progressbar2['value'] - int(self.checkbutton6['onvalue']) + int(
            self.checkbutton6['offvalue'])
        newvalue = self.checkbutton6['onvalue']
        self.checkbutton6['onvalue'] = self.checkbutton6['offvalue']
        self.checkbutton6['offvalue'] = newvalue
        self.label3.configure(text=self.progressbar3['value'])
        self.label2.configure(text=self.progressbar2['value'])

    def check7(self):
        self.progressbar3['value'] = self.progressbar3['value'] - int(self.checkbutton7['onvalue']) + int(
            self.checkbutton7['offvalue'])
        self.progressbar2['value'] = self.progressbar2['value'] + int(self.checkbutton7['onvalue']) - int(
            self.checkbutton7['offvalue'])
        newvalue = self.checkbutton7['onvalue']
        self.checkbutton7['onvalue'] = self.checkbutton7['offvalue']
        self.checkbutton7['offvalue'] = newvalue
        self.label3.configure(text=self.progressbar3['value'])
        self.label2.configure(text=self.progressbar2['value'])

    def check8(self):
        self.progressbar3['value'] = self.progressbar3['value'] + int(self.checkbutton8['onvalue']) - int(
            self.checkbutton8['offvalue'])
        self.progressbar2['value'] = self.progressbar2['value'] - int(self.checkbutton8['onvalue']) + int(
            self.checkbutton8['offvalue'])
        newvalue = self.checkbutton8['onvalue']
        self.checkbutton8['onvalue'] = self.checkbutton8['offvalue']
        self.checkbutton8['offvalue'] = newvalue
        self.label3.configure(text=self.progressbar3['value'])
        self.label2.configure(text=self.progressbar2['value'])

    def check9(self):
        self.progressbar3['value'] = self.progressbar3['value'] + int(self.checkbutton9['onvalue']) - int(
            self.checkbutton9['offvalue'])
        self.progressbar2['value'] = self.progressbar2['value'] - int(self.checkbutton9['onvalue']) + int(
            self.checkbutton9['offvalue'])
        newvalue = self.checkbutton9['onvalue']
        self.checkbutton9['onvalue'] = self.checkbutton9['offvalue']
        self.checkbutton9['offvalue'] = newvalue
        self.label3.configure(text=self.progressbar3['value'])
        self.label2.configure(text=self.progressbar2['value'])

    def check10(self):
        self.progressbar3['value'] = self.progressbar3['value'] + int(self.checkbutton10['onvalue']) - int(
            self.checkbutton10['offvalue'])
        self.progressbar2['value'] = self.progressbar2['value'] - int(self.checkbutton10['onvalue']) + int(
            self.checkbutton10['offvalue'])
        newvalue = self.checkbutton10['onvalue']
        self.checkbutton10['onvalue'] = self.checkbutton10['offvalue']
        self.checkbutton10['offvalue'] = newvalue
        self.label3.configure(text=self.progressbar3['value'])
        self.label2.configure(text=self.progressbar2['value'])

    def quit(self, event=None):
        self.mainwindow.quit()

    def run(self):
        self.mainwindow.mainloop()

    def quit1(self, event=None):
        self.newWindow.quit()

    def run1(self):
        self.newWindow.mainloop()

    def new_window(selfzz):

        root = tk.Tk()
        root.title("Search Records")

        # setting the windows size
        root.geometry("300x150")

        # declaring string variable
        # for storing name and password
        Playername_var = tk.StringVar()
        Team_var = tk.StringVar()
        Year1_var = tk.StringVar()
        Year2_var = tk.StringVar()

        # creating a label for
        # name using widget Label
        Playername_label = tk.Label(root, text='Player Name', font=('calibre', 10, 'bold'))

        # creating a entry for input
        # name using widget Entry
        Playername_entry = tk.Entry(root, textvariable=Playername_var, font=('calibre', 10, 'normal'))

        # creating a label for password
        Team_label = tk.Label(root, text='Team', font=('calibre', 10, 'bold'))

        # creating a entry for password
        Team_entry = tk.Entry(root, textvariable=Team_var, font=('calibre', 10, 'normal'))

        # name using widget Label
        Year1_label = tk.Label(root, text='From year', font=('calibre', 10, 'bold'))

        # creating a entry for input
        # name using widget Entry
        Year1_entry = tk.Entry(root, textvariable=Year1_var, font=('calibre', 10, 'normal'))

        # creating a label for password
        Year2_label = tk.Label(root, text='To Year', font=('calibre', 10, 'bold'))

        # creating a entry for password
        Year2_entry = tk.Entry(root, textvariable=Year2_var, font=('calibre', 10, 'normal'))
        # creating a button using the widget
        # Button that will call the submit function
        sub_btn = tk.Button(root, text='Submit')

        sub_btn = tk.Button(root, text='Submit', command=root.destroy)

        # placing the label and entry in
        # the required position using grid
        # method
        Playername_label.grid(row=0, column=0)
        Playername_entry.grid(row=0, column=1)
        Team_label.grid(row=1, column=0)
        Team_entry.grid(row=1, column=1)

        Year1_label.grid(row=2, column=0)
        Year1_entry.grid(row=2, column=1)
        Year2_label.grid(row=3, column=0)
        Year2_entry.grid(row=3, column=1)

        sub_btn.grid(row=4, column=1)

        # performing an infinite loop
        # for the window to display
        root.mainloop()

        ###########################################################################
        ###########################################################################
        data1 = pd.read_csv('injuries_2010-2020.csv', header=None)
        data1.columns = ['Date', 'Team', 'Acquired', 'Relinquished', 'Notes']
        # DataFrame
        dfp = pd.DataFrame(data1)
        df2 = dfp[(dfp["Relinquished"] == Playername_var.get()) & (dfp["Date"] >= Year1_var.get()) & (
                dfp["Date"] <= "Year2_var.get()")]
        print(df2[['Team', 'Date', 'Relinquished']])

        data2 = pd.read_csv('nbagames.csv', header=None)
        data2.columns = ['', 'Team', 'Game', 'Date', 'Home', 'Opponent', 'WINorLOSS', 'TeamPoints', 'OpponentPoints',
                         'FieldGoals', 'FieldGoalsAttempted', 'FieldGoals.', 'X3PointShots', 'X3PointShotsAttempted',
                         'X3PointShots.', 'FreeThrows', 'FreeThrowsAttempted', 'FreeThrows.', 'OffRebounds',
                         'TotalRebounds',
                         'Assists', 'Steals', 'Blocks', 'Turnovers', 'TotalFouls', 'Opp.FieldGoals',
                         'Opp.FieldGoalsAttempted',
                         'Opp.FieldGoals.', 'Opp.3PointShots', 'Opp.3PointShotsAttempted', 'Opp.3PointShots.',
                         'Opp.FreeThrowsOpp.', 'FreeThrowsAttempted', 'Opp.FreeThrows.', 'Opp.OffRebounds',
                         'Opp.TotalRebounds',
                         'Opp.Assists', 'Opp.Steals', 'Opp.Blocks', 'Opp.Turnovers', 'Opp.TotalFouls']
        # DataFrame
        df = pd.DataFrame(data2)
        df1 = df[(df["Team"] == Team_var.get()) & (df["Date"] >= Year1_var.get()) & (df["Date"] <= Year2_var.get())]
        print(df1[['Team', 'Date', 'WINorLOSS']])

        print("========================================================")
        print("========================================================")
        print("========================================================")
        print("========================================================")

        ###################################################################################
        def show():
            for item in df2['Date']:
                for item1 in df1['Date']:

                    if item == item1:

                        df3 = (df1.loc[df1['Date'] == item1])
                        df4 = (df2.loc[df2['Date'] == item1])
                        for item2 in df4['Relinquished']:
                            for item3 in df3['WINorLOSS']:
                                for item5 in df3['Team']:
                                    listBox.insert("", "end", values=(item, item2, item3, item5))

        records = tk.Tk()
        records.title('Records')
        label = tk.Label(records, text="Records", font=("Arial", 30)).grid(row=0, columnspan=3)
        # create Treeview with 3 columns
        cols = ('Date', 'Player', 'WINorLOSS', 'Team')
        listBox = ttk.Treeview(records, columns=cols, show='headings')
        # set column headings
        for col in cols:
            listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)

        showScores = tk.Button(records, text="Show scores", width=15, command=show).grid(row=4, column=0)
        closeButton = tk.Button(records, text="Close", width=15, command=records.destroy).grid(row=4, column=1)

        records.mainloop()

        ###################################################################################
        def CompareDates():
            win = 0
            loss = 0
            for item in df2['Date']:
                for item1 in df1['Date']:
                    if item == item1:
                        df3 = (df1.loc[df1['Date'] == item1])
                        #       print(df3['WINorLOSS'])

                        for item3 in df3['WINorLOSS']:
                            if (item3 == 'W'):
                                win = win + 1


                            else:
                                loss = loss + 1
            print("win=", win)
            print("LOSS=", loss)
            result1 = win / loss
            result2 = (1 - result1)
            if (win > loss):
                print("Mungesa e lojtarit nuk ka pasur ndikim negativ me:", result1)
            elif (loss > win):
                print("Mungesa e lojtarit ka pasur ndikim negativ me:", result2)
            else:
                print("Mungesa e lojtarit nuk ka pasur ndikim negativ apo pozitiv.")

            fig = plt.figure()
            ax = fig.add_axes([0, 0, 0.5, 0.5])
            langs = ['WIN', 'LOSS']
            students = [win, loss]
            ax.bar(langs, students)
            plt.show()

        try:
            CompareDates()
        except:
            print("An error occurred while executing the function!")



class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.listbox1 = tk.Listbox(self.frame)

        titles = ['Team', 'Win', 'Loss', 'Offense', 'Standings', 'Stats']
        ratings1 = []
        ratings1.append(titles)
        dataset = pd.read_csv("teamRecord1.csv")
        for i in range(29):
            ratings = dataset['Team'].values[i], dataset['Win'].values[i], dataset['Loss'].values[i], \
                      dataset['Offense'].values[i], dataset['Standings'].values[i], dataset['Stats'].values[i]
            ratings1.append(ratings)

        for i in range(len(ratings1)):
            self.listbox1.insert(i, ratings1[i])

        self.listbox1.configure(activestyle='dotbox', background='lightblue', borderwidth='2', cursor='arrow',
                                font='TkFixedFont', foreground='black', height='25',
                                highlightbackground='lightblue', justify = "center",
                                highlightcolor='darkblue', relief='groove',
                                selectbackground='black',
                                selectborderwidth='3', selectforeground='white', width='50')
        self.listbox1.pack(side='top')
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Application(self.newWindow)


class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.listbox1 = tk.Listbox(self.frame)

        titles = ['Team', 'Win', 'Loss']
        ratings1 = []
        ratings1.append(titles)
        dataset = pd.read_csv("teamRecord.csv")
        for i in range(29):
            ratings = dataset['Team'].values[i], dataset['Win'].values[i], dataset['Loss'].values[i]
            ratings1.append(ratings)

        for i in range(len(ratings1)):
            self.listbox1.insert(i, ratings1[i])

        self.listbox1.configure(activestyle='dotbox', background='lightblue', borderwidth='2', cursor='arrow',
                                font='TkFixedFont', foreground='black', height='25',
                                highlightbackground='lightblue',
                                highlightcolor='darkblue', relief='groove', justify = "center",
                                selectbackground='black',
                                selectborderwidth='3', selectforeground='white', width='30')
        self.listbox1.pack(side='top')
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Application(self.newWindow)


if __name__ == '__main__':
    t = threading.Thread(target=startUI)
    t.start()
