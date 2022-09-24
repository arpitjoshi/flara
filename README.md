Requirements
----
1. python3.x
2. pip
3. venv
----

Endpoints of the Service
----
1. Base/Ping - `http://127.0.0.1:5000/` OR `http://127.0.0.1:5000/ping`
2. Factorial - `http://127.0.0.1:5000/factorial?n=3`
3. Fibonacci - `http://127.0.0.1:5000/fibonacci?n=4`
4. Ackermann - `http://127.0.0.1:5000/ackermann?m=1&n=1`
----

Output of the Service Endpoints
----
1. response body is a JSON string. eg - `{"algo":"factorial","result":1,"status":"success"}`
2. response content-type is `application/json`
3. response code is 200 for a success or 400 for failure
----

Project Structure
----
 1. The project is build on `Flask 2.0`.
 2. project root - contains `requirements.txt`, `README.md`, `src`, `Dockerfile`, `docker-compose.yaml`, `venv(virtual environment)`
 3. src - source code of the project.
    1. Packages - api, app, tasks, tests
    2. Files - wsgi.py, settings_common.py, settings_testing.py
 4. wsgi.py - entrypoint for the flask application
 5. settings_common.py & settings_testing.py - for settings
 6. app - package for creating the flask app instance
 7. api - package for creating blueprints and api endpoints
 8. tasks - package for math functions
 9. tests - package for unittests. Contains more packages within it.
    1. test_algos - package & class for unittests of tasks
    2. test_apis - package & class for unittests of api endpoints
----

Setup - Native
----
This requires python3.x installed on the machine
1. Create virtual env & activate
   > python3 -m venv venv
   > 
   > source venv/bin/activate
2. Install requirements
   > pip install -r requirements.txt
3. Run the webserver
   > PYTHONPATH=src SIMPLE_SETTINGS=settings_common gunicorn --workers 3 --bind 127.0.0.1:5000 wsgi:app  ##with gunicorn (wsgi server)
   > 
   > PYTHONPATH=src SIMPLE_SETTINGS=settings_common,settings_testing flask run ##without gunicorn
4. Run the Testcases
   > PYTHONPATH=src SIMPLE_SETTINGS=settings_common,settings_testing flask test
----

Setup - Docker 
----
1. Build & Run, entry point gunicorn command.
   > docker-compose up --build
2. Put `-d` switch in the end to run the container in the detached mode
3. Run the test cases
   > docker-compose run -e SIMPLE_SETTINGS=settings_common,settings_testing web flask test
4. Stop & clean up containers
   > docker-compose down
----

Measuring time of math functions
----
1. A decorator `@timeit` is placed on the function
2. It captures the runtime of math function and writes on the `logger`
3. `logger` is using std out but can be changed to log file.
4. `LOG_LEVEL` is set to `DEBUG` explicitly in settings_common.py for displaying runtime & not recommended in production
----

Setup in Cloud
----
1. VM Machine (AWS EC2 and Elastic IP)
   1. Open EC2 console on web
   2. Create a new EC2 with free AMIs like aws-linux
   3. Attach VPC, Attach volume, Setup ssh key pair, Assign security groups
   4. Allow port 80, 443 ports in security groups
   5. SSH to server using ssh key pair
   6. SCP the code to ec2-user and follow the native setup of project
   7. Install Nginx  
   8. Update the nginx.conf for setting upstream to port 5000
   9. Alternatively run gunicorn with bind unix socket and set Nginx upstream to unix socket
2. VM Machine (AWS AutoScaling groups & EC2)
   1. Create a VM as above
   2. Create an AMI of the VM
   3. Create a launch template for Autoscaling
      1. Choose the AMI that we created
      2. Select instance type like m1.large, t2.large etc and set security group
   4. Create auto-scaling groups using Wizard
   5. Keep the size of group to be 2 for High availability. Default is 1.
   6. Setup ELB and point the traffic to auto-scaling group
3. Serverless (AWS Lambda)
   1. Use python `zappa` package to deploy on AWS Lambda
   2. Activate the virtual env and then install `pip install zappa`
   3. Create AWS user & group in IAM and assign lambda execution role. For quick setup use `AWSLambdaFullAccess`, but FullAccess not recommended.
   4. Use `access_key_id` & `secret_access_key` of the user in `zappa_settings.json`
   5. Run `zappa deploy dev`. It returns the web service URL.
   6. Changes in app - `zappa update dev`
   7. Stop & remove the app - `zappa undeploy dev`
4. Containers (AWS ECS)
   1. Run & test the app locally using docker setup
   2. Install AWS Cli
   3. Build the container using `docker build -t image_name:version` for pushing to ECR
   4. Assuming ECR(private container registry) setup already done, tag the image using `docker tag` and push using `docker push`
   5. Assuming ECS cluster setup is done using either `AWS EC2` or `AWS Fargate`
   6. Create Task definition specifying task role, task memory and cpu units 
   7. Create Cluster service specifying Task definition, number of tasks, and deployment type(rolling/blue-green)
   8. Create app load balancer and attach service and port number
5. Containers (AWS EKS)
   1. Assuming EKS is already setup 
   2. Create deployment YAML file mentioning name, metadata, replicas, selectors etc.
   3. run `kubectl apply -f app-deployment.yaml`
   4. expose the app using kubectl service
---

Monitoring 
---
1. Cloudwatch monitoring can be enabled.
2. APM like newrelic can also be used for app performance & monitoring
3. Sentry can be added for unhandled exceptions
---

Improvements
----
1. `ASGI` can be implemented for high throughput
2. environment variables can be moved `.env` files
3. http response codes being used are only 200 & 400 for quick implementation
---
