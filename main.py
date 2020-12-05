# This is Python script for creating fake employee data excel spreadsheet
import pandas as pd
import numpy as np
from faker.providers.person.en import Provider


def random_names(name_type, size):
    """
    Generate n-length ndarray of person names.
    name_type: a string, either first_names or last_names
    """
    names = getattr(Provider, name_type)
    return np.random.choice(names, size=size)


def random_genders(size, p=None):
    """Generate n-length ndarray of genders."""
    if not p:
        # default probabilities
        p = (0.49, 0.49, 0.01, 0.01)
    gender = ("M", "F", "O", "")
    return np.random.choice(gender, size=size, p=p)


def random_dates(start, end, size):
    """
    Generate random dates within range between start and end.
    Adapted from: https://stackoverflow.com/a/50668285
    """
    # Unix timestamp is in nanoseconds by default, so divide it by
    # 24*60*60*10**9 to convert to days.
    divide_by = 24 * 60 * 60 * 10 ** 9
    start_u = start.value // divide_by
    end_u = end.value // divide_by
    return pd.to_datetime(np.random.randint(start_u, end_u, size), unit='D')


def random_employeeid(size):
    """
    Generate random employee ids within range between start and end.
    """
    return np.random.randint(1000000000, 1000099999, size)


size = 100
df = pd.DataFrame(columns=['First', 'Last', 'Gender', 'Birthdate', 'Employee ID'])
df['First'] = random_names('first_names', size)
df['Last'] = random_names('last_names', size)
df['Gender'] = random_genders(size)
df['Birthdate'] = random_dates(start=pd.to_datetime('1960-01-01'), end=pd.to_datetime('1998-01-01'), size=size)
df['Employee ID'] = random_employeeid(size=size)
df.to_excel('fake-employee-data.xls')
