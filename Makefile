install:
	poetry install

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff, tests

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --user --force-reinstall dist/*.whl

.PHONY: 
