import random

def mängija_arvud(sisend, miinimum_arv, maksimum_arv):
    while True:
        try:
            väärtus = int(input(sisend))
            if miinimum_arv <= väärtus <= maksimum_arv:
                return väärtus
            print("Sisestatud arv peab olema vahemikus", miinimum_arv, "-", maksimum_arv)
        except ValueError:
            print("Sisesta korrektne arv.")

def bingo(mänguvälja_suurus, tabeli_suurus):
    arv = []
    for i in range(1, tabeli_suurus + 1):
        for j in range(1, tabeli_suurus + 1):
            bingo_tulemus = i * j
            if bingo_tulemus != 13 and bingo_tulemus not in arv:
                arv.append(bingo_tulemus)
    if len(arv) < mänguvälja_suurus * mänguvälja_suurus:
        raise ValueError("Korrutustabel on liiga väike, et luua " + str(mänguvälja_suurus) + "x" + str(mänguvälja_suurus) + " väljak.")
    mängijate_arv = random.sample(arv, mänguvälja_suurus * mänguvälja_suurus)
    mänguväli = [mängijate_arv[i:i + mänguvälja_suurus] for i in range(0, len(mängijate_arv), mänguvälja_suurus)]
    return mänguväli

def fail_bingo(bingod, failinimi="bingo.txt"):
    with open(failinimi, "w", encoding="utf-8") as fail:
        for tulemus, bingo in enumerate(bingod, start=1):
            fail.write(str(tulemus) + ". mänguväli\n")
            for rida in bingo:
                fail.write(" ".join(str(num).rjust(3) for num in rida) + "\n")
            fail.write("\n")

def bingo_arvud():
    mänguvälja_suurus = mängija_arvud("Sisestage mänguväljaku suurus: ", 1, 20)
    tabeli_suurus = mängija_arvud("Sisestage korrutustabeli suurus: ", 1, 20)
    mängijate_arv = mängija_arvud("Sisestage mängijate arv: ", 1, 10)
    if tabeli_suurus < mänguvälja_suurus:
        print("Viga: korrutustabel peab olema vähemalt sama suur kui mänguväli.")
        return
    try:
        väljad = []
        for _ in range(mängijate_arv):
            väljad.append(bingo(mänguvälja_suurus, tabeli_suurus))
    except ValueError as e:
        print("Viga:", e)
        return

    fail_bingo(väljad)
    print("Mänguväljad on salvestatud faili 'bingo.txt'.")

bingo_arvud()
