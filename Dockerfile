FROM heroku/cedar:14
ENV DEBIAN_FRONTEND noninteractive
ENV DISTRO trusty

RUN echo "Setting the environmental variables..."
ENV PATH /app/.apt/usr/bin:$PATH

ENV LD_LIBRARY_PATH /app/.apt/usr/lib/x86_64-linux-gnu:/app/.apt/usr/lib/i386-linux-gnu:/app/.apt/usr/lib:$LD_LIBRARY_PATH
ENV LIBRARY_PATH /app/.apt/usr/lib/x86_64-linux-gnu:/app/.apt/usr/lib/i386-linux-gnu:/app/.apt/usr/lib:$LIBRARY_PATH
ENV INCLUDE_PATH /app/.apt/usr/include:$INCLUDE_PATH
ENV CPATH $INCLUDE_PATH
ENV CPPPATH $INCLUDE_PATH
ENV PKG_CONFIG_PATH /app/.apt/usr/lib/x86_64-linux-gnu/pkgconfig:/app/.apt/usr/lib/i386-linux-gnu/pkgconfig:/app/.apt/usr/lib/pkgconfig:$PKG_CONFIG_PATH
ENV OBT_TYPE tag-nostat-bm.sh

RUN useradd -d /app -m app

RUN echo "Configuring the container...."
RUN uname --all

RUN echo "Installing Apertium GnuPG key to /etc/apt/trusted.gpg.d/apertium.gpg"
RUN wget -q http://apertium.projectjj.com/apt/apertium-packaging.public.gpg -O /etc/apt/trusted.gpg.d/apertium.gpg

RUN echo "Creating /etc/apt/sources.list.d/apertium-nightly.list"
RUN echo "deb http://apertium.projectjj.com/apt/nightly $DISTRO main" > /etc/apt/sources.list.d/apertium-nightly.list \
    && apt-get update \
    && apt-get -o dir::cache=/tmp/apt install -y -d g++ libicu-dev subversion git cmake libboost-dev build-essential libgoogle-perftools-dev cg3 vim nano \
    && rm -rf /var/lib/apt/lists/* \
    && for DEB in $(ls -1 /tmp/apt/archives/*.deb); do echo "Installing $(basename $DEB)"; dpkg -x $DEB /app/.apt/; done \
    && apt-get -y clean

#RUN echo "Installing vislcg3...."
#RUN cd /tmp/ && svn co http://visl.sdu.dk/svn/visl/tools/vislcg3/trunk vislcg3 && cd vislcg3/ && ./cmake.sh && make -j3  && ./test/runall.pl && su && make install && ldconfig

#RUN echo "Running apt-get update..."
#RUN apt-get update && apt-get -y install cg3

RUN echo "All done - enjoy the packages! If you just want all core tools, do: sudo apt-get install apertium-all-dev"

RUN echo "Configuring the heroku container..."
USER app
WORKDIR /app/src

ENV HOME /app
ENV PORT 3000
ENV PATH /app/.heroku/python/bin:/tmp/python-pack/bin:$PATH
ENV STACK cedar-14
ENV PYTHONHOME /app/.heroku/python
ENV PYTHONPATH /app/
ENV DOCKER_BUILD 1

RUN mkdir -p /app/temp
RUN chmod 777 /app/temp
RUN mkdir -p /app/.heroku
RUN mkdir -p /tmp/app
RUN mkdir -p /app/src
RUN mkdir -p /app/.profile.d
RUN mkdir -p /tmp/python-pack
RUN mkdir -p /tmp/cache
RUN mkdir -p /tmp/environment


WORKDIR /app/src
WORKDIR /tmp/python-buildpack/bin

WORKDIR /app/
ONBUILD COPY . /app/

RUN git clone https://github.com/heroku/heroku-buildpack-python.git /tmp/python-pack --depth 1
ONBUILD RUN bash -l /tmp/python-pack/bin/compile /app /tmp/cache /app/.env

ONBUILD COPY . /app/src/

ONBUILD RUN echo "Cloning Oslo-Bergen-Tagger...."
ONBUILD RUN git clone https://github.com/domenicosolazzo/The-Oslo-Bergen-Tagger.git
ONBUILD RUN cd The-Oslo-Bergen-Tagger/ && git clone https://github.com/domenicosolazzo/OBT-Stat.git
ONBUILD RUN echo "Retrieving the tagger..."
ONBUILD RUN cd The-Oslo-Bergen-Tagger/ && cd bin/ && wget http://www.tekstlab.uio.no/mtag/linux64/mtag && chmod +x mtag
ONBUILD RUN cd The-Oslo-Bergen-Tagger/bin && pwd && ls -la

ONBUILD RUN mkdir -p /app/.profile.d
ONBUILD RUN echo "export LC_ALL=\"en_US.UTF-8\"" >> /app/.profile.d/python.sh
ONBUILD RUN echo "export LANG=\"en_US.UTF-8\"" >> /app/.profile.d/python.sh
ONBUILD RUN echo "export PATH=\"/app/.apt/usr/bin:$PATH\"" >> /app/.profile.d/python.sh
ONBUILD RUN echo "export LD_LIBRARY_PATH=\"/app/.apt/usr/lib/x86_64-linux-gnu:/app/.apt/usr/lib/i386-linux-gnu:/app/.apt/usr/lib:$LD_LIBRARY_PATH\"" >> /app/.profile.d/python.sh
ONBUILD RUN echo "export LIBRARY_PATH=\"/app/.apt/usr/lib/x86_64-linux-gnu:/app/.apt/usr/lib/i386-linux-gnu:/app/.apt/usr/lib:$LIBRARY_PATH\"" >> /app/.profile.d/python.sh
ONBUILD RUN echo "export INCLUDE_PATH=\"/app/.apt/usr/include:$INCLUDE_PATH\"" >> /app/.profile.d/python.sh
ONBUILD RUN echo "export CPATH=$INCLUDE_PATH" >> /app/.profile.d/python.sh
ONBUILD RUN echo "export CPPPATH=$INCLUDE_PATH" >> /app/.profile.d/python.sh
ONBUILD RUN echo "export PKG_CONFIG_PATH=\"/app/.apt/usr/lib/x86_64-linux-gnu/pkgconfig:/app/.apt/usr/lib/i386-linux-gnu/pkgconfig:/app/.apt/usr/lib/pkgconfig:$PKG_CONFIG_PATH\"" >> /app/.profile.d/python.sh
ONBUILD RUN echo "export OBT_TYPE=\"tag-nostat-bm.sh\"" >> /app/.profile.d/python.sh
ONBUILD EXPOSE 3000
