from tkinter import *
from tkinter import messagebox
import pandas as pd
import ctypes as ct

class ui:
    isResultDisplayed = False

    color1 = '#93B1A6'
    color2 = '#5C8374'
    color3 = '#183D3D'
    color4 = '#040D12'
    color5 = '#d5e3de'

    def window_config(self):
        ct.windll.shcore.SetProcessDpiAwareness(1)

    # init 
    def __init__(self, name):
        self.window_config()
        
        self.name: str = name
        self.window = Tk()
        self.window.title(self.name)
        self.window.geometry('500x350')
        self.window.resizable(False, False)
        self.window.configure(bg=self.color3)
        self.window.eval('tk::PlaceWindow . center')

        # custom title bar
        self.window.overrideredirect(True)
        title_bar = Frame(self.window, bg=self.color3, relief="raised", bd=2)

        # create title label
        title_label = Label(title_bar, text=self.name, bg=self.color3, fg=self.color5, font=('Arial', 15))
        title_label.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        close_button = Button(title_bar, text=" X ",font=('Arial',8, 'bold'), command=exit,bg=self.color5)
        close_button.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        title_bar.columnconfigure(0, weight=5)
        title_bar.columnconfigure(0, weight=1)
        title_bar.pack(fill=X, padx=0)
        
        # title function
        def get_title_click(event):
            global title_click_x, title_click_y
            title_click_x = event.x_root
            title_click_y = event.y_root

        def move_window(event):
            global title_click_x, title_click_y
            new_pos_x = self.window.winfo_x() + (event.x_root - title_click_x)
            new_pos_y = self.window.winfo_y() + (event.y_root - title_click_y)
            self.window.geometry(f'+{new_pos_x}+{new_pos_y}')
            title_click_x = event.x_root
            title_click_y = event.y_root
        
        title_bar.bind('<Button-1>',get_title_click)
        title_bar.bind('<B1-Motion>',move_window)        
        title_label.bind('<Button-1>',get_title_click)
        title_label.bind('<B1-Motion>',move_window)

        def on_btn_hover(event):
            event.widget['background'] = self.color2
        def on_btn_leave(event):
            event.widget['background'] = self.color5


        # # create header label
        # self.header_label = Label(self.window,text='BMI Calculator',font=('Arial',20), bg=self.color3, fg=self.color5)
        # self.header_label.pack(pady=10)
        # create main frame
        self.main_frame = Frame(self.window,padx=10,pady=10,bg=self.color1)
        self.main_frame.pack(fill=BOTH,expand=True)
        # create input with grid
        self.name_label = Label(self.main_frame,text='Name',font=('Arial',15 ),bg=self.color1, fg=self.color4)
        self.name_label.grid(row=0,column=0,padx=10,pady=10,)
        self.name_entry = Entry(self.main_frame,font=('Arial',15),bg=self.color5)
        self.name_entry.grid(row=0,column=1,padx=10,pady=10)

        self.weight_label = Label(self.main_frame,text='Weight (kg)',font=('Arial',15),bg=self.color1, fg=self.color4)
        self.weight_label.grid(row=2,column=0,padx=10,pady=10)
        self.weight_entry = Entry(self.main_frame,font=('Arial',15),bg=self.color5)
        self.weight_entry.grid(row=2,column=1,padx=10,pady=10)
        
        self.height_label = Label(self.main_frame,text='Height (cm)',font=('Arial',15),bg=self.color1, fg=self.color4)
        self.height_label.grid(row=1,column=0,padx=10,pady=10)
        self.height_entry = Entry(self.main_frame,font=('Arial',15),bg=self.color5)
        self.height_entry.grid(row=1,column=1,padx=10,pady=10)

        # create button
        self.calculate_button = Button(self.main_frame,text='Calculate',font=('Arial',15),bg=self.color5,command=self.calculate)
        self.calculate_button.grid(row=3,column=0,columnspan=2,padx=10,pady=50,sticky='we')

        self.calculate_button.bind('<Enter>',on_btn_hover)
        self.calculate_button.bind('<Leave>',on_btn_leave)
        

    def calculate(self):        
        def on_btn_hover(event):
            event.widget['background'] = self.color2
        def on_btn_leave(event):
            event.widget['background'] = self.color5


        if self.isResultDisplayed:
            return
        else:
            self.isResultDisplayed = True
   
        try:
            self.username = self.name_entry.get()
            if self.username == '':
                self.isResultDisplayed = False
                messagebox.showerror('Error','Please enter your name')
                return

            self.weight = float(self.weight_entry.get())
            self.height = float(self.height_entry.get())
            self.bmi = self.weight / ((self.height/100)**2)
            self.bmi = round(self.bmi,2)

            if self.bmi < 18.5:
                self.type = 'Underweight'
            elif self.bmi >= 18.5 and self.bmi < 25:
                self.type = 'Normal'
            elif self.bmi >= 25 and self.bmi < 30:
                self.type = 'Overweight'
            elif self.bmi >= 30:
                self.type = 'Obese'

        except:
            self.isResultDisplayed = False
            messagebox.showerror('Error','Please enter valid number')
            return

        

        self.result_window = Tk()
        self.result_window.title('Result')
        self.result_window.geometry('400x300')
        self.result_window.resizable(False,False)
        self.result_window.overrideredirect(True)
        self.result_window.eval('tk::PlaceWindow . center')
        self.result_window.configure(bg=self.color3)

        title_bar = Frame(self.result_window, bg=self.color3, relief="raised", bd=2)

        # create title label
        title_label = Label(title_bar, text=self.name, bg=self.color3, fg=self.color5, font=('Arial', 15))
        title_label.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        def close_result_window():
            self.isResultDisplayed = False
            self.result_window.destroy()
        close_button = Button(title_bar, text=" X ",font=('Arial',8, 'bold'), command=close_result_window,bg=self.color5)
        close_button.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        title_bar.columnconfigure(0, weight=5)
        title_bar.columnconfigure(0, weight=1)
        title_bar.pack(fill=X, padx=0)
        

        # title function
        def get_title_click(event):
            global title_click_x, title_click_y
            title_click_x = event.x_root
            title_click_y = event.y_root

        def move_window(event):
            global title_click_x, title_click_y
            new_pos_x = self.result_window.winfo_x() + (event.x_root - title_click_x)
            new_pos_y = self.result_window.winfo_y() + (event.y_root - title_click_y)
            self.result_window.geometry(f'+{new_pos_x}+{new_pos_y}')
            title_click_x = event.x_root
            title_click_y = event.y_root
        
        title_bar.bind('<Button-1>',get_title_click)
        title_bar.bind('<B1-Motion>',move_window)        
        title_label.bind('<Button-1>',get_title_click)
        title_label.bind('<B1-Motion>',move_window)

        def save_to_file():
            df = pd.DataFrame({"name":self.username, "height":self.height, "weight":self.weight, "bmi":self.bmi, "timestamp": pd.Timestamp.now()}, index=[0])
            df.to_csv("data.csv", mode="a", header=False, index=False)
            self.isResultDisplayed = False
            self.result_window.destroy()

        # create result label
        self.result_label = Label(self.result_window,text='Result',font=('Arial',20,'bold'), bg=self.color3, fg=self.color5)
        self.result_label.pack(pady=10)
        # create type label
        self.type_label = Label(self.result_window,text=f'Type: {self.type}',font=('Arial',15), bg=self.color3, fg=self.color5)
        self.type_label.pack(pady=10)
        # create result frame
        self.result_frame = Frame(self.result_window,padx=10,pady=10,bg=self.color3)
        self.result_frame.pack()
        # create result
        self.bmi_label = Label(self.result_frame,text=f'BMI: {self.bmi:.2f}',font=('Arial',15), bg=self.color3, fg=self.color5)
        self.bmi_label.grid(row=0,column=0,padx=10,pady=10)
        # create save button
        self.save_button = Button(self.result_frame,text='Save',font=('Arial',15), command=save_to_file, background=self.color5)
        self.save_button.grid(row=1,column=0,padx=10,pady=10,sticky='we')

        self.save_button.bind('<Enter>',on_btn_hover)
        self.save_button.bind('<Leave>',on_btn_leave)

    def mainloop(self):
        self.window.mainloop()