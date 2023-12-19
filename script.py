import docker

print("Checking docker client")
client = docker.from_env()

print("Created docker client", client.info())
client.ping()

print("Starting docker container")
container = client.containers.run(
    image="neo4j:5.13.0",
    auto_remove=True,
    environment={
        "NEO4J_AUTH": "neo4j/passw0rd",
    },
    name="test_neo4j_haystack",
    ports={"7687/tcp": ("127.0.0.1", 7687)},
    detach=True,
    remove=True,
)
print("Started docker container", container)
container.stop()

print("Stopped docker container", container)