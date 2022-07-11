# Version: 20220711
# Image name: quay.io/opencv-ci/opencv-docs

FROM ubuntu:20.04

RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    software-properties-common \
    curl git htop man zip unzip vim wget ncdu mc nano time \
    file \
    && \
  add-apt-repository ppa:git-core/ppa && \
  apt-get install -y --no-install-recommends git && \
  rm -rf /var/lib/apt/lists/*

RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    cmake build-essential \
    doxygen doxygen-latex graphviz \
    p7zip-full \
    pylint flake8 \
    python-bs4 \
    python3-bs4 \
    ant ant-optional default-jdk \
    && \
  rm -rf /var/lib/apt/lists/*

RUN useradd ci -m -s /bin/bash -G users

USER ci

RUN \
  cd $HOME && \
  mkdir opencv opencv_contrib build && \
  git config --global --add safe.directory "*" && \
  git config --global user.email "opencv.ci" && \
  git config --global user.name "opencv.ci" && \
  git config --global pull.rebase false

ENTRYPOINT bash
