image=protected_moonshots_restapi
tag=latest


build:
		docker build -t $(image) .

push: 

run: 
		docker run -p 8080:5000 $(image):$(tag)