# Haar Cascade ile Yüz Tespiti

Bu proje, OpenCV kütüphanesi kullanılarak geliştirilmiş bir gerçek zamanlı yüz algılama uygulamasıdır.
Bu projede webcam aracılığıyla ortamda bulunan insan yüzlerini gerçek zamanlı tespiti yapan Python betiği bulunmaktadar.

## Haar Cascade Algoritması 
Haar Cascade sınıflandırıcıları, nesne tespiti için makine öğrenimi tabanlı bir yöntemdir. Bir
sınıflandırıcıyı eğitmek için bir dizi pozitif ve negatif görüntü kullanırlar, daha sonra bu
sınıflandırıcı yeni görüntülerdeki nesneleri tespit etmek için kullanılır.

**Temel Mantık:**
- Yüz algılama işlemi için, OpenCV'nin varsayılan olarak sunduğu model olan haarcascade_frontalface_default.xml dosyası dahil edilir.
- Bilgisayar kamerası webcam ile canlı görüntü alınır.
- Her bir görüntü frame yüz tespiti için alınır.
- Bu frame gri tona çevrilir. adjusted_detect_face fonksiyonundaki hazır olarak dahil ettiğimiz Haar Cascades sınıflandırıcısı ile yüz tespiti yapılır. 
- Tespit edilen yüzlerin etrafına beyaz renkte dikdörtgen çizilir.
- Görüntü anlık olarak ekranda gösterilir.
- `q` tuşuna basıldığında uygulama sonlandırılır.

**Avantajları:**
-	Çok hızlı, gerçek zamanlı çalışabilme yeteneğine sahip
-	Düşük hesaplama gereksinimleri sayesinde kaynağı kısıtlı sistemlerde çok büyük avantaj sağlar
-	Model boyutları genelde küçüktür


**Dezavantajları:**
- Yanlış tespitlere oldukça yatkındır.
- Açı, ışık, karmaşık arkaplanda doğruluğu düşüktür.
- detectMultiScale() fonksiyonunda hangi değerleri vereceği dikkatli seçilmesi gerekir.
- Yeni nesil HOG + SVM gibi yöntemlere göre hassasiyeti düşüktür.

## Yüz Tespiti Uygulaması
Aşağıda Python kodu ve açıklamaları yer almaktadır.
```python
import cv2  # OpenCV kütüphanesini içe aktar

# Görüntüdeki yüzleri tespit edip dikdörtgen çizen fonksiyon
def adjusted_detect_face(img, face_cascade):
    face_img = img.copy()  # Orijinal görüntüyü kopyala
    gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY) # görüntüyü gri tona çevirir
    face_rect = face_cascade.detectMultiScale(  # Yüzleri tespit et
        gray, 
        scaleFactor=1.2,  # Görüntü boyutunu küçültme oranı
        minNeighbors=5    # Algılamayı hassaslaştıran parametre
    )
    for (x, y, w, h) in face_rect:  # Her yüz için dikdörtgen çiz
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 255, 255), 10)
        
    return face_img  # Yüz çerçeveli görüntüyü döndür


# Yüz algılama sınıfı

class FaceDetection:
    
    def __init__(self):
        # Haar Cascade sınıflandırıcısını yükle
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        
    def main(self):
        cap = cv2.VideoCapture(0)  # Bilgisayar kamerasını başlat

        if not cap.isOpened():  # Kamera açılamazsa hata ver
            print("webcam açılmıyor ")
            exit()
        
        while True:
            ret, frame = cap.read()  # Kameradan bir kare oku
            
            if not ret:  # Görüntü alınamazsa döngüden çık
                print("görüntü okunamadı")
                break
            
            # Karedeki yüzleri algıla ve çiz
            face_img = adjusted_detect_face(frame, self.face_cascade)
            
            # Görüntüyü pencereye yazdır
            cv2.imshow('Face Detection', face_img)
        
            # 'q' tuşuna basılırsa çık
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
        cap.release()  # Kamerayı serbest bırak
        cv2.destroyAllWindows()  # Tüm OpenCV pencerelerini kapat

    
# Program Çalıştırıldığında burası çalışır
if __name__ == '__main__':
    proses = FaceDetection() # sınıfı değişkene atar
    proses.main() # sınıfın içindeki main metodunu çalıştırır

```
## Parametre Detayları
### 1. `scaleFactor`
- Küçük değerler daha hassas çalışmasını sağlar daha doğru çalışır ancak daha yavaş çalışır
- Büyük değerler küçük detayları algılayamaz ancak daha hızlı çalışır

### 2. `minNeighbors`
- düşük değerler daha fazla yüz tespiti yapar ama bazen gereksiz yerleri de yüz olarak algılayabilir
- yüksek değerler daha az yüz tespiti yapar her detayı algılamayabilir

## Etkileyen Faktörler
- Görüntü boyutunun küçük olması daha hızlı işlem yaptırır ancak doğruluğu düşer yüksek boyutta ise durum tam tersidir
- İyi aydınlatılmış net görüntülerde daha doğru algılama sağlanır bunun için görüntüye aydınlatma işlemleri yapılabilir

## Sonuç
Bu proje, OpenCV'nin Haar Cascade algoritmasıyla gerçek zamanlı yüz tespitinin nasıl gerçekleştirileceğini göstermektedir. scaleFactor ve minNeighbors gibi parametrelerin doğru seçilmesi, algılamanın doğruluğunu ve hızını doğrudan etkilemektedir.
Bu proje başlangıç seviyesi olarak ve konuyu temel olarak öğrenebilme açısından iyidir fakat daha gelişmiş yöntemlerle daha gelişmiş projeler yapılabilir.




