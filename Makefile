install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

lint:
	poetry run flake8 gendiff

publish:
	poetry publish --dry-run

package-install:
	pip install --user --force-reinstall dist/*.whl

.PHONY: 
