FROM python:alpine

# Install required packages
RUN apk add --update --virtual=.build-dependencies alpine-sdk nodejs ca-certificates musl-dev gcc python-dev make cmake g++ gfortran libpng-dev freetype-dev libxml2-dev libxslt-dev
RUN apk add --update git

# Install Jupyter
RUN pip install jupyter
RUN pip install ipywidgets
RUN jupyter nbextension enable --py widgetsnbextension

# Install JupyterLab
RUN pip install jupyterlab && jupyter serverextension enable --py jupyterlab

# Additional packages for compatability (glibc)
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub && \
  wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.23-r3/glibc-2.23-r3.apk && \
  wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.23-r3/glibc-i18n-2.23-r3.apk && \
  wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.23-r3/glibc-bin-2.23-r3.apk && \
  apk add --no-cache glibc-2.23-r3.apk glibc-bin-2.23-r3.apk glibc-i18n-2.23-r3.apk && \
  rm "/etc/apk/keys/sgerrand.rsa.pub" && \
  /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8 C.UTF-8 || true && \
  echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \
  ln -s /usr/include/locale.h /usr/include/xlocale.h

# Optional Clean-up
#  RUN apk del glibc-i18n && \
#  apk del .build-dependencies && \
#  rm glibc-2.23-r3.apk glibc-bin-2.23-r3.apk glibc-i18n-2.23-r3.apk && \
#  rm -rf /var/cache/apk/*

ENV LANG=C.UTF-8

# Install Python Packages & Requirements (Done near end to avoid invalidating cache)
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install jupyterhub

# jupyter-spark lab extension 
# FIXME: esta cogiendo bien el /jupyter-spark local?? --> no puedo poner el server extension como /jupyter_spark!! me falla
ADD jupyter-spark jupyter-spark
RUN cd jupyter-spark && npm install && pip install -e . \
	&& jupyter labextension install --debug -y /jupyter-spark \
	&& jupyter labextension enable --debug -y  /jupyter-spark \
        && jupyter serverextension enable --py jupyter_spark 

RUN jupyter labextension install -y @jupyterlab/hub-extension


ADD spark-2.2.0 /opt/spark-2.2.0

RUN pip install findspark lxml

ENV SPARK_HOME=/opt/spark-2.2.0
ENV PATH=$SPARK_HOME/bin:$PATH 
ENV PYSPARK_DRIVER_PYTHON=jupyter
ENV PYSPARK_DRIVER_PYTHON_OPTS='notebook'

RUN apk add openjdk8 bash

# Expose Jupyter port & cmd
EXPOSE 8888
RUN mkdir -p /opt/app/data
#CMD jupyter lab --ip=* --port=8888 --no-browser --notebook-dir=/opt/app/data --allow-root
CMD jupyter labhub --ip='0.0.0.0' --port=8888 --no-browser --notebook-dir=/opt/app/data --allow-root 
#CMD jupyter lab --ip=* --port=8888 --notebook-dir=/opt/app/data --allow-root
