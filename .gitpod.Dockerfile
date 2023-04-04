FROM gitpod/workspace-full:latest

USER gitpod

# Install PySpark
RUN sudo apt-get update \
    && sudo apt-get install -y openjdk-11-jdk \
    && export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/ \
    && export PATH=$JAVA_HOME/bin:$PATH \
    && python -m pip install pyspark \
    && python -m pip install pytest
