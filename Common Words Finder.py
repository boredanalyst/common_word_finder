### Intersection Finder
## This tool finds common words between two texts.

## Importing stuff

import tkinter as tk
import customtkinter as ctk

## Creating the functions.

def compare():
    ## This function stores the text in textbox A into a set.
    setA = set()
    txtA = txt_seta.get("1.0","end")
    txtA = txtA.replace('.','').replace(',','')
    txtA = txtA.upper()
    txtA = txtA.split()
    for word in txtA:
        setA.add(word)

    ## This function stores the text in textbox B into a set.
    setB = set()
    txtB = txt_setb.get("1.0","end")
    txtB = txtB.replace('.','').replace(',','')
    txtB = txtB.upper()
    txtB = txtB.split()
    for word in txtB:
        setB.add(word)

    ## This function takes the contents of setA + setB and identify intersections.

    setC = {}
    setC = setA.intersection(setB)
    output = " ".join(setC)
    output = output.lower()

    lbl_result.configure(text=output)


## Designing the main window

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("500x565")
root.title("Common Words Finder")

## Setting up the header.



lbl_headr = ctk.CTkLabel(root,text="Common Words Finder",font=("Arial",12,"bold"))
lbl_headr.pack()

lbl_subhead = ctk.CTkLabel(root,text="Made with python, tkinter, and customtkinter",font=("Arial",9,"italic"))
lbl_subhead.pack()

## setting up the text input window.

frm_input = ctk.CTkFrame(root)
frm_input.pack(pady=5)

frm_seta = ctk.CTkFrame(frm_input)
frm_seta.grid(row=0,column=0,padx=10,pady=10)

frm_setb = ctk.CTkFrame(frm_input)
frm_setb.grid(row=0,column=1,padx=10,pady=10)

## setting up setA

lbl_seta = ctk.CTkLabel(frm_seta,text="Provide your first string of text.",font=("Arial",10))
lbl_seta.pack()

txt_seta = ctk.CTkTextbox(frm_seta)
txt_seta.pack()

## setting up setB

lbl_setb = ctk.CTkLabel(frm_setb,text="Please provide your second string of text",font=("Arial",10))
lbl_setb.pack()

txt_setb = ctk.CTkTextbox(frm_setb)
txt_setb.pack()

## Setting up output set.

frm_output = ctk.CTkFrame(root)
frm_output.pack()

btn_compare = ctk.CTkButton(frm_output,text="Compare",width=430,command=compare)
btn_compare.pack(pady=3,padx=5)

lbl_result = ctk.CTkLabel(frm_output,
                          wraplength=300,
                          text="Output will be displayed here.",
                          font=("Arial",10),
                          height=190,
                          justify="left")
lbl_result.pack(pady=5)



root.mainloop()

