from sense_hat import SenseHat

sense = SenseHat()
while True:
    orientation = sense.get_orientation_degrees()
    print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
