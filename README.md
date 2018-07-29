**You can look at the application by clicking on the link**: [Live Demo](http://ec2-52-91-225-216.compute-1.amazonaws.com)


**credentials for login:**
   * user: admin
   * pass: admin123
   
* Scheduler for deleting URL is triggered every 5 minutes, so you can test its work by creating a new URL, and then update it by setting old date


##### local application startup:

  *  To set dependencies, use `pip install -r requirements.txt`
  *  To view application without task scheduler _(celery & RabbitMQ)_
      you can simply run `python3 manage.py runserver`  in the root folder of the application
  *  In order to run the scheduler in parallel, you need to install [RabbitMQ](https://www.rabbitmq.com/).
        If you already have RabbitMQ installed, you can use the `start_server.sh` script
        to run the application at the same time, as well as the task scheduler


##### Packing application in docker container and launching:

  *  By using `wrap_app.sh` script you can package the application into container and run it.
       but for this you must have a privileged user on the computer for the docker [instruction](https://docs.docker.com/install/linux/linux-postinstall/)
       Or you can execute commands `sudo docker build -t <image_name>` and `sudo docker run -p <host_port>:8000 -d <image_name>` separately, being in the root directory of the application
  *  This script will automatically install RabbitMQ and all dependencies in the container, and also run it
  *  By default, the 8000 port of the container is pushed to the 80 port of the host.

##### Installing and running application on remote server using Ansible

  *  It is possible to move the application to remote server, pack it into docker and run, using just one command of Ansible
        To do this, you must have an installed [Ansible](https://docs.ansible.com/) and also configure the inventory (hosts)           file to connect to the remote server.
  *  After you can run `ansible-playbook <absolute or relative path to 'main.yaml'>`


