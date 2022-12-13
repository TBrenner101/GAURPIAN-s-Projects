from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

pir = MotionSensor(4)
camera = PiCamera()

while True:
    
    pir.wait_for_motion()

    if pir.motion_detected:
        camera.start_preview()
        camera.start_recording('/home/group5/Desktop/video.h264')
        sleep(10)
        camera.stop_recording()
        camera.stop_preview()