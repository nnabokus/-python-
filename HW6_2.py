seconds = int(input("Введіть будь-ласка число:"))

day_sec = 24 * 60 * 60

days = seconds // day_sec
seconds = seconds % day_sec

hours = seconds // 3600
seconds = seconds % 3600

minutes = seconds // 60
secs = seconds % 60

if days == 1:
    day_word = "День"
elif 2 <= days <= 4:
    day_word = "Дні"
else:
    day_word = "Днів"

hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
secs = str(secs).zfill(2)

print(f"{days} {day_word}, {hours}:{minutes}:{secs}")
