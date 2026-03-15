FROM geopython/pygeoapi:latest
COPY my.config.yml /pygeoapi/local.config.yml
COPY my_processes/ /pygeoapi/my_processes/
ENV PYTHONPATH=/pygeoapi