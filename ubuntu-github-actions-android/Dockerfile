FROM ubuntu:20.04

USER root

ENV DEBIAN_FRONTEND noninteractive

RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends \
    build-essential ccache ninja-build \
    python3 python3-pip curl unzip \
    openjdk-8-jdk openjdk-8-jre \
    && \
  rm -rf /var/lib/apt/lists/*

RUN \
  dpkg --add-architecture i386 && \
  apt-get update && \
  apt-get install -y --no-install-recommends \
    libncurses5:i386 libstdc++6:i386 zlib1g:i386 \
    && \
  rm -rf /var/lib/apt/lists/*

RUN curl -o /tmp/gradle-5.6.4-bin.zip https://downloads.gradle-dn.com/distributions/gradle-5.6.4-bin.zip && \
    ls -al /tmp/ && \
    unzip -d /opt/gradle /tmp/gradle-5.6.4-bin.zip && \
    rm /tmp/gradle-5.6.4-bin.zip

ENV ANDROID_HOME="/usr/local/android-sdk"

RUN cd ~ && mkdir "$ANDROID_HOME" .android \
    && cd "$ANDROID_HOME" \
    && curl -o sdk.zip "https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip" \
    && unzip sdk.zip \
    && rm sdk.zip \
    && echo "y\n" > /tmp/yes \
    && $ANDROID_HOME/tools/bin/sdkmanager "platform-tools" < /tmp/yes


RUN cd "$ANDROID_HOME" && ./tools/bin/sdkmanager "build-tools;28.0.3" < /tmp/yes
RUN cd "$ANDROID_HOME" && ./tools/bin/sdkmanager "build-tools;29.0.2" < /tmp/yes
RUN cd "$ANDROID_HOME" && ./tools/bin/sdkmanager "platforms;android-21" < /tmp/yes
RUN cd "$ANDROID_HOME" && ./tools/bin/sdkmanager "platforms;android-24" < /tmp/yes
RUN cd "$ANDROID_HOME" && ./tools/bin/sdkmanager "platforms;android-26" < /tmp/yes
RUN cd "$ANDROID_HOME" && ./tools/bin/sdkmanager "ndk;18.1.5063045" < /tmp/yes
RUN cd "$ANDROID_HOME" && ./tools/bin/sdkmanager "ndk;21.1.6352462" < /tmp/yes
RUN cd "$ANDROID_HOME" && ./tools/bin/sdkmanager "ndk;22.1.7171670" < /tmp/yes
RUN cd "$ANDROID_HOME" && ./tools/bin/sdkmanager "cmake;3.6.4111459" < /tmp/yes

RUN python3 -m pip install cmake

RUN useradd ci -m -s /bin/bash -G users,dialout
USER ci

ENV GRADLE_HOME=/opt/gradle/gradle-6.6.1
ENV GRADLE_OPTS="-Dorg.gradle.daemon=false -Dorg.gradle.workers.max=2"
ENV PATH=$GRADLE_HOME/bin:$PATH
ENV ANDROID_HOME="/usr/local/android-sdk"
ENV ANDROID_NDK_HOME="/usr/local/android-sdk/ndk/18.1.5063045"

ENTRYPOINT bash
