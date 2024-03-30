

# Build the Docker image
build:
	docker build -t iris-classifier .

# Run the Docker container
run:
	docker run -p 5000:5000 --name iris-container1 iris-classifier

# Stop the Docker container
stop:
	docker stop iris-container

# Remove the Docker container
remove:
	docker rm iris-container

# Clean up Docker images
clean:
	docker rmi iris-classifier
