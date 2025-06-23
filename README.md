
NE YAPIYOR


Bu proje, OpenCV kütüphanesi kullanılarak geliştirilmiş bir gerçek zamanlı yüz algılama uygulamasıdır.
Bilgisayarın kamerası aracılığıyla ortamda bulunan insan yüzlerini tespit eder ve bu yüzlerin etrafına dikdörtgen çizer.
Tespit edilen görüntü, gerçek zamanlı olarak ekrana yansıtılır.
Projede, OpenCV içerisinde yer alan hazır ve önceden eğitilmiş Haar Cascade sınıflandırıcısı kullanılmıştır.


Uygulamanın Özellikleri

- Yüz algılama işlemi için, OpenCV'nin varsayılan olarak sunduğu model olan haarcascade_frontalface_default.xml dosyası dahil edilir.
- Bilgisayar kamerası webcam ile canlı görüntü alınır.
- Her bir görüntü frame yüz tespiti için alınır.
- Bu frame adjusted_detect_face fonksiyonundaki hazır olarak dahil ettiğimiz Haar Cascades sınıflandırıcısı ile yüz tespiti yapılır. 
- Tespit edilen yüzlerin etrafına beyaz renkte dikdörtgen çizilir.
- Görüntü anlık olarak ekranda gösterilir.
- `q` tuşuna basıldığında uygulama sonlandırılır.

