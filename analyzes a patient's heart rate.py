# program that analyzes a patient's heart rate.

heart_rate = int(input())

too_low = heart_rate < 60
too_high = heart_rate > 100
normal = heart_rate in range(60, 100)
print("Low Heart rate:")
print(too_low)

print("High Heart rate:")
print(too_high)

print("normal heart rate:")
print(normal)
