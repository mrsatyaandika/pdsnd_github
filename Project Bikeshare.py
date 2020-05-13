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
    cities = ['chicago', 'new york city', 'washington']
    city = input("Which city do you want to see? chicago, new york city, or washington?: ").lower()
    while city not in cities:
        city = input("Your selection is not in the menu, please select between chicago, new york city, or washington: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input("Which month do you want to see? between january to june, or all?: ").lower()
    while month not in months:
        month = input("Your selection is not in the menu, please select between january to june, or all: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = input("Which day in a week do you want to see? between monday to sunday, or all?: ").lower()
    while day not in days:
        day = input("Your selection is not in the menu, please select between monday to sunday, or all: ").lower()

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
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    df['weekday'] = df['Start Time'].dt.weekday_name
    popular_weekday = df['weekday'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('most common month is {}'.format(popular_month))
    print('most common weekday is {}'.format(popular_weekday))
    print('most common hour is {}'.format(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startstation = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    popular_endstation = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    popular_combinestation = df.groupby(['Start Station', 'End Station']).size().idxmax()

    print('most commonly used start station is {}'.format(popular_startstation))
    print('most commonly used end station is {}'.format(popular_endstation))
    print('most frequent combination of start and end station trip is {}'.format(popular_combinestation))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    average_travel = df['Trip Duration'].mean()

    print('total travel time is {}'.format(total_travel))
    print('average travel time is {}'.format(average_travel))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of each user type are\n{}'.format(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        genders = df['Gender'].value_counts()
        print('\ncounts of each gender are\n{}'.format(genders))
    else:
        print('\nno data gender in data source')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        most_birth = df['Birth Year'].mode()
        print('\nearliest year of birth is {}'.format(earliest_birth))
        print('most recent year of birth is {}'.format(recent_birth))
        print('most common year of birth is {}'.format(earliest_birth))
    else:
        print('\nno data birth year in data source')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    from_row = 0
    to_row = 0
    see_rows = input("Do you like to see the raw data?: ")
    while see_rows.lower() == 'yes':
        to_row += 5
        print(df.iloc[from_row:to_row])
        from_row = to_row
        see_rows = input("Do you like to see the next 5 rows?: ")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
