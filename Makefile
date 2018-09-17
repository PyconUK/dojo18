.PHONY: env run test
.DEFAULT: env

env:
	@pipenv install --dev

run:
	@echo "Nothing here yet"

test:
	@echo "Tests"
