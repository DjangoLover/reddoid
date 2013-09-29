TEST_APP=sources home

run:
	reddoid/manage.py runserver --settings=reddoid.settings.local

syncdb:
	reddoid/manage.py syncdb --settings=reddoid.settings.local

migrate:
	reddoid/manage.py migrate --settings=reddoid.settings.local

shell:
	reddoid/manage.py shell --settings=reddoid.settings.local

test:
	reddoid/manage.py test $(TEST_APP) --settings=reddoid.settings.local

manage:
	reddoid/manage.py $(CMD) --settings=reddoid.settings.local


heroku_syncdb:
	heroku run reddoid/manage.py syncdb

heroku_migrate:
	heroku run reddoid/manage.py migrate

heroku_load_posts:
	heroku run reddoid/manage.py load_posts
