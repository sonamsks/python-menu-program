import os


print('\t\t\t\t  Automation Configuration  ')
print("\t\t\t\t---------------------------- ")
print()



def core_site():
    print('Enter NameNode IP Address :-   ', end='')
    NN_ip=input()

    os.system('echo \<configuration\> >> core-site.xml')
    os.system('echo \<property\> >> core-site.xml')
    os.system('echo \<name\>fs.default.name\<\/name\> >> core-site.xml')

    if cmd=='1':
        os.system('echo \<value\>hdfs://{}:9001\<\/value\> >> core-site.xml'.format(NN_ip))
    else:
        os.system('echo \<value\>hdfs://{}:9001\<\/value\> >> core-site.xml'.format(NN_ip))

    os.system('echo \</property\> >> core-site.xml')
    os.system('echo \<\/configuration\> >> core-site.xml')

    if cmd=='2':
        os.system('scp core-site.xml {}:/etc/hadoop/core-site.xml'.format(remote_ip))
    else:
        os.system('cp core-site.xml /etc/hadoop/core-site.xml')
    os.system('rm -rf core-site.xml')
    os.system('cp temp.xml core-site.xml')

def hdfs_site():

    if cmd2=='6':
        print('Enter DataNode Directory name you want to create :-   ' ,end='')

    elif cmd2=='5':
        print('Enter NameNode Directory name you want to create :-   ' ,end='')

    dir_name=input()

    if cmd=='2':
        os.system('ssh {} mkdir {}'.format(remote_ip , dir_name))
    else:
        os.system('mkdir {}'.format(dir_name))
    os.system('echo \<configuration\> >> hdfs-site.xml')
    os.system('echo \<property\> >> hdfs-site.xml')

    if cmd2=='6':
        os.system('echo \<name\>dfs.data.dir\<\/name\> >> hdfs-site.xml')
    elif cmd2=='5':
        os.system('echo \<name\>dfs.name.dir\<\/name\> >> hdfs-site.xml')
    os.system('echo \<value\>{}\<\/value\> >> hdfs-site.xml'.format(dir_name))
    os.system('echo \</property\> >> hdfs-site.xml')
    os.system('echo \<\/configuration\> >> hdfs-site.xml')
    if cmd=='2':
        os.system('scp hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml'.format(remote_ip))
    else:
        os.system('cp hdfs-site.xml /etc/hadoop/hdfs-site.xml')
    os.system('rm -rf hdfs-site.xml')
    os.system('cp temp2.xml hdfs-site.xml')

