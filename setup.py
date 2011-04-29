try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(name='recaptcha-client',
      version='1.0.6-ssl',
      url = "http://recaptcha.net",
      author = "Ben Maurer",
      author_email = "support@recaptcha.net",
      description = "A plugin for reCAPTCHA and reCAPTCHA Mailhide",
      long_description = """\
Provides a CAPTCHA for Python using the reCAPTCHA service. Does not require
any imaging libraries because the CAPTCHA is served directly from reCAPTCHA.
Also allows you to securely obfuscate emails with Mailhide. This functionality
requires pycrypto. This library requires two types of API keys. If you'd like
to use the CAPTCHA, you'll need a key from https://www.google.com/recaptcha/admin/create.
For Mailhide, you'll need a key from http://www.google.com/recaptcha/mailhide/apikey.

The trunk can be checked out from
http://recaptcha.googlecode.com/svn/trunk/recaptcha-plugins/python,
and the associated Google Code project lives at
http://code.google.com/p/recaptcha. Note that this is a shared
project/repository for reCAPTCHA clients for several languages/environments.

There is also a Google Group at http://groups.google.com/group/recaptcha/.
Please use the associated mailing list for any questions or comments:
recaptcha@googlegroups.com. Like the Google Code project, the Google Group
mailing list is also shared among the several reCAPTCHA client implementations.

reCAPTCHA is written by Ben Maurer and maintained by Josh Bronson. It is
licensed under an MIT/X11 license.

--------------------------------------------------------------------------------

Version 1.0.6-ssl was created by Dave Gallagher on April 28, 2011, and was 
heavily derived from version 1.0.6. It's fully backwards compatible with 1.0.6 
and no code changes are necessary. Additions include:

- SSL support for submit() in captcha.py.
- SSL support for asurl() and ashtml() in mailhide.py.
- Timeout variable for submit().
- Exception handling for urllib2.urlopen in submit().
- Lots of comments.
- Code tidying.

Installation:		$ sudo python setup.py install
reCAPTCHA:			from recaptcha.client.captcha import displayhtml, submit
reCAPTCHA Mailhide:	from recaptcha.client.mailhide import ashtml

See comments inside /client/captcha.py and /client/mailhide.py for usage 
instructions.
""",

      license = "MIT/X11",
      classifiers = [
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        ],


      packages = find_packages(),

      extras_require = {
        'mailhide' : ['pycrypto'],
        },
      namespace_packages = ['recaptcha'],
      )
