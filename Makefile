fmt:
	isort .
	black .
	flake8 .

test:
	pytest

cov:
	coverage run
	coverage report
	coverage html
