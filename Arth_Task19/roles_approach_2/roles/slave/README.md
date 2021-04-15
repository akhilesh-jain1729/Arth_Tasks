Role Name
=========

This is a role which will configure Slave Node of a Multi Node Kubernetes Cluster on Public Cloud. Here, I have used AWS as my Public Cloud Provider.

Requirements
------------

Requirements for these are:
1.) Pre-created Instanes
2.) 2 files: ec2.py script and ec2.ini file
3.) Public Key, attached to these Instances
4.) Master Node pre-Configured with it's token saved in a file.

Role Variables
--------------

There are various Variables used in this role:
docker_repo_url: This is used to take Docker Repo URL
docker_pkg: This will take the name of the docker package
docker_svc: Service Name of Docker
k8s_repo_url: Kubernetes Repo URL
k8s_gpg_url: Gpgkey URL, may be used in OS other than Centos(like Redhat).
k8s_repo_pkg: List of Kubernetes Packages to install
docker_driver_path: Path of file to change the driver
warning2_pkg: iproute-tc Package
cidr_range: Range of Pods
k8s_conf_path: Kubernetes Configuration Path
k8s_dir_path: Kubernetes Directory Path
flannel_url: Url to install flannel
file_dest: Path to file in which token is stored.

Dependencies
------------

Generally, no dependency is there internally, but it is preferrable to use my Master role for configuring Master first and then by adding this role also in the same play to a SLave host will be much preferrable to do. Otherwise If you have all the Requirements fullfilled, then just run this role in a play.
Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: tag_Name_Slaves
      ignore_errors: yes     
      become: yes 
      vars_files: 
         - vars.yml
      roles:
         - slave

License
-------

BSD

Author Information
------------------

I am Akhilesh Jain, who has created this role. To understand more about this role and this complete Task, visit the following platforms of mine:

LinkedIN Profile: https://www.linkedin.com/in/akjain9221/
Medium Profile: https://akhileshjain9221.medium.com/
