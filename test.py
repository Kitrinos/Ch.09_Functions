import math

def volume_sphere(r):
    volume = 4/3*math.pi*r**3
    return volume

def main():
    volume = volume_sphere(2)
    print(f"Your volume is {volume:.2f} m^3")

if __name__ == "__main__":
    main()
