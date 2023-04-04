FROM gitpod/workspace-full:latest

USER gitpod

# Install Python 3.10
RUN sudo apt-get update \
    && sudo apt-get install -y software-properties-common \
    && sudo add-apt-repository -y ppa:deadsnakes/ppa \
    && sudo apt-get update \
    && sudo apt-get install -y python3.10 python3.10-venv python3.10-dev

# Install PySpark
RUN sudo apt-get update \
    && sudo apt-get install -y openjdk-11-jdk \
    && export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/ \
    && export PATH=$JAVA_HOME/bin:$PATH \
    && python3.10 -m pip install --upgrade pip \
    && python3.10 -m pip install pyspark
