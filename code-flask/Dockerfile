FROM python:3.7.1-slim-stretch
RUN pip install -U Flask ptvsd
ADD code /code

ENTRYPOINT ["python", "/code/server.py"]