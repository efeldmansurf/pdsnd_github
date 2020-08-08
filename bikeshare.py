import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_LIST = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city you would like to analyze? chicago, new york city or washington?')
        if city not in CITY_DATA:
            print('Looks like that\'s not one of the cities!')
        else:
            break 

        print('you choose: ', city)


    # get user input for month 
    while True:        
        month = input('Which month: january, february, march, april, may, june? Or all?')
        if month not in MONTH_LIST:
            print('Looks like that\'s not one of the months!')
        else:
            break 
           

        print('you choose: ', month)




    # get user input for day of week 
    while True:
        day = input('Which day: monday, tuesday, wednesday, thursday, friday, saturday, sunday? Or all?')
        if day not in DAY_LIST:
            print('Looks like that\'s not one of the days!')
        else:
            break 

        print('you choose: ', day)

    return city, month, day     
    print('-'*40)


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTH_LIST.index(month)

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df, city):
    """Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nAnalyzing The Most Frequent Times of Travel for', city.upper(), '...........\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most popular month is: " + MONTH_LIST[popular_month].title())

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print("The most popular day of week is: " + popular_day_of_week)

    # TO DO: display the most common start hour
    popular_start_hour = df['hour'].mode()[0]
    print("The most popular start hour is: " + str(popular_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df, city):
    """Displays statistics on the most popular stations and trip.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nAnalyzing The Most Popular Stations and Trip for', city.upper(), '...........\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    popular_start_station_amount = df['Start Station'].value_counts()[0]
    print("The most popular start station is: ", popular_start_station, "count: ", popular_start_station_amount, "times")

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    popular_end_station_amount = df['End Station'].value_counts()[0]
    print("The most popular end station: ", popular_end_station, "count: ", popular_end_station_amount, "times")

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    frequent_combo_count = (df['Start Station'] + "||" + df['End Station']).value_counts()[0]
    print("The most frequent combination of start station and end station trip is : " + str(frequent_combination.split("||")))
    print("count: ", frequent_combo_count, "times")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df, city):
    """Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nAnalyzing Trip Duration for', city.upper(), '...........\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: " + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nAnalyzing User Stats for', city.upper(), '...........\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types are: \n" + str(user_types))

    
    # TO DO: Display counts of gender
    if city == 'chicago' or city == 'new york city':
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender from the given fitered data is: \n" + str(gender))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = int(df['Birth Year'].min())
        most_recent_birth = int(df['Birth Year'].max())
        most_common_birth = int(df['Birth Year'].mode()[0])
        print('Earliest birthdate for a user is: {}'.format(earliest_birth))
        print('Most recent birthdate for a user is: {}'.format(most_recent_birth))
        print('Most common birthdate for all user is: {}'.format(most_common_birth))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, city)
        station_stats(df, city)
        trip_duration_stats(df, city)
        user_stats(df, city)
        

        restart = input('\nWould you like to run the date again? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()