import pygame
import random
import sys

# Initsialiseeri Pygame
pygame.init()

# Ekraani seaded
EKRAAN_laius = 1500
EKRAAN_pikkus = 700
EKRAAN = pygame.display.set_mode((EKRAAN_laius, EKRAAN_pikkus))
pygame.display.set_caption("Varjatud sügavus")

taustapilt = pygame.image.load("taust.png")
taustapilt = pygame.transform.scale(taustapilt, (1500, 700))

# Värvid
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fondid
FONT = pygame.font.Font(None, 36)



try:
    mängija_pilt = pygame.image.load("tegelane1.png")
    mängija_pilt = pygame.transform.scale(mängija_pilt, (200,200))
    mängija_pilt = pygame.transform.flip(mängija_pilt, True, False)
except pygame.error as e:
    print(f"Viga pildi laadimisel: {e}")
    sys.exit()

try:
    lima_pilt = pygame.image.load("lima.png")
    lima_pilt = pygame.transform.scale(lima_pilt, (150, 100))
    draakon_pilt = pygame.image.load("draakon.png")
    draakon_pilt = pygame.transform.scale(draakon_pilt, (200, 200))
    koll_pilt = pygame.image.load("koll.png")
    koll_pilt = pygame.transform.scale(koll_pilt, (150, 150))
    koll_pilt = pygame.transform.flip(koll_pilt, True, False)
    haldjas_pilt = pygame.image.load("haldjas.png")
    haldjas_pilt = pygame.transform.scale(haldjas_pilt, (100, 100))
except pygame.error as e:
    print(f"Viga koletise pildi laadimisel: {e}")
    sys.exit()
    

# Mängu andmed
oskuspunktid = 5
esimene_kohtumine = True

# Täringu funktsioon
def veeretamine():
    return random.randint(1, 12)

# Teksti näitamise funktsioon
def kiri(text, color, x, y):
    surface = FONT.render(text, True, color)
    EKRAAN.blit(surface, (x, y))

# Koletise kuvamise funktsioon
def koletise_pilt(koletis, x, y):
    if koletis == "lima":
        EKRAAN.blit(lima_pilt, (x, y))
    elif koletis == "draakon":
        EKRAAN.blit(draakon_pilt, (x, y))
    elif koletis == "koll":
        EKRAAN.blit(koll_pilt, (x, y))
    elif koletis == "haldjas":
        EKRAAN.blit(haldjas_pilt, (x, y))

# Põhifunktsioon
def main():
    global oskuspunktid, esimene_kohtumine
    clock = pygame.time.Clock()
    running = True
    kohtumine_koletisega = True
    mängija_x = 100
    mängija_y = EKRAAN_pikkus // 2

    # Koletised
    koletised = ["lima", "draakon", "haldjas", "koll"]
    
    while running:
        EKRAAN.blit(taustapilt, (0, 0))
        kiri(f"Oskuspunktid: {oskuspunktid}", WHITE, 10, 10)
        EKRAAN.blit(mängija_pilt, (mängija_x, mängija_y))

        # Koletisega kohtumine
        if kohtumine_koletisega:
            if esimene_kohtumine:
                koletis = "lima"
                esimene_kohtumine = False
            else:
                koletis = random.choice(koletised)
            
            koletise_pilt(koletis, EKRAAN_laius // 2+120, EKRAAN_pikkus // 2)
            kiri(f"Sa kohtasid: {koletis}", WHITE, 10, 50)
            kiri("Vali: Rünnak (R) või Sõbrunemine (S)", WHITE, 10, 100)
            pygame.display.flip()
            
            
            valik = None
            while valik not in ["r", "s"]:
                for sündmus in pygame.event.get():
                    if sündmus.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if sündmus.type == pygame.KEYDOWN:
                        if sündmus.key == pygame.K_r:
                            valik = "r"
                        elif sündmus.key == pygame.K_s:
                            valik = "s"
                            
    

            # Täringu veeretamine
            täring_tulemus = veeretamine()
            kiri(f"Sa veeretasid: {täring_tulemus}", WHITE, 10, 150)
            pygame.display.flip()
            pygame.time.wait(2000)
            
            if valik == "s":
                if koletis in ["draakon", "haldjas",]:
                    if täring_tulemus < 12:
                        kiri(f"Sõbrunesid agressiivse koletisega ja surid.", RED, 10, 200)
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        pygame.quit()
                    else:
                        kiri(f"Sõbrunemine õnnestus ja saad +12 oskuspunkti", GREEN, 10, 200)
                        oskuspunktid += 12
                        
                if koletis == "lima" and valik == "s":
                    if täring_tulemus >= 6:
                        kiri(f"Õnnestus! Sa sõbrunesid limaga. Lima: Koll on sõbralik, ning draakon ja haldjas on agressiivsed", GREEN, 10, 200)
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        
                    
                    else:
                        kiri(f"Sõbrunemine ebaõnnestus.", RED, 10, 200)
                        pygame.display.flip()
                        pygame.time.wait(3000)
                        kohtumine_koletisega = True
                        continue
                    
                if koletis == "koll" and valik == "s":
                    if täring_tulemus >= 6:
                        kiri(f"Õnnestus! Sa sõbrunesid kolliga.", GREEN, 10, 200)
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        
                    else:
                        kiri(f"Sõbrunemine ebaõnnestus.", RED, 10, 200)
                        pygame.display.flip()
                        pygame.time.wait(3000)
                        kohtumine_koletisega = True
                        continue

            # Rünnaku loogika
            if valik == "r":
                if täring_tulemus >= 6:
                    kiri(f"Sa tapsid {koletis} ja said +2 oskuspunkti.", GREEN, 10, 200)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    oskuspunktid += 2
                else:
                    kiri("Rünnak ebaõnnestus! Kui palju oskuspunkte soovid lisada?", RED, 10, 200)
                    pygame.display.flip()
                    pygame.time.wait(2000)
        
                    
                    punktide_lisamine = True
                    while punktide_lisamine:
                        for sündmus in pygame.event.get():
                            if sündmus.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if sündmus.type == pygame.KEYDOWN:
                                if sündmus.key == pygame.K_0:
                                    lisatud_punktid = 0
                                    punktide_lisamine = False
                                elif sündmus.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]:
                                    lisatud_punktid = int(chr(sündmus.key))
                                    if lisatud_punktid <= oskuspunktid:
                                        oskuspunktid -= lisatud_punktid
                                        kokku = täring_tulemus + lisatud_punktid
                                        if kokku >= 6:
                                            kiri(f"Sa tapsid {koletis}, aga ei saanud lisapunkte.", GREEN, 10, 250)
                                            pygame.display.flip()
                                            pygame.time.wait(2000)
                                        else:
                                            kiri("Rünnak ebaõnnestus ja sa surid.", RED, 10, 250)
                                            pygame.display.flip()
                                            pygame.time.wait(2000)
                                            running = False
                                        punktide_lisamine = False
                                    else:
                                        kiri("Pole piisavalt oskuspunkte!", RED, 10, 300)
                                        pygame.display.flip()
                                        pygame.time.wait(2000)
                                
             
    
           
           
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
