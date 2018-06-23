# Python Flask Hello World

This is a very lightweight demo web application serving "Hello World" on TCP port 8080

I use it to demo application deployment to OpenShift on https://appuio.ch

# How to instantiate

* Web-GUI: "Add to project" -> search for "Python" -> Choose "Python" -> Next -> Version: 3.5, Name: flask-helloworld, Git Repository: https://github.com/arska/flask-helloworld.git -> Create -> Close

* CLI using source-to-image (s2i): oc new-app python:3.5~https://github.com/arska/flask-helloworld.git

* CLI using Dockerfile: oc new-app --strategy=docker https://github.com/arska/flask-helloworld.git
