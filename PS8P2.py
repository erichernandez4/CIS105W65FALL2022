def room(length,width,height):
    room_space  = (2 * length * width) + (2 * length * height) + (2 * width * height)

    return room_space


response = input("DO you want to start this program")
while response == "yes":

    length  = float(input("please enter the length "))
    width = float(input("please enter the width "))
    height = float(input("please enter the height "))
    response = input("DO you want to start this program ")

area_of_room = room(length,width,height)
paint_room = area_of_room / 50
print("number of gallons needed", paint_room)
