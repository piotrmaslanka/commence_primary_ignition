FROM python:2.7.13

RUN pip install requests
ADD commence_primary_ignition.py /commence_primary_ignition.py

ENTRYPOINT ["/usr/bin/python2.7"]
CMD ["/commence_primary_ignition.py"]
