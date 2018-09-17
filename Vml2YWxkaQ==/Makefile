.PHONY: env run test
.DEFAULT: env

env:
	@pipenv install --dev

run:
	@pipenv run pgzrun src/main.py

test:
	@echo "Tests"
