FROM python:3.6
ADD requirements.txt /tmp/requirements.txt
ADD .aws_credentials /etc/boto.cfg
RUN sed 's/default/Credentials/' -i /etc/boto.cfg
RUN pip install -r /tmp/requirements.txt
ADD . /code
WORKDIR /code
RUN adduser --uid 1000 --disabled-password --gecos '' wisdomwolf && chown -R wisdomwolf:wisdomwolf /code
CMD ["ipython","-i",  "smartify_daemon.py"]
