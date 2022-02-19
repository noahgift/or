install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_hello.py

format:
	black greedy-random-tsp.py
lint:
	pylint --disable=R,C greedy-random-tsp.py

all: install lint test