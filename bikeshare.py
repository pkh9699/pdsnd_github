import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
        try:
            city = str(input('Enter a desired city name (chicago, new york city, or washington): '))
        except:
            print('That\'s not a valid input.')
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            break
        else:
            print('Invalid input, try again.')


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input('Enter the name of the month you want to know about (or all for no filter): '))
            month = month.title()
        except:
            print('That\'s not a valid input.')
        if month == 'January' or month == 'February' or month == 'March' or month == 'April' or month == 'May' or month == 'June' or month == 'July' or month == 'August' or month == 'September' or month == 'October' or month == 'November' or month == 'December':
            break
        elif month == 'All':
            break
        else:
            print('Invalid input, try again.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input('Enter the name of the day of week you want to know about (or all for no filter): '))
            day = day.title()
        except:
            print('That\'s not a valid input.')
        if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday' or day == 'Sunday' or day == 'All':
            break
        else:
            print('Invalid input, try again.')
    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month_no'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        month = months.index(month) + 1#the month in the () is the input of the month
        df = df[df['month_no'] == month]
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(city):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    dfo = pd.read_csv(CITY_DATA[city])
    dfo['Start Time'] = pd.to_datetime(dfo['Start Time'])
    dfo['month_no'] = dfo['Start Time'].dt.month
    dfo['day_of_week'] = dfo['Start Time'].dt.weekday_name
    dfo['hours'] = dfo['Start Time'].dt.hour
    start_time = time.time()

    # TO DO: display the most common month
    mcm = dfo['month_no'].mode()[0]
    print('The most common month: ',mcm)
    # TO DO: display the most common day of week
    mcdw = dfo['day_of_week'].mode()[0]
    print('The most common day of week: ',mcdw)
    # TO DO: display the most common start hour
    mcsh = dfo['hours'].mode()[0]
    print('The most common start hour: ',mcsh)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mcuss = df['Start Station'].mode()[0]
    print('The most commonly used start station: ',mcuss)
    # TO DO: display most commonly used end station
    mcues = df['End Station'].mode()[0]
    print('The most commonly used end station: ',mcues)
    # TO DO: display most frequent combination of start station and end station trip
    df['link'] ='From '+ df['Start Station'] +' to ' +  df['End Station']
    mfc = df['link'].mode()[0]
    print('The most frequent combination of start station and end station trip is: ')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    ttt = df['Trip Duration'].sum()
    print('The total travel time: ',ttt)

    # TO DO: display mean travel time
    print('The mean travel time: ',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print('The counts of gender is not provided in the data file.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        print('The earliest year of birth of passengers is: ',df['Birth Year'].min())
        print('The most recent year of birth of passengers is: ',df['Birth Year'].max())
        print('The most common year of birth of passengers is: ',df['Birth Year'].mode())
    else:
        print('There is no data concerning Birth Year in the file of the city.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(df.head(5))
    h = 0
    while True:
        try:
            boo = str(input('Do you like to see some more individual data (type in yes or no): '))
        except:
            print('That\'s not a valid input.')
        if boo == 'no':
            break
        elif boo == 'yes':
            h += 1
            h1 = 5*h
            h2 = h1 + 5
            print(df.iloc[h1:h2])
        else:
            print('Invalid input, please try again.')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(city)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
