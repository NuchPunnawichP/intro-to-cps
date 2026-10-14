import threading

# Initialize travel supply
breadCount = 0
waterCount = 0

# Number of iterations
limit = 1_000_000

def add_bread():
    global breadCount
    breadCount += 1
    # name = threading.current_thread().name
    # print(name, "is adding stuff")

def add_water():
    global waterCount
    waterCount += 1
    # name = threading.current_thread().name
    # print(name, "is adding stuff")

def hobbit():
    for i in range(limit):
        add_bread()
        add_water()

# Create two threads
frodo = threading.Thread(target=hobbit, name="Mr. Frodo")
sam = threading.Thread(target=hobbit, name="Sammy")

# Start threads
frodo.start()
sam.start()

# Wait for threads to finish
frodo.join()
sam.join()

# Display results
print("Sammy, we should bring", breadCount, "loaves of bread to Mordor.")
print("Mr. Frodo, better carry", waterCount, "bottles of water with us too.")