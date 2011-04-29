## Overview

**recaptcha-client-1.0.6-ssl** is a Python module that interfaces with reCAPTCHA and reCAPTCHA Mailhide. It generates HTML to let you display reCAPTCHA on your website, and to submit reCAPTCHA attempts to the reCAPTCHA server.

It's forked from the original Python recaptcha-client 1.0.6, and is fully backwards compatible with it (no code changes are necessary to implement). The original client is located here: http://pypi.python.org/pypi/recaptcha-client

It has all of the features of recaptcha-client 1.0.6, plus the following new ones:

- SSL support for submit() in captcha.py.
- SSL support for asurl() and ashtml() in mailhide.py.
- Timeout variable for submit().
- Exception handling for urllib2.urlopen in submit().
- Lots of comments.
- Code tidying.


## Installation

# Install:

    $ git clone git://github.com/dave-gallagher/recaptcha-client-1.0.6-ssl.git
    $ cd .../recaptcha-client-1.0.6-ssl
    $ sudo python setup.py install

# Test Installation:

    $ python
    >>> from recaptcha.client.captcha import displayhtml, submit
    >>> from recaptcha.client.mailhide import ashtml
    >>> quit()

# Uninstallation:
    
    $ python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()"
    <path_to_python>.../site-packages
    $ cd <path_to_python>.../site-packages
    $ sudo rm -r recaptcha_client-1.0.6_ssl*.egg


## Usage
