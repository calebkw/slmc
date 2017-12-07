from gcr.io/tensorflow/tensorflow:latest
RUN pip install flask numpy scipy pillow requests
ENV FLASK_APP=test.py