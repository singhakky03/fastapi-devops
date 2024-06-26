[![Python Fast API application with Github Actions](https://github.com/singhakky03/fastapi-devops/actions/workflows/pipeline.yml/badge.svg)](https://github.com/singhakky03/fastapi-devops/actions/workflows/pipeline.yml)

# fastapi-devops
Building a fast api microservices and deploying the application using github actions and aws codebuild

## Scaffold Diagram 
![scaffold](https://github.com/singhakky03/fastapi-devops/assets/1935427/c96ac983-4b2d-4aa5-9d58-8389d54313dd)

1. Create a Python Virtual Environment `python3 -m venv ~/.venv` or `virtualenv ~/.venv`  and Activate source venv with command `source .venv/bin/activate`
2. Create scaffold empty files: `Makefile`, `requirements.txt`, `main.py`, `Dockerfile`, `app/__init__.py` and `app/core.py`
3. Populate `Makefile`
4. Steps added for Continious Integration(github workflows) i.e code formatting, lint errors
5. Build CLI tool using python fire library `./cli-fire.py --help` to test wiki logic
6. Add Fast API and uvicorn library in `requirement.txt` and api logic in `main.py`
7. Add `textblob` NLP library to process textal data, using it add noun phrase extraction task.