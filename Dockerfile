# jupyter base image
FROM ghcr.io/diogenesanalytics/scipy-notebook:master AS jupyter

# change to dir for storing files
WORKDIR /usr/local/src/blog_template

# get files
COPY --chown=${NB_UID}:${NB_GID} pyproject.toml poetry.lock ./

# now install poetry deps
RUN poetry config virtualenvs.create false && \
    poetry install --with utils --no-root

# switch back to default Jupyter user and workdir
USER ${NB_USER}
WORKDIR "${HOME}"

# test base image
FROM ghcr.io/diogenesanalytics/python-testing:master AS testing

# define the build arguments
ARG DCKRSRC

# install necessary dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      bash \
      git \
      gnupg \
      make \
      rsync \
      tree \
      wget \
      unzip \
      ruby \
      ruby-dev \
      build-essential \
    && rm -rf /var/lib/apt/lists/*

# Add the safe.directory config for Git
RUN git config --global --add safe.directory '*'

# Install Jekyll (no need for Bundler or a Gemfile)
RUN gem install jekyll -v 4.3.3

# download and install Google Chrome
RUN mkdir -p /etc/apt/keyrings \
    && wget -qO- https://dl.google.com/linux/linux_signing_key.pub \
       | gpg --dearmor -o /etc/apt/keyrings/google-linux-signing-key.gpg \
    && echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/google-linux-signing-key.gpg] https://dl.google.com/linux/chrome/deb/ stable main" \
       > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# set workdir
WORKDIR ${DCKRSRC}

# copy source
COPY . .

# install poetry deps (THIS replaces requirements.txt)
RUN poetry install --with utils,dev --no-root -vvv

# get chromedriver (sbase installed by requirements.txt)
RUN sbase install chromedriver

# create unique user
RUN useradd -u 1000 -m -d /home/tester tester
RUN mkdir -p /home/tester/.cache
RUN chown -R tester:tester /home/tester

# Mark the directory safe for git
RUN git config --global --add safe.directory ${DCKRSRC}
