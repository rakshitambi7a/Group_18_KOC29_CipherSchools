from datetime import datetime

# Get the current time
time = datetime.now().time()

# Extract the hour and minute from the time object
hour = time.hour
minute = time.minute

# Calculate the angle between the hour and minute hand
hour_angle = (hour + (minute/60)) * 30
minute_angle = minute * 6
angle = abs(hour_angle - minute_angle)

# Print the angle
print("The angle between the hour and minute hand is: ", angle)
