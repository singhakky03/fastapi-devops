FROM python:3.9.6-slim-buster

RUN mkdir -p /api
COPY . main.py /api/
WORKDIR /api
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["main.py"]
ENTRYPOINT ["python"]