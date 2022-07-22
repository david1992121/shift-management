[![codecov](https://codecov.io/gh/david1992121/shift-management/branch/main/graph/badge.svg?token=6M23FDPOMY)](https://codecov.io/gh/david1992121/shift-management)
[![CI](https://github.com/david1992121/shift-management/actions/workflows/ci.yml/badge.svg)](https://github.com/david1992121/shift-management/actions/workflows/ci.yml)

# Work Planning Service

The backend API server for managing shifts

## Main Features

- DRF RestAPI
- MySQL
- Swagger API Documentation

## Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/david1992121/shift-management.git

Create and activate the virtualenv for your project, install the dependencies:

    $ pip install -r requirements.txt

Create .env file to set the environment variables for the project.

Then apply the migrations and seed the database with initial data:

    $ python manage.py migrate

You can now run the development server:

    $ python manage.py runserver

## API Guide

- User Register and Login

```
localhost:8000/api/v1/users/register
localhost:8000/api/v1/users/login
```

- Shift CRUD

```
localhost:8000/api/v1/works/shifts
```

- Swagger API documentation

The detail information can be checked using swagger API documentation on either of the following pages.

```
localhost:8000/redoc
localhost:8000/swagger
```
