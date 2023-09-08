import mysql.connector

# Ühendus andmebaasiga
connection = mysql.connector.connect(
    host="localhost",
    user="kasutaja",
    password="parool",
    database="palgakalkulaator"
)

cursor = connection.cursor()

# Funktsioon uue palga lisamiseks andmebaasi
def lisa_palk(nimi, amet, palk):
    sql = "INSERT INTO palk (nimi, amet, palk) VALUES (%s, %s, %s)"
    val = (nimi, amet, palk)
    cursor.execute(sql, val)
    connection.commit()

# Rakenduse põhiosa
if __name__ == "__main__":
    print("Tere tulemast palgakalkulaatorisse!")
    while True:
        valik = input("Kas soovite lisada uut palka (lisa) või kalkuleerida palkade summat (kalkuleeri)? ")
        if valik == "lisa":
            nimi = input("Sisestage töötaja nimi: ")
            amet = input("Sisestage töötaja amet: ")
            palk = float(input("Sisestage töötaja palk: "))
            lisa_palk(nimi, amet, palk)
            print(f"{nimi} palk on lisatud andmebaasi.")
        elif valik == "kalkuleeri":
            cursor.execute("SELECT SUM(palk) FROM palk")
            summa = cursor.fetchone()[0]
            print(f"Palkade summa on: {summa}")
        else:
            print("Vale valik. Palun sisestage 'lisa' või 'kalkuleeri'.")
