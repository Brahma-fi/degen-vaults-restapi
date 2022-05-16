image=${PM_API_IMAGE_NAME}
tag=latest
url=${AWS_URL}
region=${AWS_REGION}


build:
		docker buildx build --platform=linux/amd64 -t $(image) .

login:
		aws ecr get-login-password --region $(region) | docker login --username AWS --password-stdin $(url)

push: 
		docker tag $(image):$(tag) $(url)/$(image):$(tag)
		aws ecr get-login-password --region $(region) | docker login --username AWS --password-stdin $(url)
		docker push $(url)/$(image):$(tag)

run: 
		docker run -p 8080:5000 $(image):$(tag)