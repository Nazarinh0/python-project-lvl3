install:
	poetry install

build:
	poetry build

test:
	poetry run pytest

package-install:
	python3.10 -m pip install --user dist/*.whl

lint:
	poetry run flake8 page_loader

test-coverage:
	poetry run pytest --cov=page_loader --cov-report=xml