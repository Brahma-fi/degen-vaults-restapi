image=protected_moonshots_restapi
tag=latest


build:
		docker build -t $(image) .

push: 
		docker tag protected_moonshots_restapi:latest 820675130125.dkr.ecr.us-east-2.amazonaws.com/protected_moonshots_restapi:latest
		docker push 820675130125.dkr.ecr.us-east-2.amazonaws.com/protected_moonshots_restapi:latest

run: 
		docker run -p 8080:5000 $(image):$(tag)