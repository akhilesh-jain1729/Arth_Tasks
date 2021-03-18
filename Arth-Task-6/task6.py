import os
import getpass
print("\t\t\tWelcoming you")
print("\t\t\t--------------------")



print("WELCOME TO AWS CLOUD")
print("Configure AWS")
os.system('aws configure')

def key_pair():
		key = input('Enter key name you want to create')
		os.system('aws ec2 create-key-pair --key-name {}'.format(key))

def ec2():
		while True:
			print("\n \n")
			print("""
			Press 1: Describe_ec2
			Press 2: launching_ec2
			Press 3: stopping_ec2
			Press 4: starting_ec2
			Press 5: terminating ec2
			Press 6: 
			Press 7: 
			Press 8: 
			Press 9: 
			Press 10: return to menu
			""")

			
			i = int(input("Enter ur choice : "))
			print(i)
			if i==1:
				Describe_ec2()
			elif i==2:
				launching_ec2()
			elif i==3:
				stopping_ec2()
			elif i==4:
				starting_ec2()
			elif i==5:
				terminate_ec2()
			elif i==10:
				menu()
			else:
				os.system("hadoop dfsadmin -report")  
def s3():
		while True:
			print("\n \n")
			print("""
			Press 1: creating_s3_bucket
			Press 2: updating_content_to_s3
			Press 3: updating_put_acl_policy
			Press 4: delete_bucket
			Press 5: delete_object_from_bucket
			Press 6: 
			Press 7: 
			Press 8: 
			Press 9: 
			Press 10: return to menu
			""")

			
			i = int(input("Enter ur choice : "))
			print(i)
			if i==1:
				s3bucket()
			elif i==2:
				s3content()
			elif i==3:
				s3put()
			elif i==4:
				s3delete()
			elif i==5:
				s3deleteo()
			elif i==10:
				menu()
			else:
				os.system("hadoop dfsadmin -report")  
	 
def ebs():
		while True:
			print("\n \n")
			print("""
			Press 1: creating_ebs_storage
			Press 2: describe_ebs
			Press 3: attaching_ebs
			Press 4: detaching_ebs
			Press 5: deleting_ebs
			Press 6: 
			Press 7: 
			Press 8: 
			Press 9: 
			Press 10: return to menu
			""")

			
			i = int(input("Enter ur choice : "))
			print(i)
			if i==1:
				Creating_ebs()
			elif i==2:
				Describe_ebs()
			elif i==3:
				Attaching_ebs()
			elif i==4:
				Detaching_ebs()
			elif i==5:
				Deleting_ebs()
			elif i==10:
				menu()
			else:
				os.system("hadoop dfsadmin -report")   

def sg():
		while True:
			print("\n \n")
			print("""
			Press 1: creating_sg
			Press 2: describe_sg
			Press 3: adding_ingress_to_security_group
			Press 4: updating_egress_to_security_group
			Press 5: deleting_sg
			Press 6: 
			Press 7: 
			Press 8: 
			Press 9: return to menu
			Press 10: exit
			""")

			
			i = int(input("Enter ur choice : "))
			print(i)
			if i==1:
				Security_group()
			elif i==2:
				Describe_sg()
			elif i==3:
				Ingress()
			elif i==4:
				Egress()
			elif i==5:
				Deleting_sg()
			elif i==9:
				menu()
			elif i==10:
				exit()
			else:
				os.system("hadoop dfsadmin -report")   


def launching_ec2():
		a = input('Enter AMI_ID: ')
		i = input('Enter instance-type: ')
		c = int(input('Enter number of instance you want to launch: '))
		s = input('Enter subnet-ID: ')
		sg = input('Enter security-group: ')
		k = input('Enter key name: ')
		os.system('aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {}'.format(a,i,c,s,sg,k))

def Describe_ec2():
		os.system('aws ec2 describe-instances')

def starting_ec2():
		a = input('Enter ami-id: ')
		os.system('aws ec2 start-instances --instance-ids {}'.format(a))
		
def stopping_ec2():
		a = input('Enter ami-id: ')
		os.system('aws ec2 stop-instances --instance-ids {}'.format(a))

def terminate_ec2():
		a = input('Enter ami-id: ')
		os.system('aws ec2 terminate-instances --instance-ids {}'.format(a))

def Describe_ebs():
		os.system('aws ec2 describe-volumes')

