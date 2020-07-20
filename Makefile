venv: requirements.txt
	python3 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt
	touch venv

run: venv
	xdg-open http://localhost:8088
	venv/bin/python motepix.py

dev: venv
	venv/bin/python motepix.py
