import tkinter as tk

def reset():
    entry1.delete(0, tk.END)
    entry1.insert(0, "0.0")
    entry2.delete(0, tk.END)
    entry2.insert(0, "0.0")

def convertidor_a_calsius():
    Fahrenheit=float(entry1.get())
    celsius=(Fahrenheit-32)*5.0/9.0
    entry2.delete(0,tk.END)
    entry2.insert(0,f"{celsius:.2f}")
    
def convertir_a_fahrenheit():
    celsius=float(entry2.get())
    Fahrenheit=(celsius*9/5)+32
    entry1.delete(0,tk.END)
    entry1.insert(0,f"{Fahrenheit:.2f}")
        
        
    
    #ventana=tk.Tk()
    #ventana.
    
app = tk.Tk()
app.title("Conversor de Temperatura")

label1 = tk.Label(app, text="Fanhrenheit:")
label1.grid(row=0, column=0)

entry1 = tk.Entry(app)
entry1.grid(row=0, column=1)

button1 = tk.Button(app, text= "Convertir a Celsius", command=convertidor_a_calsius)
button1.grid(row=0, column=2)

label2 = tk.Label(app, text="Celsius:") 
label2.grid(row=1, column=0)

entry2 = tk.Entry(app)
entry2.grid(row=1, column=1)

button2 = tk.Button(app, text= "Convertir a Fahrenheit", command=convertir_a_fahrenheit)
button2.grid(row=1, column=2)

button3= tk.Button(app, text= "Restablecer", command=reset)
button3.grid(row=2, column=1)

app.mainloop()
