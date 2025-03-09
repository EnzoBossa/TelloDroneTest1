from djitellopy import tello

length = 20
angle = 90

def flight_routine(drone):

    drone.connect()
    drone.takeoff()

    drone.move_forward(length)
    drone.rotate_clockwise(angle)
    drone.move_forward(length)
    drone.rotate_clockwise(angle)
    drone.move_forward(length)
    drone.rotate_clockwise(angle)
    drone.move_forward(length)
    drone.rotate_clockwise(angle)


    drone.land()

    drone.end()


def main():
    drone = tello.Tello()
    flight_routine(drone)


if __name__ == '__main__':
    main()

