Welcome to Online Shopper

In this project the user is able to purchase items from a
selection of products, register and login.

SETUP:
Either install the project or clone it via git
using git clone:

git clone https://github.com/KhutsoJ/online-shopper.git
cd online-shopper

Create a virtual environment to store all your packages:

python -m venv venv

Install project requirements using: pip install -r requirements.txt

Once packages are installed, run "python manage.py migrate" then 
"python manage.py runserver" to start the project. To view the
project, click the link in the terminal.

from there, you can play around with the project, register or login,
add products from the cart and process your payment at checkout :D

Running the Docker container:
To build the docker image: docker build -t online-shopper .
To run the container: docker run -d -p 8000:8000 online-shopper

Viewing the Sphinx documentation:
Go into the docs directory: cd docs
Build the html document: ".\make html" or "make html"
Open the index file in: docs/_build/html/index.html
