FROM python:alpine
RUN pip install requests
RUN pip install beautifulsoup4
RUN mkdir /opt/project2

COPY . /opt/project2

ENTRYPOINT python /opt/project2/file1.py