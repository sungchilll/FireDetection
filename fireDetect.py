from ultralytics import YOLO
import time
import requests

# 모델 설정
model = YOLO('fireSmoke.pt')

# 아두이노와 통신하기 위한 설정
arduino_ip = "192.168.37.7"  # 아두이노의 IP 주소
arduino_port = 80  # 아두이노와 통신하는 포트

# 서보모터 동작을 제어하는 API 엔드포인트
api_endpoint = f"http://{arduino_ip}:{arduino_port}/servo"

# 아두이노로 신호 전송하는 함수
def send_signal():
    try:
        requests.get(f"http://{arduino_ip}:{arduino_port}/signal")  # 아두이노로 GET 요청 전송
    except requests.exceptions.RequestException as e:
        print(e)

# 객체 인식 및 타이머 설정
object_detected = False
start_time = time.time()
duration = 5  # 종료 타이머 시간 (초)

# 모델 웹캠에 적용
results = model(source=0, stream=True, show=True)  
for r in results:
    count = 0
    boxes = r.boxes  # Boxes object for bbox outputs
    masks = r.masks  # Masks object for segment masks outputs
    probs = r.probs  # Class probabilities for classification outputs
    
    # 객체 인식 박스의 개수
    objects = len(boxes.xyxy)

    # 객체의 개수가 1개 이상이라면 object_detected = True
    if objects > 0:
        object_detected = True
        # 객체 인식 시간 재기
        elapsed_time = time.time() - start_time
        # 객체 인식 OK and 객체 인식 시간 5초 이상이면
        if object_detected and elapsed_time >= duration:
            response = requests.get(api_endpoint, params={'action':'rotate'})
            if response.status_code == 200:
                print("서보모터 작동 완료")
                break
            else:
                print("서보모터 작동 실패")
            break
            
    # 아니면 object_detected = False, 시간 초기화
    else: 
        object_detected = False
        start_time = time.time()

    
