run:
	reddoid/manage.py runserver --settings=reddoid.settings.local

syncdb:
	reddoid/manage.py syncdb --settings=reddoid.settings.local
