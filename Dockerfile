FROM python:2.7

WORKDIR /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY api.py /app
ENTRYPOINT [ "python", "api.py" ]