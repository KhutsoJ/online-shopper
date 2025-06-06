FROM python:latest

WORKDIR /app

# copies requirements.txt from computer to the image and name it requirements
COPY requirements.txt requirements.txt

# install the requirements
RUN pip3 install -r requirements.txt

# copies all files from same directory
COPY . .

EXPOSE 8000

# start server at port 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
