import datetime
# iveidoju def funkcijas laika noteikšanai un sveiciena izvadīšanai.
def noteikt_laiku():
    stunda = datetime.datetime.now().hour
    return stunda

def izvadit_sveicienu():
    stunda = noteikt_laiku()
    
    if 6 <= stunda < 12:
        print("Labrīt!")
    elif 12 <= stunda < 18:
        print("Labdien!")
    else:
        print("Labvakar!")

if __name__ == "__main__":
    izvadit_sveicienu()
