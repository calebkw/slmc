from gcr.io/tensorflow/tensorflow:latest
RUN pip install flask numpy scipy pillow
ENV FLASK_APP=test.py