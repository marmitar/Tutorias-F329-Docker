FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && apt-get install -y \
        wget curl openssh-client git texlive-full latexmk \
        python3 python3-numpy python3-scipy python3-pandas \
        python3-matplotlib python3-pygments python3-xlrd \
    && apt-get --purge remove -y .\*-doc$ \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
    && ln -s $(which python3) $(dirname $(which python3))/python
