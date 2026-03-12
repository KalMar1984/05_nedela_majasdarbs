# Importējam tkinter bibliotēku grafiskajai saskarnei
import tkinter as tk

# Importējam messagebox, lai varētu parādīt kļūdu logu
from tkinter import messagebox


# =====================================================
# KONVERSIJAS KONSTANTES (biznesa loģika – nav GUI)
# =====================================================

# 1 kilometrs = 0.621371 jūdzes
KM_TO_MI = 0.621371

# 1 kilograms = 2.20462 mārciņas
KG_TO_LB = 2.20462

# 1 litrs = 0.264172 galoni
L_TO_GAL = 0.264172


# =====================================================
# KONVERSIJAS FUNKCIJA
# GUI izmanto tikai šo funkciju
# =====================================================

def convert(value, conversion_type):
    """
    Funkcija veic konversiju atkarībā no izvēlētā tipa.
    
    value – skaitlis ko ievadīja lietotājs
    conversion_type – teksts no dropdown izvēlnes
    """

    # Ja izvēlēts km → mi
    if conversion_type == "km → mi":
        return value * KM_TO_MI

    # Ja izvēlēts mi → km
    elif conversion_type == "mi → km":
        return value / KM_TO_MI

    # Ja izvēlēts kg → lb
    elif conversion_type == "kg → lb":
        return value * KG_TO_LB

    # Ja izvēlēts lb → kg
    elif conversion_type == "lb → kg":
        return value / KG_TO_LB

    # Ja izvēlēts L → gal
    elif conversion_type == "L → gal":
        return value * L_TO_GAL

    # Ja izvēlēts gal → L
    elif conversion_type == "gal → L":
        return value / L_TO_GAL


# =====================================================
# FUNKCIJA KAS TIEK IZSAUKTA NOSPIEŽOT POGU
# =====================================================

def on_convert():
    """
    Šī funkcija tiek izsaukta kad lietotājs
    nospiež pogu "Konvertēt".
    """

    try:
        # Mēģinām pārvērst Entry laukā ievadīto tekstu par skaitli
        value = float(entry.get())

    except ValueError:
        # Ja tas nav skaitlis, parādām kļūdas logu
        messagebox.showerror("Kļūda", "Lūdzu ievadi derīgu skaitli")
        return

    # Iegūstam izvēlēto konversijas tipu no dropdown
    conversion_type = selected.get()

    # Izsaucam konversijas funkciju
    result = convert(value, conversion_type)

    # Formatējam rezultātu ar 2 decimālzīmēm
    formatted = f"{result:.2f}"

    # Nosakām vienības ko rādīt pie rezultāta
    if "mi" in conversion_type and "→ mi" in conversion_type:
        unit = "mi"
    elif "km" in conversion_type and "→ km" in conversion_type:
        unit = "km"
    elif "lb" in conversion_type and "→ lb" in conversion_type:
        unit = "lb"
    elif "kg" in conversion_type and "→ kg" in conversion_type:
        unit = "kg"
    elif "gal" in conversion_type and "→ gal" in conversion_type:
        unit = "gal"
    else:
        unit = "L"

    # Parādām rezultātu Label elementā
    result_label.config(text=f"Rezultāts: {formatted} {unit}")


# =====================================================
# GUI IZVEIDE
# =====================================================

# Izveidojam galveno programmas logu
root = tk.Tk()

# Loga nosaukums
root.title("Vienību konvertors")

# Loga izmērs
root.geometry("300x200")


# =====================================================
# KONVERSIJAS IZVĒLNE (Dropdown)
# =====================================================

# Saraksts ar pieejamajām konversijām
options = [
    "km → mi",
    "mi → km",
    "kg → lb",
    "lb → kg",
    "L → gal",
    "gal → L"
]

# StringVar glabā dropdown izvēlēto vērtību
selected = tk.StringVar(value=options[0])

# Teksts virs dropdown
label_type = tk.Label(root, text="Konversijas tips:")
label_type.pack()

# Izveidojam dropdown izvēlni
dropdown = tk.OptionMenu(root, selected, *options)

# Parādām to logā
dropdown.pack(pady=5)


# =====================================================
# ENTRY LAUKS
# =====================================================

# Teksts virs ievades lauka
label_value = tk.Label(root, text="Vērtība:")
label_value.pack()

# Lauks kur lietotājs ievada skaitli
entry = tk.Entry(root)

# Parādām laukumu logā
entry.pack(pady=5)


# =====================================================
# KONVERTĒŠANAS POGA
# =====================================================

# Izveidojam pogu kas izsauc funkciju on_convert
button = tk.Button(root, text="Konvertēt", command=on_convert)

# Parādām pogu
button.pack(pady=10)


# =====================================================
# REZULTĀTA LABEL
# =====================================================

# Teksts kur parādīsies rezultāts
result_label = tk.Label(root, text="Rezultāts:")

# Parādām to logā
result_label.pack()


# =====================================================
# PROGRAMMAS GALVENAIS CIKLS
# =====================================================

# Šī rinda palaiž GUI programmu
# un gaida lietotāja darbības
root.mainloop()  