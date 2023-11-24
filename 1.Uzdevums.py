#  ievadu skaitli
lietotaja_ievade = int(input("Ievadiet skaitli: "))

# summa
summa = 0

# for cikls, kas skaita no 1 lidz ievadītajam skaitlim
for skaitlis in range(1, lietotaja_ievade + 1):
    summa += skaitlis

# rezultāts
print(f"Summa no 1 līdz {lietotaja_ievade} ir: {summa}")