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
run:
	#run docker
	docker run -p 127.0.0.1:8080:8080 ec4ce3a1d25f
deploy:
	#deploy
all: install lint run_test build run deploy