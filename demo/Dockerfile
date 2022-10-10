

FROM ubuntu:18.04
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python-pip -y
RUN apt-get install wget curl -y
SHELL ["/bin/bash","--login", "-c"] 
RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh 
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN echo ". /root/miniconda3/etc/profile.d/conda.sh" >> ~/.profile
RUN conda init bash
# RUN . /root/.bashrc && \
#     /root/miniconda3/bin/conda create -n py27 python=2.7 && \
# SHELL ["conda","run", "-n", "py27", "/bin/bash","-c"]
# RUN echo "checkpoint"
# CMD conda activate py27
# RUN pip2 install http://download.pytorch.org/whl/cu80/torch-0.2.0.post3-cp27-cp27mu-manylinux1_x86_64.whl
# COPY requirements.txt .
# RUN cat requirements.txt 
# RUN pip2 install -r requirements.txt
SHELL ["python", "--version"]

