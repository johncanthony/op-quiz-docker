FROM alpine:3.6


WORKDIR /app

COPY requirements.txt ./
COPY app.py ./


RUN apk add --update \
        python \
        python-dev \
        py-pip \
        build-base



RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8081

CMD ["python","./app.py"]




