# Dockerfile to install ten-rules-jupyter on Cyverse/VICE
FROM discoenv/jupyter-lab:beta

USER root

# Update the packages
RUN apt-get update \
    && apt-get clean \
    && rm -rf /usr/lib/apt/lists/*

USER jovyan

WORKDIR /home/jovyan

# Clone repository
RUN git clone https://github.com/jupyter-guide/ten-rules-jupyter 

# Install dependencies
RUN pip install -r ./ten-rules-jupyter/requirements.txt

COPY entry.sh /bin
RUN mkdir /home/jovyan/.irods

ENTRYPOINT ["/bin/entry.sh"]
