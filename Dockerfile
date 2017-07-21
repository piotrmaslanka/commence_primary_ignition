FROM python:2.7.13

RUN pip install requests
ADD commence_primary_ignition.py /commence_primary_ignition.py

CMD ["/usr/bin/python", "/commence_primary_ignition.py"]
