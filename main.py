import random

def tas_kagit_makas_Somaya_Arab():

    # Tanıtım

    print("Taş, Kağıt ve Makas oyununa hoş geldin!")
    print("Özet: Taş makası yener, makas kağıdı yener ve kağıt taşı yener.")
    print("İlk iki turu kazanan oyunun kazananı.")

    while True:
        # Kurulumu
        secenekler = ['taş', 'kağıt', 'makas']
        oyuncu = 0
        bilgisayar= 0
        tur_sayisi = 0

        while oyuncu < 2 and bilgisayar < 2:

            print(f"\n{tur_sayisi + 1}. Tur")
            oyuncu_secimi = input("Seçiminizi yapın (taş, kağıt, makas): ").lower()

            while oyuncu_secimi not in secenekler:
                oyuncu_secimi = input("Geçersiz seçim. Lütfen tekrar deneyin (taş, kağıt, makas): ").lower()

            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")


            if oyuncu_secimi == bilgisayar_secimi:
                print("Beraberlik!")
            elif (oyuncu_secimi == 'taş' and bilgisayar_secimi == 'makas') or \
                 (oyuncu_secimi == 'makas' and bilgisayar_secimi == 'kağıt') or \
                 (oyuncu_secimi == 'kağıt' and bilgisayar_secimi == 'taş'):
                print("Bu turu kazandınız!")
                oyuncu += 1
            else:
                print("Bu turu bilgisayar kazandı!")
                bilgisayar += 1

            tur_sayisi += 1


        if oyuncu == 2:
            print("\nTebrikler, oyunu kazandınız!")
        else:
            print("\nMaalesef, bilgisayar oyunu kazandı.")

        # 6. Devam Etme İsteği
        devam_oyuncu = input("Başka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
        devam_bilgisayar = random.choice(['evet', 'hayır'])
        print(f"Bilgisayarın devam isteği: {devam_bilgisayar}")

        if devam_oyuncu == 'hayır' or devam_bilgisayar == 'hayır':
            print("Oyun sona erdi. Teşekkürler!")
            break

# Fonksiyonu çalıştırmak için
tas_kagit_makas_Somaya_Arab()
