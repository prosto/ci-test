import docker

print("Checking docker client")
client = docker.from_env()

print("Created docker client", client.info())
client.ping()