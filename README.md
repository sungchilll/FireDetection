본 코드는 화재 및 연기를 n초 이상 감지 시 소화 모터를 작동 시키는 코드입니다.
객체 인식 모델인 YOLOv8을 사용하여 자체 제작한 약 7000장의 화재 및 연기 데이터셋을 훈련시켜 모델을 제작하였습니다. 
모델의 mAP50은 88.4%, mAP50-95는 61.6%의 정확도를 나타내고 있습니다.
객체 인식 모델을 사용하여 화재 및 연기를 n초 이상 감지 시 같은 네트워크에 연결되어 있는 아두이노 우노 WIFI보드에 http 프로토콜을 사용하여 Servo 모터를 작동 시키는 프로그램을 작성하였습니다.

![val_batch1_pred](https://github.com/sungchilll/FireDetection/assets/91365240/4bc86400-d668-4e8e-8734-cac2f9ec74af)
![val_batch1_labels](https://github.com/sungchilll/FireDetection/assets/91365240/5f8e31f6-4fb8-4c8e-a72b-b885c692330f)

본 코드를 활용하여 "자율 순찰 로봇을 위한 심층학습 기반 화재 감지 시스템 구현" 논문을 작성하여 2023 한국통신학회 하계 종합 학술 발표회에 참가하였습니다.
