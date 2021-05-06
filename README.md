

#WEBFORTUNE

![python-app.yml](https://github.com/github/qhussey32/webfortune/actions/workflows/python-app.yml/badge.svg)


In this program the user will communicatewith the command line through the webserver to get fortunes, use cowsay, or both.

HOW TO USE WITH DOCKER.

To build the application you need docker installed. After that to creat your image run the comman 'docker build -t <repository>. The repository is what you want your docker image to go by.


To run it use the command docker -d -p <port>:5000 <repository> where <port> is the one you want t obind, 5000 is the conatainer port that its bound to while repository is the identifier used previously to build it.

To stop the docker container use docker ps. Then look for your unique identifier and run command docker stop.

LOCAL USE

follow these steps.

python3 -m virtualenv env

source env/bin/activate

pip3 install -r requirements.text

HOW TO RUN

To run the webserver and type FLASK_APP=appserver.py flask run --host=0.0.0.0. Then in the browser of your choice type <your_ip_address>:5000.
