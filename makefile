image=protected_moonshots_restapi
tag=latest
url='820675130125.dkr.ecr.us-east-2.amazonaws.com'
region=us-east-2


build:
		docker buildx build --platform=linux/amd64 -t $(image) .

push: 
		docker tag protected_moonshots_restapi:latest 820675130125.dkr.ecr.us-east-2.amazonaws.com/protected_moonshots_restapi:latest
		aws ecr get-login-password --region $(region) | docker login --username AWS --password-stdin $(url)
		docker push 820675130125.dkr.ecr.us-east-2.amazonaws.com/protected_moonshots_restapi:latest

run: 
		docker run -p 8080:5000 $(image):$(tag)