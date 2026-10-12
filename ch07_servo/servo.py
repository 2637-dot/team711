import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

pin = 16

# BOARD 모드 (물리적 16번 핀 사용)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

# PWM 초기화 및 시작을 함수 밖(전역)에서 미리 실행해 둡니다.
servo = GPIO.PWM(pin, 50)
servo.start(0)

def setAngle(angle):
    duty = 2.5 + 10 * angle / 180
    print(f"degree : {angle} to {duty}(duty)")
    servo.ChangeDutyCycle(duty)
    sleep(0.5)
    servo.ChangeDutyCycle(0) # 모터 떨림 방지

def cleanup():
    servo.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    setAngle(0)
    sleep(1)
    setAngle(90)
    sleep(1)
    setAngle(50)
    sleep(1)
    setAngle(120)
    sleep(1)
    setAngle(180)
    sleep(1)

    cleanup()
