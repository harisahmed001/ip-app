FROM python:3.10-slim-buster
# Making a seperate layer wouldnt install requirements on each build
COPY requirements.txt /application/
WORKDIR /application
RUN pip install -r requirements.txt
COPY ./ /application/
ENTRYPOINT [ "./entrypoint.sh" ]
