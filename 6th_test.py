#########################################################################
# Date: 2018/10/02
# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 3RD_ASSIGNMENT_CODE
    # Complete the code to perform Third Assignment
    # =======================================================================
    def car_startup(self):
        # implement the assignment code here
        self.car.steering.center_alignment()
        while True:
            self.car.accelerator.go_forward(40)

            distance = self.car.distance_detector.get_distance()

            if distance < 30:
                self.car.steering.turn_left(50)
                self.car.accelerator.go_forward(50)
                time.sleep(1)
                self.car.steering.turn_right(120)
                self.car.accelerator.go_forward(70)
                time.sleep(1)

            if distance > 30 or distance < 0:
                self.car.accelerator.go_forward(50)
                distance = self.car.distance_detector.get_distance()
           
                if self.car.line_detector.read_digital() == [0,0,1,0,0]:
                    self.car.steering.center_alignment()
                    self.car.accelerator.go_forward(50)

                elif self.car.line_detector.read_digital()[1] == 1:
                    if self.car.line_detector.read_digital()[0] == 1:
                        self.car.steering.turn_left(80)
                    elif self.car.line_detector.read_digital()[2] == 1 :
                        self.car.steering.turn_left(85)
                    else:
                        self.car.steering.turn(75)

                elif self.car.line_detector.read_digital()[0] == 1:
                    self.car.steering.turn_right(120)
                    self.car.accelerator.go_backward(50)
                    time.sleep(0.3)
                    self.car.accelerator.stop()
                    self.car.steering.turn(60)
                    self.car.accelerator.go_forward(60)
 
                elif (self.car.line_detector.read_digital() == [0, 0, 0, 1, 1]):
                    self.car.steering.turn_right(100)
                    self.car.accelerator.go_forward(40)

                elif (self.car.line_detector.read_digital() == [0, 0, 0, 0, 1]):
                    self.car.steering.turn_right(120)
                    self.car.accelerator.go_forward(40)

                elif (self.car.line_detector.read_digital() == [0, 0, 0, 0, 0]):
                    self.car.steering.turn_right(120)
                    self.car.accelerator.go_backward(60)
                    time.sleep(0.5)
                    self.car.steering.turn(70)
                    self.car.accelerator.go_forward(60)
                    time.sleep(0.3)

                elif (self.car.line_detector.read_digital() == [1, 1, 1, 1, 1]):
                    self.car.accelerator.stop()
                    break
                time.sleep(0.11)



if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
