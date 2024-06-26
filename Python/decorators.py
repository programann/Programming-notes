def check_working_hours(func):
    def wrapper(time):
        if 1100 <time< 2100:
            func(time)
        else:
            print("Am off duty")
    return wrapper

@ check_working_hours
def clean_the_floor(time):
    print('Cleaning the floor')

@ check_working_hours
def wash_the_floor(time):
    print('Washing dishes')

@ check_working_hours
def take_deliveries(time):
    print ('Taking deliveries')

print(take_deliveries(1500)) # should return Taking deliveries