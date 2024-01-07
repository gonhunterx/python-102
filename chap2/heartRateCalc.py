# heart rate calculator 


def calc_heartrate(age):
    max_hr = 220 - age
    target_hr = (max_hr * .85) - 50 
    return max_hr, target_hr

def main():
    age = input("Please enter your age: ")
    
    max_hr, target_hr = calc_heartrate(int(age))
    print(f"Your max heart rate is {max_hr}\n Your target heart rate is {target_hr}")

main()