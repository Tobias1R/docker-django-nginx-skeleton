FROM python:3.10.0
## Install dependencies
RUN apt-get update \
    # System stuff    
    && apt-get --no-install-recommends install -y ca-certificates nginx gettext-base \ 
    # PIP build dependencies
    gcc libssl-dev \   
    # Cleanup after installation
    && apt-get clean -y \
    && apt-get autoclean -y \
    && apt-get autoremove -y \
    && rm -fr /var/lib/apt/lists/* \
    # Create basic project structure
    && mkdir -p /app/project/assets/ /app/logs /app/tmp/

WORKDIR /app/

# requirements.txt (PIP) files to the image
ADD project/requirements.txt /app/requirements.txt

# Python dependencies
RUN pip install -U -r /app/requirements.txt --no-cache-dir

ADD . /app/

RUN python3 manage.py collectstatic --noinput -v0

RUN chmod -R 777 logs

# NGINX
# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

ADD docker/production/nginx/nginx.conf /etc/nginx/sites-enabled/project

RUN mkdir -p /var/www/app

RUN useradd uwsgi

RUN chown -R uwsgi:www-data /var/www/app 

RUN chown -R uwsgi:www-data /app 

RUN rm -f /etc/nginx/sites-enabled/default

EXPOSE 80