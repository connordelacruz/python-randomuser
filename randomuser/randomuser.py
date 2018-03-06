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
    # Dictionary where the random user _data will be stored
    _data = {}
    # Dictionary where _info section of results will be stored
    _info = {}

    def __init__(self, get_params=None, user_data=None, api_info=None):
        """Initialize RandomUser object

        :param get_params: (Optional) Dictionary mapping query parameter names to their values. See https://randomuser.me/documentation for details on parameters.
        :param user_data: (Optional) If specified, this _data will be used instead of querying the API for user _data. Use in instances where the user _data has already been generated (e.g. restoring user _data, creating multiple users with single call to API using the 'results' parameter)
        :param api_info: (Optional) If the user is being generated with the user_data parameter, the _info variable will be set to this. Otherwise, it will be ignored when generating a random user.
        """
        global URL
        if user_data is not None:
            self._data = user_data
            self._info = api_info
        else:
            self.request_url = URL
            if get_params:
                self.request_url += '?' + urlencode(get_params)
            self._generate_user()

    def _generate_user(self):
        # TODO: catch timeout exception and fall back to local _data?
        results = json.loads(request.urlopen(self.request_url).read())
        self._data = results['results'][0]
        self._info = results['info']

    # Personal Info
    # --------------------------------

    def get_first_name(self, capitalize=True):
        """Returns first name

        :param capitalize: (Default = True) Capitalize first letter if True
        """
        first_name = self._data['name']['first']
        return first_name.title() if capitalize else first_name

    def get_last_name(self, capitalize=True):
        """Returns last name

        :param capitalize: (Default = True) Capitalize first letter if True
        """
        last_name = self._data['name']['last']
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
        return self._data['gender']

    def get_dob(self, parse_time=False):
        """Returns date of birth as a string in the format '%Y-%m-%d %H:%M:%S'

        :param parse_time: (Default = False) If True, parse date of birth string using time.strptime() and return the results instead of a string
        """
        dob = self._data['dob']
        if parse_time:
            dob = self._parse_time(dob)
        return dob

    def get_nat(self):
        """Returns nationality"""
        return self._data['nat']

    # Location
    # --------------------------------

    def get_street(self):
        """Returns street address"""
        return self._data['location']['street']

    def get_city(self):
        """Returns city"""
        return self._data['location']['city']

    def get_state(self):
        return self._data['location']['state']

    def get_postcode(self):
        """Returns post code"""
        return self._data['location']['postcode']

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
        return self._format_phone_number(self._data['phone'], strip_parentheses, strip_hyphens)

    def get_cell(self, strip_parentheses=False, strip_hyphens=False):
        """Returns cell phone number as a string in the format '(###)-###-####'

        :param strip_parentheses: (Default = False) Omit parentheses if True
        :param strip_hyphens: (Default = False) Omit hyphens if True
        """
        return self._format_phone_number(self._data['cell'], strip_parentheses, strip_hyphens)

    def get_email(self):
        """Returns email address"""
        return self._data['email']

    # Login
    # --------------------------------

    def get_username(self):
        """Returns username"""
        return self._data['login']['username']

    def get_password(self):
        """Returns password"""
        return self._data['login']['password']

    def get_registered(self, parse_time=False):
        """Returns registration date as a string in the format '%Y-%m-%d %H:%M:%S'

        :param parse_time: (Default = False) If True, parse date string using time.strptime() and return the results instead of a string
        """
        registered = self._data['registered']
        if parse_time:
            registered = self._parse_time(registered)
        return registered

    def get_login_salt(self):
        """Returns user login salt"""
        return self._data['login']['salt']

    def get_login_md5(self):
        """Returns user login md5"""
        return self._data['login']['md5']

    def get_login_sha1(self):
        """Returns user login sha1"""
        return self._data['login']['sha1']

    def get_login_sha256(self):
        """Returns user login sha256"""
        return self._data['login']['sha256']

    # ID
    # --------------------------------

    def get_id_type(self):
        """Returns the ID type"""
        return self._data['id']['name']

    def get_id_number(self):
        """Returns the ID number"""
        return self._data['id']['value']

    def get_id(self):
        """Returns a dictionary mapping 'type' to ID type and 'number' to ID number
        """
        return {'type': self.get_id_type(), 'number': self.get_id_number()}

    # Misc
    # --------------------------------

    # Constants for possible picture sizes
    PICTURE_SIZE_LARGE = 'large'
    PICTURE_SIZE_MEDIUM = 'medium'
    PICTURE_SIZE_THUMBNAIL = 'thumbnail'

    def get_picture(self, size=PICTURE_SIZE_LARGE):
        """Returns url to a .jpg of the generated user

        :param size: (Default = PICTURE_SIZE_LARGE) The size of picture to return the url for. Possible values for this are stored in constants PICTURE_SIZE_LARGE, PICTURE_SIZE_MEDIUM, and PICTURE_SIZE_THUMBNAIL
        """
        return self._data['picture'][size]

    # Constants for _info dictionary keys
    INFO_SEED = 'seed'
    INFO_RESULTS = 'results'
    INFO_PAGE = 'page'
    INFO_VERSION = 'version'

    def get_info(self):
        """Returns a dictionary with information about the API query

        Keys for the _info dictionary are stored in constants INFO_SEED, INFO_RESULTS, INFO_PAGE, and INFO_VERSION
        """
        return self._info

    # Helper Functions
    # --------------------------------

    def _parse_time(self, date_string):
        """Parses the date string format returned by the API and returns the time tuple result of time.strptime()

        :param date_string: The date string in the format '%Y-%m-%d %H:%M:%S'
        """
        date_format = '%Y-%m-%d %H:%M:%S'
        return time.strptime(date_string, date_format)

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
            user = RandomUser(user_data=user_data, api_info=info)
            users.append(user)
        return users
