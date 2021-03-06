import streamlit as st
import csv

labels = ["safe","unsafe","social","educational"]

def update_count(count):
  with open("counter", "w") as f:
    f.truncate()
    f.write(f"{count}")

def write_label(w,label,notes,count):
  with open('labeled-dataset.csv','a') as fd:
    fd.write(f"{w},{label},{notes},{count}\n")

def insert_button(columns,labels,i,label_buttons):
  with columns[i]:
    b = st.button(l)
    label_buttons.append(b)

with open("counter", "r") as f:
  count = int(f.readline())

websites,label_buttons = [],[]

with open('websites.csv', newline='') as csvfile:
  for temp in csv.reader(csvfile):
    websites.append(temp[0])
  websites.append("DONE")

if count<len(websites):
  w = websites[count]
  if w=="DONE":
      st.balloons()
      if st.button("Reset"):
        update_count(1) 
  else:    
    st.markdown(f'## [{w}]({w})')
    columns = st.beta_columns(len(labels))

    for i,l in enumerate(labels):
        insert_button(columns,labels,i,label_buttons)

    notes=st.text_input("notes")

    for i,b in enumerate(label_buttons):
      if b:
        write_label(websites[count-1],labels[i],notes,count-1)
        count += 1
        update_count(count)