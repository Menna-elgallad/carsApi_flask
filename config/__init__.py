# -*- coding: utf-8 -*-

from smart_getenv import getenv


DEBUG = getenv('DEBUG', default=True, type=bool)

PROJECT_NAME = LOGGER_NAME = 'cars'
SECRET_KEY = getenv('SECRET_KEY', default='cars-test')
JWT_SECRET_KEY=getenv('JWT_SECRET_KEY', default='cars-test')
JWT_ACCESS_TOKEN_EXPIRES=getenv('JWT_ACCESS_TOKEN_EXPIRES',default=219000)
JWT_REFRESH_TOKEN_EXPIRES=getenv('JWT_REFRESH_TOKEN_EXPIRES',default=30)

SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI', default='postgresql://postgres:1234@localhost:5432/cars')
SQLALCHEMY_TRACK_MODIFICATIONS = getenv('SQLALCHEMY_TRACK_MODIFICATIONS', default=True, type=bool)
