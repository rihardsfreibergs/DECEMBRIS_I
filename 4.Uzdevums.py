# veidoju def funkciju priekš faktoriālā skaitļā
def faktorials(skaitlis):
    if skaitlis < 0:
        return "Faktoriāls nav definēts negatīvajiem skaitļiem"
    elif skaitlis == 0 or skaitlis == 1:
        return 1
    else:
        rezultats = 1
        for i in range(2, skaitlis ):
            rezultats *= i
        return rezultats

# Lietotājs ieraksta skaitli
ievade = int(input("Ievadiet skaitli, kura faktoriālu vēlaties aprēķināt: "))

# Izvadu rezultātu
print(f"{ievade}! = {faktorials(ievade)}")
