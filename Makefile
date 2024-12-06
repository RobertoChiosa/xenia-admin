fixtures-dump:
	@echo "Dumping fixtures in management fixtures ..."
	source venv/bin/activate &&
	cd project && python manage.py dumpdata --indent 2 --output fixtures/initial_data.json
