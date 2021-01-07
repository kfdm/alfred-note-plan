APP_BIN := .venv/bin/noteplan-list
PIP_BIN := .venv/bin/pip

$(PIP_BIN):
	python3 -m venv .venv

${APP_BIN}: $(PIP_BIN)
	${PIP_BIN} install -e .

.PHONY: pip
pip:	$(PIP_BIN)

clean:
	rm -rf .venv
