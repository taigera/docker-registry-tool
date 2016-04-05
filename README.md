# docker-registry-tool
Command-line tool for dealing with Docker Registry

## Introduction
The docker-registry-tool is a multi-platform command-line tool made with Python that abstracts the complexity of the Docker Registry API operations, thus making it easier to use. Moreover, the use of docker-registry-tool provides more security than the use of that API operations, as it only authenticates when you have an operation running and automatically closes the session when that operation is complete, so you do not have to worry about opening and closing authentication sessions every time.

These are the advantages of using docker-registry-tool:

* Compatible with Windows, GNU/Linux and OS X.
* Easy to use.
* More secure.
* Brings more operations (and possibilities) than using the operations available from the Registry API.

## Dependencies
You need to satisfy the following dependencies in order to compile the project 

* Python 2.7 with [pip](https://pip.pypa.io/en/stable/) tool installed.
* Python modules installed: [requests](http://docs.python-requests.org/en/master/) and [pyaes](https://github.com/ricmoo/pyaes)  
* [PyInstaller](http://www.pyinstaller.org) 3.1.1 or greater

## Install
Follow these instructions to compile and install docker-registry-tool.

1. Clone this repository.
2. Check that you have satisfied all dependencies by executing the command `python docker_registry_tool.py`. If the previous command does not return any error, then proceed to the next step.
3. Install PyInstaller as explained [here](http://pythonhosted.org/PyInstaller/)
4. Use PyInstaller to get a binary from the source files: `pyinstaller --onefile docker_registry_tool.py`.
5. You will get the binary file in the dist folder. 

## Configuration
The script configuration is made in the `docker_registry_tool.conf` file. You can open and modify it with a plain text editor. This file must be in the same path where the Docker Registry Tool is stored. 

## Run
### Get detailed information about an image stored in the Taiger Docker Registry
There are two subcommands designed specifically to retrieve technical information about an image:

* General information (identifiers, layers, ...) → `docker_registry_tool info --remote-image {IMAGE TO CHECK} --tag {TAG}` .Replace `{IMAGE TO CHECK}` and `{TAG}` with the proper image name and tag. For example, `docker_registry_tool info --remote-image ubuntu --tag latest`
* Digest → `docker_registry_tool digest --remote-image {IMAGE TO CHECK} --tag {TAG}`. Replace `{IMAGE TO CHECK}` and `{TAG}` with the proper image name and tag. For example, `docker_registry_tool digest --remote-image ubuntu --tag development`

### Uploading a new image to the Taiger Docker Registry
If you want to push a new image stored in the Taiger Docker Registry, then type this command `docker_registry_tool upload --remote-image {IMAGE TO CHECK} --tag {TAG}`. Replace `{IMAGE TO CHECK}` and `{TAG}` with the proper image name and tag. For example, `docker_registry_tool upload --remote-image ubuntu --tag development`

### Downloading an image stored in the Taiger Docker Registry
If you want to pull an image stored in the Taiger Docker Registry, then type this command `docker_registry_tool download --remote-image {IMAGE TO CHECK} --tag {TAG}`. Replace `{IMAGE TO CHECK}` and `{TAG}` with the proper image name and tag. For example, `docker_registry_tool download --remote-image mysql --tag latest`

### Process Docker Compose files that uses image stored in the Taiger Docker Registry
If you want to use a Docker Compose file that has linked some images stored in the Taiger Docker Registry, then type this command `docker_registry_tool compose --local-compose {DIRECTORY}`. Replace `{DIRECTORY}` with the directory where the Docker Compose file is. For example, `docker_registry_tool compose --local-compose /Users/Foo/Desktop/Project`

### Commit changes to an image stored in the Taiger Docker Registry
To update the image stored in the Taiger Docker Registry with the latest changes made in local containers, then you have to issue this command `docker_registry_tool commit --local-container {CONTAINER NAME} --remote-image {IMAGE NAME} --tag {TAG}`. Replace `{CONTAINER NAME}` with the local container that has the new changes and `{IMAGE NAME}` and `{TAG}` with the proper image name and tag. For example, `docker_registry_tool commit --local-container bc56c1151e2f --remote-image ubuntu --tag master`

Notice that this command will commit your local image too with the changes made in the container.

### List all images stored in the Taiger Docker Registry
If you want to get all images stored in the server, then you must type `docker_registry_tool images`.

### List all tags stored in the Taiger Docker Registry
If you want to get all tags of an image, then you must type `docker_registry_tool tags --remote-image {IMAGE TO CHECK}`. Replace `{IMAGE TO CHECK}` with the proper image name. For example, `docker_registry_tool tags --remote-image ubuntu`.

### Search for an image stored in the Taiger Docker Registry
Issue the following command to search for an image: `docker_registry_tool search --criteria {SEARCH CRITERIA}`. Replace `{SEARCH CRITERIA}` with the proper search criteria. The command will return a list with the names of the images that satisfy the search condition. For example, `docker_registry_tool search --criteria ub` will retrieve all names that contains "ub".

### Deleting an image stored with the  Taiger Docker Registry Tool
Issue the following command to delete an image: `docker_registry_tool delete --remote-image {IMAGE NAME} --tag {TAG}`. Replace `{IMAGE TO CHECK}` and `{TAG}` with the proper image name and tag. For example, `docker_registry_tool delete --remote-image ubuntu --tag old`

## Users
 * The company [Taiger](http://www.taiger.com) uses this tool in their development processes and infrastructures.


## Reporting issues
Issues can be reported via the [Github issue tracker](https://github.com/taigers/docker-registry-tool/issues).

Please take the time to review existing issues before submitting your own to prevent duplicates. Incorrect or poorly formed reports are wasteful and are subject to deletion.

## Submitting fixes and improvements
Fixes and improvements are submitted as pull requests via Github. 

## Related projects
 * [docker-registry-garbage-collector](https://github.com/taigers/docker-registry-garbage-collector)
 * [docker-registry-manager](https://github.com/taigers/docker-registry-manager)
