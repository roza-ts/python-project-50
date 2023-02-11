install:
	poetry install

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff tests

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/

test print:
	poetry run pytest -s

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-install-force:
	python3 -m pip install --user --force-reinstall dist/*.whl

.PHONY: 
