import docker

print("Checking docker client")
client = docker.from_env()

print("Created docker client", docker.info())
client.ping()