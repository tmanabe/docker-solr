FROM solr:9.2.1

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root
RUN apt-get update
RUN apt-get install -y python3

RUN curl https://bootstrap.pypa.io/get-pip.py | python3
RUN pip3 install -U pip
RUN pip3 install torch transformers==4.31.0 sentencepiece fugashi unidic-lite

ARG python=/Users/owner/.pyenv/versions/3.9.16/bin/python
RUN mkdir -p /Users/owner && chown solr /Users/owner
RUN mkdir -p /home/solr && chown solr /home/solr

ARG policy=/opt/solr-9.2.1/server/etc/security.policy
RUN echo "grant {" >> ${policy}
RUN echo "  permission java.io.FilePermission \"${python}\", \"execute\";" >> ${policy}
RUN echo "};" >> ${policy}

USER solr
RUN mkdir -p `dirname ${python}`
RUN ln -s `which python3` ${python}
