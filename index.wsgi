import sae
from contactsync import wsgi

application = sae.create_wsgi_app(wsgi.application)

