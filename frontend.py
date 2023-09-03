global img
import tkinter
from PIL import ImageTk,Image
import tkinter
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
import tkinter  as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile


def DATASET():
    my_w = tkinter.Tk()
    my_w.geometry("500x300")  # Size of the window
    my_w.title('Dataset')

    my_font1 = ('times', 12, 'bold')
    l1 = tk.Label(my_w, text='Read File & create DataFrame',
                  width=30, font=my_font1)
    l1.grid(row=1, column=1)
    b1 = tk.Button(my_w, text='Browse File',
                   width=20, command=lambda: upload_file())
    b1.grid(row=2, column=1)
    t1 = tk.Text(my_w, width=200, height=200)
    t1.grid(row=3, column=1, padx=5)

    def upload_file():
        f_types = [('CSV files', "*.csv"), ('All', "*.*")]
        file = filedialog.askopenfilename(filetypes=f_types)
        # l1.config(text=file) # display the path
        df = pd.read_csv(file)  # create DataFrame
        # str1="Rows:" + str(df.shape[0])+ "\nColumns:"+str(df.shape[1])
        # print(str1)
        t1.insert(tk.END, df)  # add to Text widget

    my_w.mainloop()  # Keep the window open

def ACCURACYPLOT():
    root =tkinter.Toplevel()
    root.geometry("800x400")
    img= tkinter.PhotoImage(file='BBCSeaborn.png')
    tkinter.Label(root,image=img).pack()

    root.mainloop()


def Accuracy():
    Accuracy = tkinter.Tk()
    Accuracy.title("accuracy")
    Accuracy.geometry('600x300')
    frame1 = tkinter.LabelFrame(Accuracy, text=" \t   Accuracy \t\t", bg='black', fg='White',
                                font=("Calibri", 32, 'bold'))
    frame1.place(height=300, width=600)
    style = ttk.Style(frame1)
    style.theme_use('clam')
    treev = ttk.Treeview(frame1, selectmode='browse')
    treev.pack(fill=tkinter.BOTH, expand=True)
    treev["columns"] = ("1", "2")
    treev['show'] = 'headings'
    treev.column("1", width=150, anchor='c')
    treev.column("2", width=50, anchor='c')
    # treev.column("3", width = 90, anchor ='se')
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Times New Roman", 14, 'bold'))
    treev.heading("1", text="Algorithms")
    treev.heading("2", text="Accuracy")
    # treev.heading("3", text ="Time")

    acc1 = format(ACCXg, ".0f")
    # timer=format(s11,".3f")
    treev.insert("", 'end', text="L1", values=("XG BOOST", acc1))

    acc2 = format(ACCRF, ".0f")
    # format(RF_model.accuracy_score(X_test.astype('float64'),y_test.astype('float64'))*100,".1f")
    # timer2=format(s22,".3f")
    treev.insert("", 'end', text="L2", values=("Random Forest", acc2))

    acc3 = format(ACCKNN, ".0f")
    # timer4=format(s44,".3f")
    treev.insert("", 'end', text="L3", values=("KNN", acc3))

    Accuracy.mainloop()

top = tkinter.Toplevel()
top.title("Parkinson's Disease Prediction")
label=tkinter.Label(top, text ="            Parkinson's Disease Prediction  \t  \t", bg='black', fg="white", font=("Serif", 32, 'bold')).place(x = 0,y = 10)
top.geometry('1000x1000')
img = ImageTk.PhotoImage(file="BBCSeaborn.png")
label1 = tkinter.Label(
    top,
    image=img
)
label1.place(x=0, y=0)
btn0 = tkinter.Button(top, text="DATASET", command=DATASET,bg="white", font=("Serif", 11)).place(x=50, y=300)
btn1 = tkinter.Button(top, text="ACCURACY PLOT",command=ACCURACYPLOT,bg="white", font=("Serif", 11)).place(x=200, y=300)
btn2 = tkinter.Button(top, text="ACCURACY",command=Accuracy,bg="white", font=("Serif", 11)).place(x=400, y=300)
btn3 = tkinter.Button(top, text="PREDICTION",command=Prediction, bg="white", font=("Serif", 11)).place(x=600, y=300)
top.mainloop()