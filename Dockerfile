FROM docker.io/python:3.10

ENV APP_DIR=/usr/local/bin/message-writer
RUN mkdir $APP_DIR

# Copy pip to use pinned down versions
COPY requirements_stable.txt      $APP_DIR/

# set working directory
WORKDIR $APP_DIR

# change file ownership
RUN chmod -R +x $APP_DIR

# copy main file
COPY . $APP_DIR

RUN pip install -r requirements_stable.txt && \
    rm -r requirements_stable.txt
