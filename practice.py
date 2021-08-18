def run_calculate_mins_to_secs():
    minutes = int(input("Enter minutes to get seconds: "))
    seconds = calculate_mins_to_secs(minutes)
    print(f'There are {seconds} seconds in {minutes} minutes.')

def calculate_mins_to_secs(minutes):
    seconds = minutes * 60
    return seconds

run_calculate_mins_to_secs()