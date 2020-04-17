# Clone the macaddress repository.

https://github.com/mn450/macaddress.git

# Change the api key as shown in below feild in main.py python file.

PARAMS = {'apiKey': 'your api key here', 'output':'json', 'search': search}

# Building the docker image by running below command

docker build -t testimage .

# Now run the container from testimage (docker image) by passing MAC-address as argument

docker run -ti testimage 98-22-EF-E3-42-AA

# Finally you will get output of CompanyName with respect to 98-22-EF-E3-42-AA MAC-address

root@test:/tmp/macaddress# docker run -ti testimage 98-22-EF-E3-42-AA
Company Name == Liteon Tech Corp
