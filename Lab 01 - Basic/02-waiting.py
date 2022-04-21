x = int(input("x: "))
y = int(input("y: "))

time = x + y
while time >= 24:
    time = time - 24

print(f"She comes at {time}:00")