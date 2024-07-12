FROM python:3.9-alpine3.15

WORKDIR /app

RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev

RUN pip install mysql-connector-python

COPY insert_students.py .

CMD ["python","insert_students.py"]
