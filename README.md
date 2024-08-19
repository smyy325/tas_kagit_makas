# Taş, Kağıt, Makas Oyunu

## Hakkında
Bu proje, klasik Taş, Kağıt, Makas oyununun bilgisayara karşı oynanabilir bir versiyonunu sunar. Proje, döngüler, koşullu ifadeler ve kullanıcı girişi gibi temel Python kavramlarını uygulamak amacıyla tasarlanmıştır. Ayrıca, OpenCV ve cvzone kullanılarak el hareketlerini algılayan bir versiyon üzerinde çalışılmaktadır.

## Özellikler
- Kullanıcı ve bilgisayar arasında taş, kağıt, makas oyunu.
- Oyunun birden fazla turdan oluşması ve ilk iki turu kazananın oyunu kazanması.
- Kullanıcıya ve bilgisayara başka bir oyun oynamak isteyip istemediklerinin sorulması.
- Oyun sonuçlarının ekrana yazdırılması.
- El hareketlerini algılamak için OpenCV ve cvzone kullanımı (henüz tam işlevsel değil).

## Kullanılan Teknolojiler
- **Python**: Programlama dili olarak kullanıldı.
- **OpenCV**: Görüntü işleme kütüphanesi.
- **cvzone**: OpenCV için ek özellikler sunan bir kütüphane.

## Mimari
- **Ana Döngü**: Oyun bir `while` döngüsü içerisinde oynanır.
- **Tur Döngüsü**: Her turda oyuncu ve bilgisayarın seçimi alınır, sonuç belirlenir ve galibiyet sayacı güncellenir.
- **Devam Etme İsteği**: Oyun sonunda kullanıcı ve bilgisayarın devam etmek isteyip istemediği kontrol edilir.
- **El Hareketleri Algılama**: OpenCV ve cvzone kullanılarak oyuncunun el hareketleri algılanmaya çalışılmaktadır (henüz tam olarak işlevsel değildir).

## 6. Proje Nasıl Ayağa Kaldırılır
1. [GitHub Depo URL'si] adresinden projeyi klonlayın veya indirin.
2. Python yüklü olduğundan emin olun.
3. OpenCV ve cvzone kütüphanelerini yüklemek için terminalde `pip install opencv-python cvzone` komutunu çalıştırın.
4. Terminal veya komut istemcisinde projeye gidin.
5. `python tas_kagit_makas_ADINIZ_SOYADINIZ.py` komutunu çalıştırarak oyunu başlatın.

![Ekran görüntüsü 2024-08-19 224817](https://github.com/user-attachments/assets/07168fc5-891b-4e14-83e1-62b721349092)
![Ekran görüntüsü 2024-08-19 225612](https://github.com/user-attachments/assets/f385fa27-4bb3-48d8-a372-8bd3cf9f613e)

