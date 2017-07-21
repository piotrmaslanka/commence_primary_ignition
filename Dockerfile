FROM python:2.7.13

RUN pip install requests
ADD commence_primary_ignition.py /root/commence_primary_ignition.py

CMD ["/root/commence_primary_ignition.py"]
