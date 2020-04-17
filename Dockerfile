FROM python
RUN  mkdir -p  /var/test
COPY test.py /var/test/test.py
RUN  pip install requests
CMD  ["python","/var/test/test.py"]
