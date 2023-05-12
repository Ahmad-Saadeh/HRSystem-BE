# FROM python:3.9
# ENV DockerHOME=/Home/Desktop/HR-system-BE
# RUN mkdir -p $DockerHOME
# WORKDIR $DockerHOME
# COPY ../venv ./venv
# ENV PATH="/app/venv/bin:$PATH"
# COPY ./requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . .
# EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# COPY ./hr_system/venv ./venv
# COPY ./hr_system/requirements.txt .
# base image  
FROM python:3.9
# setup environment variable  
ENV DockerHOME=/Home/Desktop/HR-system-BE/hr_system 

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . $DockerHOME  
# run this command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs  
EXPOSE 8000  
# start server  
CMD python manage.py runserver  