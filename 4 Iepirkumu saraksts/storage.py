# Importē json bibliotēku
# JSON ir datu formāts, kurā saglabāsim iepirkumu sarakstu
import json

# Norāda faila nosaukumu, kur glabāsies dati
FILE_NAME = "shopping.json"


# -----------------------------------------
# Funkcija kas ielādē sarakstu no JSON faila
# -----------------------------------------
def load_list():
    """
    Nolasa datus no JSON faila un atgriež Python sarakstu.
    """

    try:
        # Atver failu lasīšanas režīmā ("r")
        with open(FILE_NAME, "r", encoding="utf-8") as file:

            # json.load pārvērš JSON tekstu Python objektā
            data = json.load(file)

            # Atgriež ielādētos datus
            return data

    except FileNotFoundError:
        # Ja fails neeksistē, atgriež tukšu sarakstu
        return []

    except json.JSONDecodeError:
        # Ja fails ir bojāts vai tukšs
        return []


# -----------------------------------------
# Funkcija kas saglabā sarakstu JSON failā
# -----------------------------------------
def save_list(items):
    """
    Saglabā produktu sarakstu JSON failā.
    """

    # Atver failu rakstīšanas režīmā ("w")
    with open(FILE_NAME, "w", encoding="utf-8") as file:

        # json.dump saglabā Python objektu JSON formātā
        json.dump(
            items,      # dati
            file,       # fails
            indent=4,   # skaists formatējums
            ensure_ascii=False
        )   