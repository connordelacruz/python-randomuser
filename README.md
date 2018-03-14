# Python Random User Generator

Python class for generating random user data using [randomuser.me](https://randomuser.me) API.

## Basic Usage

```python
from randomuser import RandomUser

# Generate a single user
user = RandomUser()

# Generate a list of 10 random users
user_list = RandomUser.generate_users(10)
```

Both `RandomUser()` and `RandomUser.generate_users()` can optionally accept a dictionary of parameter names to desired values using the `get_params` optional parameter:

```python
# Generate a random female user
user = RandomUser({'gender': 'female'})

# Generate a list of 10 random users from Canada
user_list = RandomUser.generate_users(10, {'nat': 'ca'})
```

For more information on what parameters can be specified, see the [randomuser.me documentation](https://randomuser.me/documentation).

## Method Overview

For details on the RandomUser class and optional parameters for these methods, see the [documentation](http://connordelacruz.com/python-randomuser/randomuser.html).

### Getter Methods

* `get_cell()`
* `get_city()`
* `get_dob()`
* `get_email()`
* `get_first_name()`
* `get_full_name()`
* `get_gender()`
* `get_id()`
* `get_id_number()`
* `get_id_type()`
* `get_info()`
* `get_last_name()`
* `get_login_md5()`
* `get_login_salt()`
* `get_login_sha1()`
* `get_login_sha256()`
* `get_nat()`
* `get_password()`
* `get_phone()`
* `get_picture()`
* `get_postcode()`
* `get_registered()`
* `get_state()`
* `get_street()`
* `get_username()`
* `get_zipcode()`
