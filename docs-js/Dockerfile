# Version: 20220711
# Image name: quay.io/opencv-ci/opencv-docs-js

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

ENV EMSDK_VERSION=1.39.0-upstream
ENV EMSDK_DIR=/opt/emsdk-portable
ENV EMSDK_CACHE_DIR=/opt/build-worker/emsdk-${EMSDK_VERSION}

RUN \
  /bin/bash -c "mkdir -p ${EMSDK_DIR} && \
    cd ${EMSDK_DIR} && \
    git rev-parse HEAD || (rm -rf ./.git && git clone https://github.com/juj/emsdk.git .) && \
    git reset --hard || true && \
    git clean -f -d || true && \
    git fetch origin && \
    git checkout -B main origin/main && \
    git rev-parse HEAD && \
    ./emsdk list && \
    ./emsdk install ${EMSDK_VERSION} && \
    ./emsdk activate ${EMSDK_VERSION} && \
    source ./emsdk_env.sh && \
    mkdir -p ./.home && \
    cp -rp ./.em* ./.home/ && \
    # python script (opencv/platforms/js/build_js.py) has shebang and required hardly python
    ln -s /usr/bin/python3 /usr/bin/python"

RUN \
  useradd ci -m -s /bin/bash -G users && \
  chown -R ci:ci ${EMSDK_DIR}

USER ci

RUN \
  cd $HOME && \
  mkdir opencv opencv_contrib build scripts && \
  git config --global --add safe.directory "*" && \
  git config --global user.email "opencv.ci" && \
  git config --global user.name "opencv.ci" && \
  git config --global pull.rebase false

COPY scripts/pack_docs.py /home/ci/scripts/

ENV PATH=${EMSDK_DIR}:${EMSDK_DIR}/upstream/emscripten:${EMSDK_DIR}/node/14.18.2_64bit/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV EMSDK=${EMSDK_DIR}
ENV EM_CONFIG=${EMSDK_DIR}/.emscripten
ENV EM_CACHE=${EMSDK_DIR}/upstream/emscripten/cache
ENV EMSDK_NODE=${EMSDK_DIR}/node/14.18.2_64bit/bin/node
ENV EMSCRIPTEN ${EMSDK_DIR}/upstream/emscripten

ENTRYPOINT bash
