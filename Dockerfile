from gcr.io/tensorflow/tensorflow:latest-py3
#RUN apt-get update
#RUN apt-get install -y python3-pip
RUN pip install flask numpy scipy pillow requests
ENV FLASK_APP=request_handler.py
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
