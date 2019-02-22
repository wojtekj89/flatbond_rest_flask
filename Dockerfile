FROM python:3

LABEL maintainer="w.jarmakowski@gmail.com"

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]