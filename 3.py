width = float(input())
length = float(input())
depth = float(input())
volume = width * length * depth
time_seconds = volume * 15
time_minutes = time_seconds / 60
print(f"{time_minutes:.2f} นาที")
