

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
RUN conda create -n py27 python=2.7
RUN echo "source activate py27" > ~/.bashrc
RUN echo "Switched to Python 2.7"
RUN pip install https://download.pytorch.org/whl/cpu/torch-1.4.0%2Bcpu-cp27-cp27mu-linux_x86_64.whl
COPY requirements.txt .
RUN cat requirements.txt 
RUN pip install -r requirements.txt
RUN conda install -c rdkit rdkit=2018.09.1
RUN apt-get install libxrender1 -y
RUN apt install -y libsm6 libxext6 libxrender-dev 
WORKDIR /app
COPY ./ ./
WORKDIR /app/model
RUN echo "python app.py" >> ~/.bashrc
