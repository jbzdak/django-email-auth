
Yet another email login for django
==================================

Distict features:

- It actually fixes two problems with logging users by email, that is: email field is not unique
  and unindexed.
- Doesnt create new tables in the database.


This app is dead simple:

- It uses south to fix problems with email field on auth.User model
- It installs listener that adds a random username to User when saving if username is not set.

What it doesn't support:

- I didn't patch user creation process, in for which I developed it users will be created
  by admin.

When not to use it
------------------

When you are not using south.

Usage
-----

1. Install `south`
2. Add `email_login` to APPLICATIONS setting.
3. Sync db and then migrate `email_login`
4. Add `'email_login.backend.EmailAuthBackend'` to `AUTHENTICATION_BACKENDS` setting, so it looks like that::

    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'email_login.backend.EmailAuthBackend'
        )

