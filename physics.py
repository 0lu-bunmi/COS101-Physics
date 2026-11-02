# COS 101 Assignment
# Five Basic Physics Formulas

# 1. Speed: speed = distance / time
def calculate_speed(distance, time):
    return distance / time


# 2. Acceleration: acceleration = (final velocity - initial velocity) / time
def calculate_acceleration(final_velocity, initial_velocity, time):
    return (final_velocity - initial_velocity) / time


# 3. Force: force = mass * acceleration
def calculate_force(mass, acceleration):
    return mass * acceleration


# 4. Work done: work = force * distance
def calculate_work(force, distance):
    return force * distance


# 5. Kinetic energy: KE = 1/2 * mass * velocity squared
def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2


if __name__ == "__main__":
    print("Speed:", calculate_speed(100, 20), "m/s")
    print("Acceleration:", calculate_acceleration(30, 10, 5), "m/s^2")
    print("Force:", calculate_force(10, 5), "N")
    print("Work done:", calculate_work(20, 5), "J")
    print("Kinetic energy:", calculate_kinetic_energy(10, 4), "J")
