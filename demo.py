import random
import time



x = random.random()
print(x)

y = random.randint(10, 50)

current_time = time.time()
total_seconds = int(current_time)

seconds = total_seconds % 60

total_minutes = seconds // 60

print(total_seconds)