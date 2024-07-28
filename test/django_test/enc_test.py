from encryption import *
m_plaint_text = {'DB_PASSWORD': '', 'SECRET_KEY': '##$$'}
lib = OutboxEncryption()
lib.enc_environ(m_plaint_text)

# how to run:
# type:
# python manage.py shell
# import enc_test
## evaluate resulte ....