def Attaching_ebs():
		a = input('Enter instance-id: ')
		v = input('Enter volume-id: ')
		d = input('Enter device-name: ')
		os.system('aws ec2 attach-volume --instance-id {} --volume-id {} --device {}'.format(a,v,d))

def Creating_ebs():
		t = input('Enter volume type eg. gp2: ')
		s = input('Enter volume-size: ')
		a = input('Enter availability-zone eg.ap-south-1a: ')
		os.system('aws ec2 create-volume --volume-type {} --size {} --availability-zone {}'.format(t,s,a))

def Detaching_ebs():
		v = input('Enter volume-id: ')
		os.system('aws ec2 detach-volume --volume-id {}'.format(v))

def Deleting_ebs():
		v = input('Enter volume-id: ')
		os.system('aws ec2 delete-volume --volume-id {}'.format(v))

def Security_group():
		n = input('Enter security_group_name: ')
		d = input('Add description: ')
		v = input('Enter vcp_id: ')
		os.system('aws ec2 create-security-group --group-name {} --description "{}" --vpc-id {}'.format(n,d,v))

def Describe_sg():
		i = input('Enter security_group_id: ')
		os.system('aws ec2 describe-security-groups --group-ids {}'.format(i))

def Ingress():
		i = input('Enter security-group id: ')
		n = input('Enter security-group name: ')
		e = input('Enter protocol: ')
		p = int(input('Enter port number: '))
		c = input('Enter cidr-block: ')
		os.system('aws ec2 authorize-security-group-ingress --group-id {} --group-name {} --protocol {} --port {} --cidr {}'.format(i,n,e,p,c))

def Egress():
		i = input('Enter security-group id: ')
		e = input('Enter protocol: ')
		p = int(input('Enter port number: '))
		c = input('Enter cidr-block: ')
		os.system('aws ec2 authorize-security-group-egress --group-id {}  --protocol {} --port {} --cidr {}'.format(i,e,p,c))

def s3bucket():
		n = input('Enter a unique bucket name: ')
		r = input('Enter region: ')
		os.system('aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}'.format(n,r,r))

def s3delete():
		n = input('Enter bucket name: ')
		r = input('Enter region: ')
		os.system('aws s3api delete-bucket --bucket {} --region {}'.format(n,r))

def s3content():
		l = input('Enter local location: ')
		n = input('Enter bucket name: ')
		os.system('aws s3 sync "{}" s3://{}'.format(l,n))
def s3put():
		n = input('Enter bucket-name: ')
		k = input('Enter key or pic: ')
		os.system('aws s3api put-object-acl --bucket {} --key {} --acl public-read'.format(n,k))

def s3deleteo():
		n = input('Enter bucket-name: ')
		k = input('Enter key or pic: ')
		os.system('aws s3api delete-object --bucket {} --key {}'.format(n,k))

def cloudfront():
		n = input('Enter bucket name: ')
		os.system('aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com'.format(n))

def Deleting_sg():
		n = input('Enter security_group_id: ')
		os.system('aws ec2 delete-security-group --group-id {}'.format(n))

def menu():
		while True:
			print("\n \n")
			print("""
			Press 1: creating_a_key_pair
			Press 2: ec2
			Press 3: ebs
			Press 4: security_group
			Press 5: s3bucket
			Press 6: creating_cloudfront
			Press 7: 
			Press 8: 
			Press 9: 
			Press 10: to exit
			""")

			
			i = int(input("Enter ur choice : "))
			print(i)
			if i==1:
				key_pair()
			elif i==2:
				ec2()
			elif i==3:
				ebs()
			elif i==4:
				sg()
			elif i==5:
				s3()
			elif i==6:
				cloudfront()
			elif i==10:
				exit()
			else:
				os.system("hadoop dfsadmin -report")


while True:
			print("\n \n")
			print("""
			Press 1: creating_a_key_pair
			Press 2: ec2
			Press 3: ebs
			Press 4: security_group
			Press 5: s3bucket
			Press 6: creating_cloudfront
			Press 7: 
			Press 8: 
			Press 9: 
			Press 10: to exit
			""")

			
			i = int(input("Enter ur choice : "))
			print(i)
			if i==1:
				key_pair()
			elif i==2:
				ec2()
			elif i==3:
				ebs()
			elif i==4:
				sg()
			elif i==5:
				s3()
			elif i==6:
				cloudfront()
			elif i==10:
				exit()
			else:
				exit()  