while True:
    print("\t\t\t\tPress 1 to Configure Local Server\n\t\t\t\tPress 2 to Configuring Remote Server")
    print('\t\t\t\tPress 0 to Exit')
    print('\t\t\t\t => ', end='')
    cmd=input()

    if cmd=='1':

        print('\t\t\tpress 1 to Show Date \n\t\t\tpress 2 to Show Calender')
        print('\t\t\tpress 3 to Run Any Linux Command')
        print('\t\t\tpress 4 to Configure WebServer')
        print('\t\t\tpress 5 to Configure and Start NameNode')
        print('\t\t\tpress 6 to Configure and Start DataNode')
        print('\t\t\tpress 7 to Configure LVM ')
        print('\t\t\tpress 8 to work on aws')
        print('\t\t\t\t =>  ', end='')
        cmd2=input()

        if cmd2=='1':
            os.system("sudo date")

        elif cmd2=='2':
            os.system('sudo cal')

        elif cmd2=='3':
            print('Enter Linux Command :-   ' , end='')
            linux_cmd=input()
            os.system('sudo {}'.format(linux_cmd))

        elif cmd2=='4':
            os.system('yum install httpd -y')
            os.system('systemctl start httpd')
            os.system('systemctl enable httpd')
            os.system('cp index.html /var/www/html')

        elif cmd2=='5':
            os.system('rpm -ivh /jdk-8u171-linux-x64.rpm')
            os.system('rpm -ivh /hadoop-1.2.1-1.x86_64.rpm --force')
            hdfs_site()
            core_site()
            os.system('hadoop namenode -format')
            os.system('hadoop-daemon.sh start namenode')
            os.system('jps')

        elif cmd2=='6':
            os.system('rpm -ivh /jdk-8u171-linux-x64.rpm')
            os.system('rpm -ivh /hadoop-1.2.1-1.x86_64.rpm --force')
            hdfs_site()
            core_site()
            os.system('sudo hadoop-daemon.sh start datanode')
            os.system('sudo jps')


        elif cmd2=='7':
            no=int(input("how many EBS you want to attach : "))
            os.system('fdisk -l')
            EBS1=input("enter EBS path : ")
            EBS2=input("enter EBS path : ")
            os.system("pvcreate {}".format(EBS1))
            os.system("pvdisplay {}".format(EBS1))
            os.system("pvcreate {}".format(EBS2))
            os.system("pvdisplay {}".format(EBS2))
            vgname=input("enter vg name : ")
            os.system('vgcreate {} {} {}'.format(vgname,EBS1,EBS2))
            os.system('vgdisplay {}'.format(vgname))
            lvname=input("enter lv name : ")
            lvsize=input('enter lv size : ')
            os.system('lvcreate --size {}G --name {} {}'.format(lvsize,lvname,vgname))
            os.system('lvdisplay {}/{}'.format(vgname,lvname))
            os.system('vgdisplay {}'.format(vgname))
            os.system('mkfs.ext4 /dev/{}/{}'.format(vgname,lvname))
            folder=input("enter folder name : ")
            os.system("mkdir /{} ".format(folder))
            os.system('mount /dev/{}/{}  /{}'.format(vgname,lvname,folder))
            os.system('df -h')

        else:
            print('Please , Select above given Options . Thank You :)')

    elif cmd=='2':
        print("enter remote OS IP :-   ", end='')
        remote_ip=input()

        print('\t\t\tpress 1 to Show Date \n\t\t\tpress 2 to Show Calender')
        print('\t\t\tpress 3 to Run Any Linux Command')
        print('\t\t\tpress 4 to Configure WebServer')
        print('\t\t\tpress 5 to Configure and Start NameNode')
        print('\t\t\tpress 6 to Configure and Start DataNode')
        print('\t\t\tpress 7 to do Parition')
        print('\t\t\t\t =>  ', end='')
        cmd2=input()

        if cmd2=='1':
            os.system("ssh {} date".format(remote_ip))

        elif cmd2=='2':
            os.system('ssh {} cal'.format(remote_ip))

        elif cmd2=='3':
            print('Enter Linux Command :-   ' , end='')
            linux_cmd=input()
            os.system('ssh {} {}'.format(remote_ip ,linux_cmd))

        elif cmd2=='4':
            os.system('ssh {} yum install httpd -y'.format(remote_ip))
            os.system('ssh {} systemctl start httpd'.format(remote_ip))
            os.system('ssh {} systemctl enable httpd'.format(remote_ip))
            os.system('scp index.html {}:/var/www/html'.format(remote_ip))

        elif cmd2=='5':
            os.system('ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(remote_ip))
            os.system('ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'.format(remote_ip))
            hdfs_site()
            core_site()
            os.system('ssh {} hadoop namenode -format'.format(remote_ip))
            os.system('ssh {} hadoop-daemon.sh start namenode'.format(remote_ip))
            os.system('ssh {} jps'.format(remote_ip))

        elif cmd2=='6':
            os.system('ssh {} rpm -ivh /jdk-8u171-linux-x64.rpm'.format(remote_ip))
            os.system('ssh {} rpm -ivh /hadoop-1.2.1-1.x86_64.rpm --force'.format(remote_ip))
            hdfs_site()
            core_site()
            os.system('ssh {} hadoop-daemon.sh start datanode'.format(remote_ip))
            os.system('ssh {} jps'.format(remote_ip))
            os.system('ssh {} hadoop dfsadmin -report'.format(remote_ip))

        elif cmd2=='7':
            os.system('ssh {} fdisk -l'.format(remote_ip))
            ini=input("enter path")
            os.system('ssh {} fdisk {}'.format(remote_ip,ini))
            os.system('ssh {} fdisk -l'.format(remote_ip))
            ini2=input("enter path")
            os.system('ssh {} mkfs.ext4 {}'.format(remote_ip,ini2))
            print('\t\tEnter name of Directory to mount the HDs')
            dirname=input()
            os.system('ssh {} mkdir {}'.format(remote_ip , dirname))
            os.system('ssh {} mount /dev/xvdf3 {}'.format(remote_ip , dirname))
            os.system('ssh {} df -h'.format(remote_ip))
        else:
            print('Select options as mention')
    elif cmd=='0':
        break
    else:
        print('\n\t\t\t\tPlease Choose Valid Options mention above')
                                                                                                                           


                                                                                                                           