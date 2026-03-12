# importējam tkinter bibliotēku grafiskajai lietotnei
# tkinter ir Python standarta bibliotēka logu (GUI) veidošanai
import tkinter as tk

# izveidojam galveno programmas logu
root = tk.Tk()

# iestatām loga virsrakstu (tas parādās loga augšējā joslā)
root.title("Skaitītājs")

# izveidojam mainīgo, kas glabās skaitītāja vērtību
# IntVar ir īpašs tkinter mainīgais, kas var automātiski atjaunināt GUI elementus
# value=0 nozīmē, ka sākuma vērtība būs 0
counter_var = tk.IntVar(value=0)


# funkcija, kas palielina skaitītāju par 1
def increment():
    # get() paņem pašreizējo skaitītāja vērtību
    current = counter_var.get()

    # set() iestata jaunu vērtību
    # šeit mēs pieskaitām 1
    counter_var.set(current + 1)


# funkcija, kas samazina skaitītāju par 1
def decrement():
    # paņemam pašreizējo vērtību
    current = counter_var.get()

    # pārbaudām vai vērtība ir lielāka par 0
    # tas neļauj skaitītājam kļūt negatīvam
    if current > 0:
        # ja nosacījums izpildās, samazinām par 1
        counter_var.set(current - 1)


# funkcija, kas atiestata skaitītāju uz 0
def reset():
    # vienkārši iestata vērtību atpakaļ uz 0
    counter_var.set(0)


# izveidojam Label elementu (teksta lauku)
# root nozīmē, ka tas atradīsies galvenajā logā
# textvariable=counter_var nozīmē:
# label teksts vienmēr būs vienāds ar counter_var vērtību
# kad counter_var mainās, label automātiski atjaunojas
# font nosaka teksta fontu un izmēru (ļoti liels skaitītājs)
label = tk.Label(root, textvariable=counter_var, font=("Arial", 48))

# novietojam label logā ar grid izkārtojumu
# row=0 nozīmē pirmā rinda
# column=0 nozīmē pirmā kolonna
# columnspan=3 nozīmē ka label aizņem 3 kolonnas
# pady=20 pievieno vertikālu atstarpi
label.grid(row=0, column=0, columnspan=3, pady=20)


# izveidojam pogu "−"
# text="−" ir pogas teksts
# command=decrement nozīmē, ka nospiežot pogu izsauksies decrement funkcija
# width=8 nosaka pogas platumu
minus_button = tk.Button(root, text="−", command=decrement, width=8)

# novietojam pogu grid izkārtojumā
# row=1 nozīmē otrā rinda
# column=0 nozīmē pirmā kolonnau
# padx=5 pievieno horizontālu atstarpi
minus_button.grid(row=1, column=0, padx=5)


# izveidojam Reset pogu
reset_button = tk.Button(root, text="Reset", command=reset, width=8)

# novietojam pogu vidējā kolonnā
reset_button.grid(row=1, column=1, padx=5)


# izveidojam pogu "+"
plus_button = tk.Button(root, text="+", command=increment, width=8)

# novietojam pogu trešajā kolonnā
plus_button.grid(row=1, column=2, padx=5)


# mainloop() palaiž programmas galveno ciklu
# tas uztur logu atvērtu un gaida lietotāja darbības (piemēram pogu nospiešanu)
root.mainloop()  