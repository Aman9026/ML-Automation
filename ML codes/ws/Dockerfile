FROM centos
RUN yum install python36 -y
RUN python3 --version
RUN pip3 --version
RUN pip3 install -U virtualenv
RUN virtualenv --version
RUN virtualenv --system-site-packages -p python3 ./machinelearning
RUN source ./machinelearning/bin/activate
RUN pip3 install --upgrade pip
RUN pip install --upgrade tensorflow-gpu
RUN pip install scikit-learn
RUN pip install pillow
RUN pip install h5py
RUN pip install keras
RUN pip install numpy
COPY /mlwork/ /home/
RUN chmod +x /home/autoadd.sh
ENTRYPOINT [ "python3", "/home/autoadd.sh"]

