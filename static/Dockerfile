# declare what image to use
FROM python:latest

#docker build -f Dockerfile -t my-python-app .
#docker run -it my-python-app

# RUN mkdir -p /static_folder
# # COPY local folder to container Folder
# COPY ./static /static_folder
WORKDIR /app
COPY ./src .

#add to Docker Hub
#docker build -f Dockerfile -t ayaanmerchant/my-python-app:latest .
#docker push ayaanmerchant/my-python-app:latest

#python -m http.server 8000
#docker run -it -p 3000:8000 my-python-app
CMD ["python", "-m", "http.server", "8000"]
