# Class for generating random user information

# Imports
# ----------------------------------------------------------------
from urllib import request, error
from urllib.parse import urlencode
import json
import time
import re

# Global Variables
# ----------------------------------------------------------------

URL = 'https://randomuser.me/api/'

# Classes
# ----------------------------------------------------------------

class RandomUser(object):
    # Dictionary where the random user data will be stored
    data = {}

    def __init__(self, get_params=None, user_data=None):
        """Initialize RandomUser object

        :param get_params: (Optional) Dictionary mapping query parameter names to their values. See https://randomuser.me/documentation for details on parameters.
        :param user_data: (Optional) If specified, this data will be used instead of querying the API for user data. Can be useful when generating multiple users with a single query using the results parameter.
        """
        global URL
        if user_data is not None:
            self.data = user_data
        else:
            self.request_url = URL
            if get_params:
                self.request_url += '?' + urlencode(get_params)
            self._generate_user()

    def _generate_user(self):
        # TODO: catch timeout exception and fall back to local data?
        results = json.loads(request.urlopen(self.request_url).read())
        self.data = results['results'][0]
        self.data['info'] = results['info']


    # Personal Info
    # --------------------------------

    def get_first_name(self, capitalize=True):
        """Returns first name

        :param capitalize: (Default = True) Capitalize first letter if True
        """
        first_name = self.data['name']['first']
        return first_name.title() if capitalize else first_name

    def get_last_name(self, capitalize=True):
        """Returns last name

        :param capitalize: (Default = True) Capitalize first letter if True
        """
        last_name = self.data['name']['last']
        return last_name.title() if capitalize else last_name

    def get_full_name(self, capitalize=True):
        """Returns first and last name separated by a space

        :param capitalize: (Default = True) Capitalize first letter of each name if True
        """
        first_name = self.get_first_name(capitalize)
        last_name = self.get_last_name(capitalize)
        full_name = '{} {}'.format(first_name, last_name)
        return full_name

    def get_gender(self):
        """Returns gender"""
        return self.data['gender']

    def get_dob(self, parse_time=False):
        """Returns date of birth as a string in the format '%Y-%m-%d %H:%M:%S'

        :param parse_time: (Default = False) If True, parse date of birth string using time.strptime() and return the results instead of a string
        """
        dob = self.data['dob']
        if parse_time:
            date_format = '%Y-%m-%d %H:%M:%S'
            dob = time.strptime(dob, date_format)
        return dob

    # Location
    # --------------------------------

    def get_street(self):
        """Returns street address"""
        return self.data['location']['street']

    def get_city(self):
        """Returns city"""
        return self.data['location']['city']

    def get_state(self):
        return self.data['location']['state']

    def get_postcode(self):
        """Returns post code"""
        return self.data['location']['postcode']

    def get_zipcode(self):
        """ Returns zip code (wrapper for get_postcode())"""
        return self.get_postcode()

    # Contact
    # --------------------------------

    def _format_phone_number(self, phone_string, strip_parentheses=True, strip_hyphens=True):
        """Takes a string representation of a phone number and strips characters based on parameter values

        :param phone_string: The phone number as a string
        :param strip_parentheses: (Default = True) Remove '(' and ')' characters if True
        :param strip_hyphens: (Default = True) Remove '-' characters if True
        """
        if strip_parentheses:
            phone_string = re.sub('[()]', '', phone_string)
        if strip_hyphens:
            phone_string = re.sub('-', '', phone_string)
        return phone_string

    def get_phone(self, strip_parentheses=False, strip_hyphens=False):
        """Returns phone number as a string in the format '(###)-###-####'

        :param strip_parentheses: (Default = False) Omit parentheses if True
        :param strip_hyphens: (Default = False) Omit hyphens if True
        """
        return self._format_phone_number(self.data['phone'], strip_parentheses, strip_hyphens)

    def get_cell(self, strip_parentheses=False, strip_hyphens=False):
        """Returns cell phone number as a string in the format '(###)-###-####'

        :param strip_parentheses: (Default = False) Omit parentheses if True
        :param strip_hyphens: (Default = False) Omit hyphens if True
        """
        return self._format_phone_number(self.data['cell'], strip_parentheses, strip_hyphens)

    def get_email(self):
        """Returns email address"""
        return self.data['email']

    # Login
    # --------------------------------

    def get_username(self):
        """Returns username"""
        return self.data['login']['username']

    def get_password(self):
        """Returns password"""
        return self.data['login']['password']

    # Misc
    # --------------------------------

    def get_picture(self):
        """Returns url to a .jpg of the generated user"""
        return self.data['picture']['large']

    def get_info(self):
        """Returns a dictionary with information about the API query"""
        return self.data['info']

    # Static Methods
    # --------------------------------

    @staticmethod
    def generate_users(amount, get_params=None):
        """Returns a list containing the specified amount of randomly generated users.

        The Random User Generator API can generate multiple users in a single query
        instead of connecting once for each user and increasing load on both ends.

        :param amount: The number of users to generate.
        :param get_params: (Optional) Dictionary mapping query parameter names to their values. See https://randomuser.me/documentation for details on parameters.
        """
        global URL
        if get_params is None:
            get_params = {}
        # Max amount allowed is 5,000 (https://randomuser.me/documentation#multiple)
        get_params['results'] = amount if amount <= 5000 else 5000
        request_url = URL + '?' + urlencode(get_params)
        results = json.loads(request.urlopen(request_url).read())
        info = results['info']
        users = []
        for user_data in results['results']:
            user_data['info'] = info
            user = RandomUser(user_data=user_data)
            users.append(user)
        return users

