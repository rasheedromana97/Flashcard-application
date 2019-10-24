from tkinter import *
import os
import csv
os.system('clear')

def get_length(file_path):
    with open("flashcard_db.csv","r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)

file_path = "flashcard_db.csv"

def append_data():
    next_id = get_length(file_path)
    fieldnames = ["id","information"]
    with open(file_path,"a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            "id": next_id,
            "information": myTextbox.get(),
        })

root = Tk()
root.title('Flash Cards: Revise for perfection')
root.geometry("400x600")

myLabel = Label(root, text = "Topic")
myLabel.pack()

myTextbox = Entry(root, width=30)
myTextbox.pack()

myButton = Button(root, text="Submit", command=append_data)
myButton.pack()

root.mainloop()
