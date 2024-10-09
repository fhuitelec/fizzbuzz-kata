PYTEST := uv run pytest
PYLINT := uv run pylint
PYRIGHT := uv run pyright
RUFF := uv run ruff
CLI := uv run fizzbuzz
LINT_DIRECTORIES := src/fizzbuzz tests

.PHONY: run
run:
	$(CLI)

.PHONY: test
test:
	$(PYTEST) -v --cov-report term --cov=src/fizzbuzz

.PHONY: lint
lint:
	$(PYLINT)  $(LINT_DIRECTORIES)
	$(PYRIGHT) $(LINT_DIRECTORIES)
	$(RUFF) format       $(LINT_DIRECTORIES)
	$(RUFF) check  --fix $(LINT_DIRECTORIES)
