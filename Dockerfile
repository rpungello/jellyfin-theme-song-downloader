FROM python:3

ARG VERSION=1.0.0
ENV APP_VERSION=${VERSION}

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]