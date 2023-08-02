scp nvidia@172.30.153.250:/home/nvidia/Downloads/OpenCV.zip .

scp nvidia@172.30.153.250:/home/nvidia/Downloads/add.zip .

# hybus JetbotEx

sudo sh -c 'echo 200 > /sys/devices/pwm-fan/target_pwm'

cp  ~/AILearningJetbot/Basic_Install/Adafruit_MotorHAT/*.py ~/.local/lib/python3.6/site-packages/Adafruit_MotorHAT/

Adafruit_MotorHAT_Motors.py

Adafruit_PWM_Servo_Driver.py 

cd

mv AILearningJetbot _AILearningJetbot

git clone -b hibusJetbot --single-branch https://github.com/jetsonai/AILearningJetbot

모터 동작 확인

jtop

스왑을 먼저해야함.

To Check
python3

import torch

import torchvision

git clone https://github.com/JetsonHacksNano/installSwapfile

cd installSwapfile

./installSwapfile.sh

sudo reboot

리부팅 후 jtop 으로 스왑 상태 확인해주세요.

----------------------

# StartJetbot

# 1. 젯봇 소개

https://www.waveshare.com/product/robotics/jetbot-ai-kit-acce.htm

https://jetsonaicar.tistory.com/21

# 2. 젯봇 설치 

3.1 OR 3.2 중 택 1

# 3.1 젯봇 이미지 설치

3_1_InstallJetBotImage.txt

# 3.2 젯팩에서 설치

3_2_Jetpack2Jetbot.txt


# 4 부팅 후 기본 세팅

power모드 1.5W로 변경

무선환경이라면 wifi 세팅

system setting

절전 모드 해제


# 5. 주피터 노트북 예제 시작

종이컵 2개 위에 올리기

브라우저에서 localhost:8888 로 접속
혹은 ip 확인 후 pc에서 접속

basic_motion 테스트
-> 다 마친 후 restart Kernel and Clear All Outputs 메뉴 선택

data_collection
