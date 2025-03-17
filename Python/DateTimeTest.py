import time
#prints time in a struct_time format
print(f"Current UTC time: {time.gmtime(0)}")

#create a time struct object
dt = time.struct_time((2025, 3, 12, 11, 43, 00, 2, 71, 1))
print(f"{time.mktime(dt)}")
print(time.gmtime(1741826580.0))

sec = int(input("Seconds: "))
ccsec = time.ctime(sec)
print(ccsec)

timer = int(input("How many seconds: "))
while timer > 0:
    print(".")
    timer = timer - 1
    time.sleep(1)

print("Time's up")