# Trial-Database-PostgreSQL

My trial database project using PostgreSQL + Python. The database stores data about imaginary students and the application allows to enter data, delete data, order data and see the database statistics.
To see the application and test how it works, you have to run it on localhost.
Here are the steps, how to do it:

1.	Install Virtual Box: https://www.virtualbox.org/wiki/Downloads
2.	Install Vagrant: https://www.vagrantup.com/downloads.html
3.	Install Git (If you didn't yet): https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
4.	Download the project to your computer from this github page
5.	Unzip the project
6.	Open Git Bash
7.	In Git Bash change directory (according to the place where the project is saved) to the project and the folder named vagrant. 
    E.g.: cd downloads/Trial-Database-PostgreSQL-master/vagrant
    (of course, the ugly name of the project can be changed into simplier one before doing this step)
8.	Run VM using this command: vagrant up 
    (wait, it can last several seconds)
9.	Log in using this command: vagrant ssh 
    (wait, it can last several seconds)
    This should be shown:  vagrant@vagrant-ubuntu-trusty-32: ~$
10.	All the files of the project have been copied into the VM, everything needed has been installed and the tables of the database were created according to the schemas given in test.sql file
11.	Change directory: cd /vagrant/test
12.	Enter this command: python test.py    
    This should be shown after that: 
    Serving HTTP on port 8000...
13.	Now write to your browser: localhost:8000
    The application should open.
