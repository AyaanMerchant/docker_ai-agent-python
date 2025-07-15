# declare what image to use
FROM python:latest

#create python virtual environment
#isolate python from system level python
RUN python -m venv /opt/venv/

#activate virtual environment
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
COPY ./src .
COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
