# Version: 20220726
# Image name: quay.io/opencv-ci/opencv-ubuntu-14.04

FROM ubuntu:14.04

RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    software-properties-common \
    curl zip git unzip wget rsync mc nano time \
    file \
    && \
  rm -rf /var/lib/apt/lists/*

RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    cmake \
    build-essential \
    ccache \
    python \
    python-dev \
    python-numpy \
    python3 \
    python3-dev \
    python3-numpy \
    zlib1g-dev \
    libjpeg-dev \
    libpng12-dev \
    libtiff5-dev \
    libjasper-dev \
    libgtk2.0-dev \
    libavformat-dev \
    libavformat-extra-54 \
    libswscale-dev \
    ant \
    ant-optional \
    openjdk-7-jdk \
    openjdk-7-jre \
    hdf5-tools \
    hdf5-helpers \
    libhdf5-7 \
    libhdf5-dev \
    libhdf5-serial-dev \
    libleptonica-dev \
    liblept4 \
    tesseract-ocr \
    tesseract-ocr-eng \
    libtesseract-dev \
    libtesseract3 \
    libusb-dev \
    libusb-1.0.0-dev \
    libudev-dev \
    libgdal-dev \
    libvtk6-dev \
    libgoogle-glog-dev \
    libatlas-base-dev \
    libeigen3-dev \
    libsuitesparse-dev \
    liblapacke-dev \
    libgdcm2-dev \
    xvfb \
    && \
  apt-get clean

RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends \
    libva-dev \
    && \
  rm -rf /var/lib/apt/lists/*

# Self-hosted runner UID is 1000
RUN useradd ci -m -s /bin/bash -G users --uid=1000

USER ci

RUN \
  mkdir $HOME/opencv $HOME/opencv_contrib $HOME/build && \
  git config --global --add safe.directory "*" && \
  git config --global user.email "opencv.ci" && \
  git config --global user.name "opencv.ci" && \
  git config --global pull.rebase false

# Run docker build from the root directory of the repository
COPY scripts/warnings-handling.py /home/ci/scripts/warnings-handling.py

CMD bash
