FROM heroku/cedar:14

RUN useradd -d /app -m app

RUN echo "Configuring the container...."
RUN uname --all

RUN echo "Updating the packages"
RUN apt-get update
RUN apt-get -y clean

RUN echo "Installing g++, libicu-dev, subversion cmake libboost-dev build-essential...."
RUN apt-get -y install g++ libicu-dev subversion cmake libboost-dev build-essential

RUN echo "Installing libgoogle-perftools-dev...."
RUN apt-get -y install libgoogle-perftools-dev

RUN echo "Installing Git..."
RUN apt-get -y install git

RUN echo "Setting the environmental variables..."
ENV PATH /app/.apt/usr/bin:$PATH
ENV LD_LIBRARY_PATH /app/.apt/usr/lib/x86_64-linux-gnu:/app/.apt/usr/lib/i386-linux-gnu:/app/.apt/usr/lib:$LD_LIBRARY_PATH
ENV LIBRARY_PATH /app/.apt/usr/lib/x86_64-linux-gnu:/app/.apt/usr/lib/i386-linux-gnu:/app/.apt/usr/lib:$LIBRARY_PATH
ENV INCLUDE_PATH /app/.apt/usr/include:$INCLUDE_PATH
ENV CPATH $INCLUDE_PATH
ENV CPPPATH $INCLUDE_PATH
ENV PKG_CONFIG_PATH /app/.apt/usr/lib/x86_64-linux-gnu/pkgconfig:/app/.apt/usr/lib/i386-linux-gnu/pkgconfig:/app/.apt/usr/lib/pkgconfig:$PKG_CONFIG_PATH

RUN echo "Installing vislcg3...."
RUN cd /tmp/
RUN svn co http://visl.sdu.dk/svn/visl/tools/vislcg3/trunk vislcg3
RUN cd vislcg3/ && ./cmake.sh
RUN cd vislcg3/ && make -j3
RUN cd vislcg3/ && ./test/runall.pl && make install && ldconfig


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

RUN echo "Cloning Oslo-Bergen-Tagger...."
RUN git clone https://github.com/domenicosolazzo/The-Oslo-Bergen-Tagger.git
RUN cd The-Oslo-Bergen-Tagger/ && git clone https://github.com/domenicosolazzo/OBT-Stat.git
RUN cd The-Oslo-Bergen-Tagger/ && cp ../bin/mtag-linux64 . && mv mtag-linux64 mtag && chmod +x mtag

ONBUILD EXPOSE 3000
