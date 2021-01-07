APP_BIN := .venv/bin/noteplan-list
PIP_BIN := .venv/bin/pip

$(PIP_BIN):
	python3 -m venv .venv
	${PIP_BIN} install -e .

${APP_BIN}: $(PIP_BIN)
	${PIP_BIN} install -e .

.PHONY:	pip
pip:
	${PIP_BIN} install -e .

clean:
	rm -rf .venv
