#Title: Python Practice Problems
#Author: Richard Fleming
#Create Date: August 18, 2021

#PROBLEM 1 - Calculate Minutes to seconds
def run_calculate_mins_to_secs():
    minutes = int(input("Enter minutes to get seconds: "))
    seconds = calculate_mins_to_secs(minutes)
    print(f'There are {seconds} seconds in {minutes} minutes.')

def calculate_mins_to_secs(minutes):
    seconds = minutes * 60
    return seconds

#run_calculate_mins_to_secs()



#PROBLEM 2 - Area of a Triangle
def run_get_triangle_area():
    triangle_height = int(input("Enter the height of the triangle: "))
    triangle_base = int(input("Enter the base length of the triangle: "))
    triangle_area = get_triangle_area(triangle_height, triangle_base)
    print(f'The area of a triangle with {triangle_base} base length and {triangle_height} height is {triangle_area}.')

def get_triangle_area(height, base):
    area = (base * height) / 2
    return area

run_get_triangle_area()