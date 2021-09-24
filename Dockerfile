FROM python:3.8

RUN apt-get update && \
    apt-get install -y ca-certificates && \
    apt-get clean

RUN pip install requests satella>=2.17.21
WORKDIR /root
ADD commence_primary_ignition.py /root/commence_primary_ignition.py

CMD ["python", "commence_primary_ignition.py"]
