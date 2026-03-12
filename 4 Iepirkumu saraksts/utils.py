# -----------------------------------------
# Aprēķina vienas rindas cenu
# -----------------------------------------
def calc_line_total(item):
    """
    Aprēķina vienas rindas kopējo cenu.

    item ir dictionary piemēram:
    {
        "name": "Maize",
        "qty": 3,
        "price": 1.20
    }
    """

    # daudzums × cena
    return item["qty"] * item["price"]


# -----------------------------------------
# Aprēķina kopējo cenu visam sarakstam
# -----------------------------------------
def calc_grand_total(items):
    """
    Aprēķina kopējo cenu visiem produktiem.
    """

    # Sākuma summa
    total = 0

    # Iet cauri visiem produktiem
    for item in items:

        # Pieskaita rindas cenu
        total += calc_line_total(item)

    # Atgriež kopējo summu
    return total


# -----------------------------------------
# Saskaita visas vienības
# -----------------------------------------
def count_units(items):
    """
    Saskaita kopējo produktu vienību skaitu.
    """

    # Sākuma skaits
    units = 0

    # Iet cauri visiem produktiem
    for item in items:

        # Pieskaita daudzumu
        units += item["qty"]

    # Atgriež rezultātu
    return units  