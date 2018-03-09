Basic Usage
-----------

.. code:: python

    from randomuser import RandomUser

    # Generate a single user
    user = RandomUser()

    # Generate a list of 10 random users
    user_list = RandomUser.generate_users(10)

Both ``RandomUser()`` and ``RandomUser.generate_users()`` can optionally
accept a dictionary of parameter names to desired values using the
``get_params`` optional parameter:

.. code:: python

    # Generate a random female user
    user = RandomUser({'gender': 'female'})

    # Generate a list of 10 random users from Canada
    user_list = RandomUser.generate_users(10, {'nat': 'ca'})

For more information on what parameters can be specified, see the
`randomuser.me documentation <https://randomuser.me/documentation>`__.


