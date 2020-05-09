from gpiozero import Button
from picamera import PiCamera
from signal import pause
global order
button = Button(17)
camera = PiCamera()
camera.resolution = (4056, 3040)
camera.start_preview(alpha=128)
order = 0

def capture():
    global order
    order = order + 1

    camera.capture('/home/pi/%s.jpg' % order)

button.when_pressed = capture

pause()