.PHONY: set-up run-tests

set-up:
	poetry install

run-tests: set-up
	poetry run pytest -vvs ./tests/
