import time
# Function without sleep
def countdown(x):
    while x >= 1:
        print(f"{x} SECOND(S)!")
        x -= 1
    print("HAPPY NEW YEAR!")
countdown(10)

# Function with sleep
def countdown_with_sleep(x):
    while x >= 1:
        print(f"{x} SECOND(S)!")
        time.sleep(1)  # one second pause
        x -= 1
    print("HAPPY NEW YEAR!")
countdown_with_sleep(10)
