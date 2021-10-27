# def bus_rate(age):
#     if age > 65:
#         return 0
#     elif age > 20:
#         return 1200
#     else:
#         return 750
#
# myrate = bus_rate(28)
# print(myrate)

def check_gender(pin):
    if int(pin.split('-')[1][:1]) % 2 == 0:
        print('여성입니다.')
    else:
        print('남성입니다.')

check_gender('940704-2055815')
check_gender('940704-1055815')
