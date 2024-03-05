FROM python:3.11.4-slim-bullseye

# Install Fortran compiler and BLAS, LAPACK libraries
RUN apt-get update && apt-get install -y \
    gfortran \
    libblas-dev \
    liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install numpy fmodpy

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the necessary files for Fortran build script
COPY tchlux tchlux
COPY mypackage/__init__.py mypackage/__init__.py
COPY compile_fortran.py compile_fortran.py

RUN ["python", "./compile_fortran.py"]

# Copy the rest of the application files
COPY . .