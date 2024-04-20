install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black *.py app/*.py
lint:
	#flake8 or #pylint
	pylint --disable=R,C *.py app/*.py
run_test:
	#test
	python -m pytest -vv --cov=app testcases/*.py
build:
	# Build container
deploy:
	#deploy
all: install lint test deploy