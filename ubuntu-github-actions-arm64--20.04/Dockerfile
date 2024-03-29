# Version: 20230413
# Image name: quay.io/opencv-ci/opencv-ubuntu-20.04-arm64

FROM ubuntu:20.04

# reportlab, svglib: for https://github.com/opencv/opencv/pull/23363
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    software-properties-common \
    cmake build-essential ccache ninja-build wget curl zip unzip rsync mc nano time file\
    python2-dev python-numpy \
    python3-dev python3-numpy python3-setuptools python3-pip\
    zlib1g-dev libjpeg-dev libpng-dev libtiff5-dev libopenjp2-7-dev \
    libgtk-3-dev \
    libavcodec-dev libavformat-dev libswscale-dev \
    libtbb-dev libtbb2 \
    ant ant-optional default-jdk \
    hdf5-tools libhdf5-dev \
    libleptonica-dev liblept5 tesseract-ocr tesseract-ocr-eng libtesseract-dev libtesseract4 \
    libusb-dev libusb-1.0.0-dev libudev-dev \
    libgdal-dev \
    libvtk7-dev \
    libgoogle-glog-dev \
    libatlas-base-dev libeigen3-dev libsuitesparse-dev liblapacke-dev \
    xvfb \
    pkg-config && \
  add-apt-repository ppa:git-core/ppa && \
  apt-get install -y --no-install-recommends git && \
  apt-get clean && python3 -m pip install --upgrade pip && \
  pip install requests pylint==2.4.4 reportlab svglib && pip cache purge

RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    libva-dev \
    libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev \
        gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-libav \
    libopenni2-dev \
    libdc1394-22-dev \
    libgphoto2-dev \
    && \
  rm -rf /var/lib/apt/lists/*

# Self-hosted runner UID is 1000
RUN useradd ci -m -s /bin/bash -G users --uid=1004

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
