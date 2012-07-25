# py-gmail

A simple python script that I use to send quick emails from a gmail account with python (it works with google apps too). You have to specify your credentials in settings.json and place it in a secure place.

The script takes three arguments:
    1. -m, --message: the message
    2. -s, --subject: the subject
    3. -d, --destination: the destination email

Example:

    python maily.py -m 'Hello, World!' -s 'Test' -d 'javi.manzano.oller@gmail.com'
