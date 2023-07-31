import time
import os

def configure_aws():
    ch = input("Do you wan't to install aws-cli(y/n)")
    if ch == 'y' or ch == 'Y' :
        os.system('curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"')
        os.system("unzip awscliv2.zip")
        os.system("./aws/install")
    print("***  CONFIGURE THE OS  ***")
    os.system("aws configure")
    input("\t\t Press Enter to Continue")


def key_pair():
    key = input("Create a new key name : ")
    os.system(f"aws ec2 create-key-pair --key-name {key}")
    input("\t\t Press Enter to Continue")

def ec2():
    while True :
        os.system("clear")
        print("""
        press 1 : To describe EC2 instance
        press 2 : To launch EC2 instance
        press 3 : To start EC2 instance
        press 4 : To stop EC2 instance
        press 5 : To terminate EC2 instance
        press 6 : Return to menu
        """)

        i = int(input("Enter your choice : "))
        print(i)

        if i ==1 :
            ec2_describe()
        if i == 2:
            ec2_launch()
        if i==3:
            ec2_start()
        if i == 4:
            ec2_stop()
        if i == 5:
            ec2_termintate()
        if i==6:
            return


        else :
            print("\n Select correct option")


# WE WILL DEAL WITH THE AWS SERVICES HERE

def s3():
    while True:
        os.system("clear")
        print("="*20)
        print("CHOOSE YOUR S3 SERVICES")
        print("="*20)
        print("""
        press 1 : To create a s3 bucket
        press 2 : To upload the content in S3 bucket
        press 3 : To delete s3 bucket
        press 4 : To delete object from the bucket
        press 5 : Return to memu
        """
        )

        i= int(input("Enter your choice :::: "))
        if i==1:
            pass
        elif i==2:
            pass
        elif i==3:
            del_s3bucket()
        elif i==4:
            pass
        elif i==5:
            pass
        else:
            print("\n Select correct option")

# ALL THE COMMANDS RELATED WITH EBS(ELASTIC BLOCK STORAGE)

def ebs():
    while True:
        os.system("clear")
        print("="*20)
        print("CHOOSE YOUR EBS COMMANDS")
        print("="*20)
        print("""
        press 1 : To create a EBS storage
        press 2 : To show all the availabel EBS storage
        press 3 : To attach the EBS
        press 4 : To detach the EBS
        press 5 : To delete the EBS
        press 6 : Create snapshot of EBS
        press 7 : Return to main MENU
        """
        )

        i= int(input("Enter your choice :::: "))
        if i==1:
            ebs_create()
        elif i==2:
            ebs_describe()
        elif i==3:
            ebs_attach()
        elif i==4:
            ebsDetach()
        elif i==5:
            ebs_del()
        elif i==6:
            createEBSSnapshot()
        elif i ==7 :
            return

        else:
            print("\n Select correct option")

# =============================== ALL EC2 FUNCTIONS ================================

# this function will lauch the ec2 instance
def ec2_launch():
    ami = input("Enter the AMI ID : ")#LIST OF AMI CAN BE PROVIDED

    ins = input("Enter the instance type: ")
    number = int(input("Enter the number of instances you want to lauch"))
    sec_grp = input("Enter the security group:")
    sub = input("Enter the subnet ID :")
    key = input("Enter your key name: ")
    os.system(f"aws ec2 run-instances --image-id {ami} --instance-type {ins} --count {number} --subnet-id {sub} --security-group-ids {sec_grp} --key-name {key}")

def ec2_describe():
    os.system("aws ec2 describe-instances")
    input("\n Press enter to continue")

def ec2_start():
    instance_id = input("Enter your instance ID : ")
    os.system(f"aws ec2 start-instances --instance-ids {instance_id}")
    input("\n Press enter to continue")



def ec2_stop():
    instance_id = input("Enter your instance ID : ")
    os.system(f"aws ec2 stop-instances --instance-ids {instance_id}")
    input("\n Press enter to continue")

def ec2_termintate():
    instance_id = input("Enter your instance ID : ")
    os.system(f"aws ec2 start-instances --instance-ids {instance_id}")
    input("\n Press enter to continue")

# EBS SERVICES

def ebs_describe():
    os.system("aws ec2 describe-volumes")
    input("\n\n Press Enter to continue")

def ebs_create():
    volType = input("Enter volume type (like gp2) : ")
    size = input("Enter the volume size (min 1 GiB)")
    availZone = input("Enter the avialability zone: ")
    os.system(f'aws ec2 create-volume --volume-type {volType} --size {size} --availability-zone {availZone}')

def ebs_attach():
    instanceId = input("Enter the instance ID where you would like to attach the volume  : ")
    ebsVolId = input("Enter the volume ID of EBS : ")
    deviceName = input("Enter the device name like /dev/sdf : ")
    os.system(f"aws ec2 attach-volume --instance-id {instanceId} --volume-id {ebsVolId} --device {deviceName}")
    input("n\n Press enter to continue")

def ebs_del():
    print("\t\t It is recommended to unmount the volume from the device ")
    volID = input("Enter the volume ID : ")
    os.system(f"aws ec2 delete-volume --volume-id {volID}")
    input("\n\n Press Enter to continue ")

def createEBSSnapshot():
    ebsVolId = input("Enter the volume ID of EBS : ")
    descSnapshot = input("Describe your snapshot : ")
    os.system(f"aws ec2 crete-snapshot --volume-id {ebsVolId} --description {descSnapshot}")


def ebsDetach():
    ebsVolId = input("Enter the volume ID of EBS : ")
    os.system(f"aws ec2 detach-volume --volume-id {ebsVolId}")


# ALL THE FUNCTIONS FOR S3 SERVICE

def del_s3bucket():
    bucketName = input("Enter the unique bucket name : ")
    region  = input("Enter the region : ")
    os.system(f'aws delete-bucket --bucket {bucketName} --region {region}')

def s3content():
    location = input("Enter the local machine : ")
    bucketName = input("Enter the unique bucket name : ")
    print("\n\n upload process initiated ....... \n\n")

    os.system(f"aws s3 sync {location} s3://{bucketName}")

if __name__ == "__main__":
    while True:
        print("\t\t Press 1 to work on ec2 instances : ")
        print("\t\t Press 2 to work on EBS")
        print("\t\t Press 3 to run aws configuration")
        print("\t\t Press 4 to create a new key pair")
        print("\t\t Press 9 to terminate")
        ch = int(input("Enter your choice : "))

        if ch == 1:
            ec2()
        elif ch==2:
            ebs()
        elif ch==3:
            configure_aws()
        elif ch==4:
            key_pair()
        elif ch==9:
            exit()
        else :
            print("Enter correct options")




