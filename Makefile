help:
	@echo "make run          - run the application"
	@echo "make start_server - run as a server (see README)"
	@echo "make test         - run unit tests"
	@echo "make venv_nuke    - remove the virtual environment"


run: .venv
	export PYTHONPATH="$(PWD)"; \
	./.venv/bin/python3 main.py 10 88 93 82

start_server: .venv
	./.venv/bin/python3 -m uvicorn app:app --reload

curl_test:
	curl \
		-X POST \
		-H "Content-Type: application/json" \
		-d '{"numbers": [17, 21, 100, 2000, 999999]}' \
		"http://127.0.0.1:8000/convert/" \

	@echo

test: .venv
	./.venv/bin/python3 -m pytest

venv_nuke:
	rm -rf .venv

.venv:  # does nothing if .venv/ exists
	which virtualenv || sudo apt-get install python3-virtualenv

	DEB_PYTHON_INSTALL_LAYOUT='deb' \
	virtualenv ".venv"

	./.venv/bin/python3 -m pip install -r requirements.txt

