#include <Servo.h>
#include <WiFiNINA.h>

// WiFi 설정
char ssid[] = "WIFI ID";
char password[] = "PASSWORD";
int status = WL_IDLE_STATUS;
WiFiServer server(80);

// 서보모터 핀 설정
const int servoPin = 9;
Servo servo;

void setup()
{
  // 시리얼 통신 초기화
  Serial.begin(9600);

  // WiFi 연결
  while (status != WL_CONNECTED)
  {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid, password);
    delay(5000);
  }
  server.begin();

  // 서보모터 핀 설정
  servo.attach(servoPin);
  servo.write(0);  // 초기 위치 (0도)
}

void loop()
{
  WiFiClient client = server.available();
  if (client)
  {
    String request = client.readStringUntil('\r');
    client.flush();

    if (request.indexOf("/servo?action=rotate") != -1)
    {
      // "/servo?action=rotate" 엔드포인트에 대한 요청 수신
      rotateServo();
    }

    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/html");
    client.println();
    client.println("<h1>Arduino Uno WiFi Rev2</h1>");
    client.println("<p>Servo Motor Control</p>");
    //client.stop();
  }
}

void rotateServo()
{
  // 서보모터 작동
  for (int angle = 0; angle <= 180; angle += 10)
  {
    servo.write(angle);
    delay(15);
  }

  delay(10000);

  // 서보모터 초기 위치로 이동
  for (int angle = 180; angle >= 0; angle -= 10)
  {
    servo.write(angle);
    delay(15);
  }
}
