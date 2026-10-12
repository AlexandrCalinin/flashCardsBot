.PHONY: install run lint format fix check

# install project dependencies
install:
	uv sync && uv run pre-commit install

# launch project locally
run:
	uv run python -m bot.main

# uv lints and formating
lint:
	uv run ruff check .

format:
	uv run ruff format .

fix:
	uv run ruff check --fix .

# pre commit
check:
	uv run pre-commit run --all-files