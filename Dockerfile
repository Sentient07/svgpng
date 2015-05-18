FROM centos:7

MAINTAINER Jack Twilley <mathuin@gmail.com>

EXPOSE 8000

RUN yum -y update && yum -y install \
    epel-release

RUN yum -y update && yum -y install \
    bzip2 \
    cairo-devel \
    gcc \
    gcc-c++ \
    libffi \
    libffi-devel \
    nodejs \
    npm \
    python-devel \
    python-setuptools \
    tar

# RUN npm -g install phantomjs

RUN yum -y install git make flex bison gperf ruby \
    openssl-devel freetype-devel fontconfig-devel libicu-devel \
    sqlite-devel libpng-devel libjpeg-devel

RUN git clone git://github.com/ariya/phantomjs.git && \
    cd phantomjs && \
    git checkout 1.9 && \
    git reset --hard && \
    ./build.sh --confirm && \
    cp bin/phantomjs /usr/bin/phantomjs

RUN npm -g install casperjs

RUN easy_install pip

WORKDIR /opt/svgpng

COPY ./requirements.txt /opt/svgpng/requirements.txt
RUN pip install -r requirements.txt
COPY . /opt/svgpng
#RUN cp /opt/svgpng/settings.py.dist /opt/svgpng/settings.py

WORKDIR /opt/svgpng/svgpng

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
