import cv2


def adjusted_detect_face(img, face_cascade):
    face_img = img.copy()
    face_rect = face_cascade.detectMultiScale(face_img, 
                                              scaleFactor=1.2, 
                                              minNeighbors=5)
    for (x, y, w, h) in face_rect:
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 255, 255), 10)
        
    return face_img



class FaceDetection:
    
    def __init__(self):
        self.face_cascade =  cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
    
    def main(self):
        cap = cv2.VideoCapture(0) 

        if not cap.isOpened():
            print("webcam açılmıyor ")
            exit()
        
        while True:
            ret, frame = cap.read()
            
            if not ret:
                print("görüntü okunamadı")
                break
            
            face_img = adjusted_detect_face(frame, self.face_cascade)
            
            cv2.imshow('Face Detection', face_img)
        
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
        cap.release()
        cv2.destroyAllWindows()

    
if __name__ == '__main__':
    proses = FaceDetection()
    proses.main()
    
    
        
