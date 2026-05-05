.PHONY: setup test lint fmt

setup:
	python3 -m venv .venv
	. .venv/bin/activate && pip install -r requirements-dev.txt

test:
	pytest -q

lint:
	ruff check .

fmt:
	ruff format .
