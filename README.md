# Running PySpark and GraphFrames in a Docker container

This repo shows how to run [PySpark](https://spark.apache.org/docs/latest/api/python/index.html) and the [GraphFrames](https://graphframes.io/) library using a Docker Container, without having to worry about installing Spark-related dependencies in your machine.

This guide assumes you are a Visual Studio Code user.

## Step 1: Install Docker Desktop

If you don't have it installed already, follow the instructions to install [Docker Desktop](https://docs.docker.com/desktop/).

## Step 2: Download the Spark Docker image

Open a terminal and run `docker pull spark:python3`.

## Step 3: Install the Dev Containers VS Code extension

Make sure you have the [Dev Containers](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/devcontainers-getting-started/) extension installed in VS Code.

## Step 4: Run the repository in a container

Clone the repository from GitHub and open it in VS Code.
Press `shift` + `ctrl` + `P` to open the command palette and search for `Dev Containers: Reopen in Container`.
This will create a container from the `spark:python3` image and install a few Python packages inside a virtual environment.

## Step 5: Test the container

Within the Dev Containers session, open a terminal, source the virtual environment, and test the installation by running:

```
python pyspark_test.py
python graphframes_test.py
```
