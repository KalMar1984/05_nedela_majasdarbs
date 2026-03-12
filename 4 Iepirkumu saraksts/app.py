# Importē tkinter bibliotēku grafiskā interfeisa veidošanai
# tkinter ir iebūvēta Python bibliotēka logu programmām
import tkinter as tk

# Importē messagebox moduļus, lai varētu parādīt paziņojumu logus
# piemēram: kļūda, informācija, brīdinājums
from tkinter import messagebox

# Importē funkcijas no storage.py faila
# load_list() -> ielādē sarakstu no JSON faila
# save_list() -> saglabā sarakstu JSON failā
from storage import load_list, save_list

# Importē palīgfunkcijas no utils.py
# calc_line_total() -> aprēķina vienas rindas cenu
# calc_grand_total() -> aprēķina kopējo cenu
# count_units() -> saskaita kopējo vienību skaitu
from utils import calc_line_total, calc_grand_total, count_units


# -----------------------------------------
# Funkcija kas atjauno Listbox saturu
# -----------------------------------------
def refresh_listbox():
    """Atjauno Listbox saturu no items saraksta."""

    # Notīra Listbox visus elementus
    # 0 nozīmē pirmo elementu
    # tk.END nozīmē pēdējo elementu
    listbox.delete(0, tk.END)

    # Iet cauri visiem produktiem sarakstā "items"
    for item in items:

        # Aprēķina kopējo cenu šai rindai
        # piemēram: 3 × 1.20 = 3.60
        line_total = calc_line_total(item)

        # Ievieto tekstu Listbox sarakstā
        # tk.END nozīmē pievienot saraksta beigās
        listbox.insert(
            tk.END,

            # f-string ļauj ievietot mainīgos tekstā
            f"{item['name']} × {item['qty']}  —  "
            f"{item['price']:.2f} EUR  —  {line_total:.2f} EUR"
        )

    # Pēc saraksta atjaunošanas pārrēķina kopsummu
    update_total()


# -----------------------------------------
# Funkcija kas aprēķina kopējo summu
# -----------------------------------------
def update_total():
    """Aprēķina un parāda kopējo cenu."""

    # Aprēķina kopējo cenu visiem produktiem
    total = calc_grand_total(items)

    # Saskaita cik vienību kopā ir sarakstā
    units = count_units(items)

    # Maina label tekstu
    total_label.config(
        text=f"Kopā: {total:.2f} EUR ({units} vienības)"
    )


# -----------------------------------------
# Funkcija kas pievieno jaunu produktu
# -----------------------------------------
def add_item():
    """Nolasa datus no Entry laukiem un pievieno sarakstam."""

    # Nolasa produkta nosaukumu no ievades lauka
    # strip() noņem liekās atstarpes
    name = name_entry.get().strip()

    # Nolasa daudzuma tekstu
    qty_text = qty_entry.get()

    # Nolasa cenu tekstu
    price_text = price_entry.get()

    # ---------------------------------
    # VALIDĀCIJA
    # ---------------------------------

    # Ja nosaukums ir tukšs
    if not name:
        messagebox.showerror(
            "Kļūda",
            "Produkta nosaukums nedrīkst būt tukšs"
        )
        return

    # Pārbauda vai daudzums ir skaitlis
    try:
        qty = int(qty_text)
    except:
        messagebox.showerror(
            "Kļūda",
            "Daudzumam jābūt veselam skaitlim"
        )
        return

    # Pārbauda vai cena ir skaitlis
    try:
        price = float(price_text)
    except:
        messagebox.showerror(
            "Kļūda",
            "Cenai jābūt skaitlim"
        )
        return

    # ---------------------------------
    # PIEVIENO PRODUKTU
    # ---------------------------------

    # Izveido jaunu produkta objektu (dictionary)
    item = {
        "name": name,
        "qty": qty,
        "price": price
    }

    # Pievieno produktu sarakstam
    items.append(item)

    # Saglabā JSON failā
    save_list(items)

    # Atjauno sarakstu ekrānā
    refresh_listbox()

    # ---------------------------------
    # IZTĪRA IEVADES LAUKUS
    # ---------------------------------

    name_entry.delete(0, tk.END)
    qty_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)


# -----------------------------------------
# Funkcija kas dzēš izvēlēto elementu
# -----------------------------------------
def delete_selected():
    """Dzēš izvēlēto produktu."""

    # Nosaka kurš saraksta elements ir izvēlēts
    selection = listbox.curselection()

    # Ja nekas nav izvēlēts
    if not selection:
        messagebox.showinfo(
            "Info",
            "Izvēlies produktu, ko dzēst"
        )
        return

    # Paņem izvēlētā elementa indeksu
    index = selection[0]

    # Izņem elementu no saraksta
    items.pop(index)

    # Saglabā izmaiņas JSON
    save_list(items)

    # Atjauno sarakstu
    refresh_listbox()


# -----------------------------------------
# GALVENĀ PROGRAMMAS DAĻA
# -----------------------------------------

# Ielādē produktus no JSON faila
items = load_list()


# Izveido galveno programmas logu
root = tk.Tk()

# Uzstāda loga virsrakstu
root.title("Iepirkumu saraksts")


# -----------------------------------------
# PRODUKTA NOSAUKUMA LAUKS
# -----------------------------------------

# Teksts "Produkts:"
name_label = tk.Label(root, text="Produkts:")
name_label.grid(row=0, column=0)

# Ievades lauks produkta nosaukumam
name_entry = tk.Entry(root, width=20)
name_entry.grid(row=0, column=1)


# -----------------------------------------
# DAUDZUMA LAUKS
# -----------------------------------------

qty_label = tk.Label(root, text="Daudzums:")
qty_label.grid(row=1, column=0)

qty_entry = tk.Entry(root, width=5)
qty_entry.grid(row=1, column=1)


# -----------------------------------------
# CENAS LAUKS
# -----------------------------------------

price_label = tk.Label(root, text="Cena:")
price_label.grid(row=1, column=2)

price_entry = tk.Entry(root, width=10)
price_entry.grid(row=1, column=3)


# -----------------------------------------
# PIEVIENOŠANAS POGA
# -----------------------------------------

# Poga kas izsauc add_item funkciju
add_button = tk.Button(
    root,
    text="Pievienot",
    command=add_item
)

add_button.grid(row=2, column=0, columnspan=4, pady=10)


# -----------------------------------------
# SARAKSTA LOGS (LISTBOX)
# -----------------------------------------

listbox = tk.Listbox(root, width=50)
listbox.grid(row=3, column=0, columnspan=4)


# -----------------------------------------
# DZĒŠANAS POGA
# -----------------------------------------

delete_button = tk.Button(
    root,
    text="Dzēst izvēlēto",
    command=delete_selected
)

delete_button.grid(row=4, column=0, columnspan=4, pady=10)


# -----------------------------------------
# KOPSUMMAS LABEL
# -----------------------------------------

total_label = tk.Label(root, text="Kopā: 0 EUR")
total_label.grid(row=5, column=0, columnspan=4)


# -----------------------------------------
# ATJAUNO SARAKSTU STARTĀ
# -----------------------------------------

# Kad programma startējas, ielādē produktus
refresh_listbox()


# -----------------------------------------
# PROGRAMMAS CIKLS
# -----------------------------------------

# mainloop() uztur logu aktīvu
# programma strādā līdz logs tiek aizvērts
root.mainloop()  