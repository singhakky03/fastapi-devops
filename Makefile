install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
		python -m textblob.download_corpora
format:
	#format code
	black *.py app/*.py
lint:
	#flake8 or #pylint
	pylint --disable=R,C *.py app/*.py testcases/*.py
run_test:
	#test
	python -m pytest -vv --cov=app --cov=main testcases/*.py
build:
	# Build container
	docker build -t deploy-fastapi .
deploy:
	#deploy
all: install lint test deploy