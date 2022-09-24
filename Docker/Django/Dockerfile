FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV WEB_ROOT /var/www/app
RUN mkdir -p ${WEB_ROOT}
WORKDIR ${WEB_ROOT}
ADD ./requirements.txt ${WEB_ROOT}
RUN pip install -r requirements.txt
ADD ./ ${WEB_ROOT}/
