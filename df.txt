# Top level build args
ARG build_for=linux/x86-64

# base image (abstract)
FROM --platform=$build_for public.ecr.aws/lambda/python:3.10 as base

# N.B. The refs updated automagically every release via bumpversion
ARG dbt_core_ref=dbt-core@v1.8.0b1
ARG dbt_snowflake_ref=dbt-snowflake@v1.8.0b1

# System setup
#
RUN yum update -y \
  && yum install -y \
    git \
    ssh \
    make \
    gcc \
    postgresql-devel \
  && yum clean all

# Env vars
ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8
ENV DBT_PROFILES_DIR=${LAMBDA_TASK_ROOT}
ENV DBT_PROJECT_DIR=${LAMBDA_TASK_ROOT}
# Update python
RUN python -m pip install --upgrade pip setuptools wheel --no-cache-dir

# Install dbt-core and dbt-snowflake
RUN python -m pip install --no-cache-dir "git+https://github.com/dbt-labs/${dbt_core_ref}#egg=dbt-core&subdirectory=core"
RUN python -m pip install --no-cache-dir "git+https://github.com/dbt-labs/${dbt_snowflake_ref}#egg=dbt-snowflake"

# Copy app.py into the Docker image
#WORKDIR /usr/app
COPY app.py ${LAMBDA_TASK_ROOT}
COPY dbt_project.yml ${LAMBDA_TASK_ROOT}
COPY profiles.yml ${LAMBDA_TASK_ROOT}
COPY . /tmp/dbt

# Set docker basics
#WORKDIR /var/task
CMD [ "app.lambda_handler" ]
