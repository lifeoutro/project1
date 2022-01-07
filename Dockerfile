FROM python:alpine
RUN pip install requests
RUN pip install beautifulsoup4
RUN mkdir -p /opt/project2/logs

COPY . /opt/project2

ENTRYPOINT python /opt/project2/file1.py >> /opt/project2/logs/dockerrun