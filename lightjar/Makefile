PROJECT = $(shell basename $$(pwd))

all: format lint test clean

black:
	poetry run black .

isort:
	poetry run isort .

format: black isort

lint:
	poetry run pylint \
		--disable C0114 \
		--disable C0330 \
		--disable R0201 \
		--disable R0903 \
		.

test:
	poetry run python -m pytest \
		--random-order \
		--verbose \
		--capture no \
		--failed-first \
		--exitfirst \
		--cov

clean:
	@find . -depth -name __pycache__ -exec rm -fr {} \;
	@find . -depth -name .pytest_cache -exec rm -fr {} \;
	@find . -depth -name ".coverage.*" -exec rm {} \;
	@find . -depth -name "*egg-info" -exec rm -fr {} \;

install:
	poetry install
