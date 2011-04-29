# Overview #

**recaptcha-client-1.0.6-ssl** is a Python 2.x module that interfaces with reCAPTCHA and reCAPTCHA Mailhide. It generates HTML to let you display reCAPTCHA on your website, and to submit reCAPTCHA attempts to the reCAPTCHA server.

- **reCAPTCHA** is generally used inside HTML forms. Users must solve a reCAPTCHA to submit a form successfully.
- **reCAPTCHA Mailhide** masks email addresses, and requires a user to solve a reCAPTCHA to reveal the full email address.

This code is forked from the original Python *recaptcha-client 1.0.6*, and is fully backwards compatible with it (no code changes are necessary to implement). The original client is located here: http://pypi.python.org/pypi/recaptcha-client

It has all of the features of *recaptcha-client 1.0.6*, plus the following new ones:

- SSL support for submit() in captcha.py.
- SSL support for asurl() and ashtml() in mailhide.py.
- Timeout variable for submit().
- Exception handling for urllib2.urlopen in submit().
- Lots of comments.
- Code tidying.

More information about reCAPTCHA and reCAPTCHA Mailhide: http://www.google.com/recaptcha

# Installation #

### Dependencies: ###

If you wish to use **reCAPTCHA Mailhide** (recaptcha.client.mailhide), you must also install the Python Crypto library. This is not required if you only use **reCAPTCHA** (recaptcha.client.captcha). The easiest way to install this is with pip:

    $ sudo pip install pycrypto
    $ python
    >>> import Crypto
    >>> Crypto
    <module 'Crypto' from '.../site-packages/Crypto/__init__.pyc'>

### Download and Install: ###

Make sure to uninstall any old versions of recaptcha-client first.

    $ git clone git://github.com/dave-gallagher/recaptcha-client-1.0.6-ssl.git
    $ cd .../recaptcha-client-1.0.6-ssl
    $ sudo python setup.py install

### Test Installation: ###

    $ python
    >>> import recaptcha
    >>> recaptcha
    <module 'recaptcha' from 'recaptcha/__init__.pyc'>

### Uninstallation: ###
    
    $ python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()"
    <path_to_python>.../site-packages
    $ sudo rm -r <path_to_python>.../site-packages/recaptcha_client-1.0.6_ssl*.egg

# reCAPTCHA Usage #

- You must have both a Public and Private **reCAPTCHA** API Key.
- These keys are different than **reCAPTCHA Mailhide** API Keys.
- Register for free keys here: http://www.google.com/recaptcha/whyrecaptcha
- Note: A *global key* is not needed for local development (127.0.0.1).

### Generate reCAPTCHA HTML: ###

Place the generated HTML inside your form code, and render it to a webpage as a HTTP Response.

    >>> from recaptcha.client.captcha import displayhtml
    >>> 
    >>> PUBLIC_KEY = "YOUR_PUBLIC_RECAPTCHA_KEY"
    >>> 
    >>> html = displayhtml(public_key=PUBLIC_KEY, use_ssl=True, error=None)
    >>> print html
    <script type="text/javascript" src="https://www.google.com/recaptcha/api/challenge?k=YOUR_PUBLIC_RECAPTCHA_KEY"></script><noscript>  <iframe src="https://www.google.com/recaptcha/api/noscript?k=YOUR_PUBLIC_RECAPTCHA_KEY" height="300" width="500" frameborder="0"></iframe><br />  <textarea name="recaptcha_challenge_field" rows="3" cols="40"></textarea>  <input type='hidden' name='recaptcha_response_field' value='manual_challenge' /></noscript>

### Validate: ###

After receiving an HTTP POST Request from a submitted form, extract both *recaptcha_challenge_field* and *recaptcha_response_field* from the POST. You should also extract the clients IP address (see your API/webserver for details on how to do this).

    >>> from recaptcha.client.captcha import submit
    >>> 
    >>> recaptcha_challenge_field = http_request_post.get("recaptcha_challenge_field", None)   # Psuedo-code
    >>> recaptcha_response_field = http_request_post.get("recaptcha_response_field", None)     # Psuedo-code
    >>> client_ip_address = ...
    >>> PRIVATE_KEY = "YOUR_PRIVATE_RECAPTCHA_KEY"
    >>> 
    >>> recaptcha_response = submit(recaptcha_challenge_field, recaptcha_response_field, PRIVATE_KEY, client_ip_address, use_ssl=True, timeout_seconds=60)
    >>> if recaptcha_response.is_valid:
    ...    print "reCAPTCHA was solved successfully"
    ... else:
    ...    print "reCAPTCHA failed with error: %s" % recaptcha_response.error_code

# reCAPTCHA Mailhide Usage #

- You must have both a Public and Private **reCAPTCHA Mailhide** API Key.
- These keys are different than **reCAPTCHA** API Keys.
- Register for a free key here: http://www.google.com/recaptcha/mailhide/
- You MUST install Python's Crypto library to use this. See *Installation* for details.

### Generate reCAPTCHA Mailhide HTML: ###

Place this HTML inside your webpage. The email address will be abridged. To reveal the full email address, the user clicks on a link to open a pop-up window containing a reCAPTCHA. After solving the reCAPTCHA, the full email address is displayed.

    >>> from recaptcha.client.mailhide import ashtml
    >>> 
    >>> EMAIL = "susan_smith@example.com"
    >>> PUBLIC_MAILHIDE_KEY = "YOUR_PUBLIC_RECAPTCHA_MAILHIDE_KEY"
    >>> PRIVATE_MAILHIDE_KEY = "YOUR_PRIVATE_RECAPTCHA_MAILHIDE_KEY"
    >>> 
    >>> html = ashtml(EMAIL, PUBLIC_MAILHIDE_KEY, PRIVATE_MAILHIDE_KEY, use_ssl=True)
    >>> print html
    susa<a href="https://www.google.com/recaptcha/mailhide/d?k=XXXXXXXXXXXXXXXXXXXXXXXXXX&amp;c=YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY" onclick="window.open('https://www.google.com/recaptcha/mailhide/d?k=XXXXXXXXXXXXXXXXXXXXXXXXXX&amp;c=YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY', '', 'toolbar=0,scrollbars=0,location=0,statusbar=0,menubar=0,resizable=0,width=500,height=300'); return false;" title="Reveal this e-mail address">...</a>@example.com































