# Version: 20230910
# Image name: quay.io/opencv-ci/opencv-ubuntu-22.04-riscv-scr

FROM ubuntu:22.04

RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    software-properties-common \
    cmake ccache ninja-build gpg-agent curl git htop man zip unzip vim wget ncdu mc nano time \
    file \
    && \
  add-apt-repository ppa:git-core/ppa && \
  apt-get install -y --no-install-recommends git && \
  rm -rf /var/lib/apt/lists/*

ADD https://dl.opencv.org/toolchains/202308-sc-dt.tar.gz /opt/
RUN cd /opt \
  && echo "c790b1287188ec88ffc685984f3aa548b8085017  202308-sc-dt.tar.gz" | sha1sum -c - \
  && tar -xvf 202308-sc-dt.tar.gz \
  && mv sc-dt/llvm rvv-llvm \
  && mv sc-dt/riscv-gcc riscv \
  && mv sc-dt/tools tools \
  && rm -rf sc-dt \
  && rm 202308-sc-dt.tar.gz

RUN \
  mkdir -p /home/ci/opencv /home/ci/opencv_contrib /home/ci/build && \
  git config --global --add safe.directory "*" && \
  git config --global user.email "opencv.ci" && \
  git config --global user.name "opencv.ci" && \
  git config --global pull.rebase false

COPY scripts/warnings-handling.py $HOME/scripts/warnings-handling.py

WORKDIR /home/ci

CMD bash
