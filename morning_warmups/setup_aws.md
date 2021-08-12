##Setting Up Amazon Web Services (AWS)

This week we will be needing a lot of AWS. Following the instructions below to set up your account
and claim the free credit that is available to you.

<br>

##Part 1: Create an AWS account

See [Part 1][setup_aws]

- Create Security Credentials.  Go to the 
  [AWS security credentials page](https://console.aws.amazon.com/iam/home?#security_credential).
  If you are asked about IAM users, close the message.  Expand **Access Keys** and click **Create New
  Access Key**.  You will see a message **Your access key (access key ID and secret access key) has been
  created successfully**. Click **Download Key File** and save it to your home directory. 
  
  Remember where this file is. It contains the **Access Key ID** and **Secret Access Key**. 
  
<br>

##Part 2: Setting up an EC2 key pair

To connect to an Amazon EC2 instances, you need to create an **SSH key pair**. 

- After setting up your account, go to the [EC2 console](https://console.aws.amazon.com/ec2)

- Select the region to be **N.Virgina**. Please do not work with another region.

  ![image](img/region.png)

- On the left click **Key Pair** and then **Create Key Pair**
  
  <img height="400px" src="img/keypair.png">
    
- Download and save the `.pem` private key file to a new folder `.ssh` in your home directory. Any folder
  that starts with a `.` will hide the folder. In this case, you want to hide the sensitive information.
  Change the permissions of the file using this command:

  ```$ chmod 400 </path/to/saved/keypair/file.pem>```

<br>

##Part 3: Activate your AWS free credit

See [Part 2][setup_aws]

[setup_aws]:https://github.com/GalvanizeDataScience/unix/edit/master/setup_aws.md
