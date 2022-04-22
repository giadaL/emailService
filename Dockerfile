#
FROM python:3.10

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./src /code/src
COPY ./src/config /code/src/config

#
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0"]