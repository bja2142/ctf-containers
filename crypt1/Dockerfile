FROM php:apache

RUN apt-get update -y && apt-get install -y libpng-dev

RUN docker-php-ext-install gd

COPY service/src/ /var/www/html
