# SSH into a AWS EC2

### From the documentation:
  SSH ([Secure Shell](https://en.wikipedia.org/wiki/SSH_(Secure_Shell)))  is a program for logging into a remote machine and for executing commands on a remote machine.  It is intended to provide secure encrypted communications between two untrusted hosts over an insecure network.    
  SSH connects and logs into the specified destination, which may be specified as either `[user@]hostname` or a URI of the form `ssh://[user@]hostname`.  The user must prove his/her identity to the remote machine using one of several methods.  When connecting to AWS we will use PEM keys.   
  If a command is specified, it is executed on the remote host instead of a login shell.


In short SSH is a secure transfer protocol that allows one to securely connect to another system.    

---------------
    
# Using SSH:

**Note** you can always look at the documentation for ssh by typing the command ` man ssh ` into a terminal.     
1) Create a EC2 instance:  
 - Note the operating system (including version of Linux).   
 - If using existing PEM key make sure you still have it. If using a new one note were you downloaded the key.
 - If using a new key move to to a folder dedicated to your keys, `~/.ssh`  or `~/aws` are recommended.
 - Make the key private ` chmod 400 <key_name>.pem `.

2. When the EC2 is finished loading select the instance from the `EC2 Dashboard` and click on `Connect`
 - Make sure you are on the `SSH client` tab.
 - From here you need to get the user and IP.  You can copy the example that will look like ` ssh -i "<key_name>.pem" <user_name>@<ip address> `
    > The components to this command is making a connection to the given computer (IP address) as the given computer user (user name). The `-i` represents we are using a file that contains the password to allow the connection.  
    > Please note that if you created a Amazon Linux instance you will have to make sure the user name (the part before the @) is `ec2-user`
 
3. The command can be copied into your terminal in the folder with your PEM key and run.  A ssh connection will be made to the remote computer.
 - You will be asked if you are sure you wish to connect to this new system. answer yes.  You will be asked this every time you try to connect to a new IP address.
 - If you have not made your PEM key private you will not be able to connect.
 

**Note** If you ever wish to use Jupyter Notebooks locally that run on a cloud computer you can do something called [ssh tunneling](https://www.ssh.com/ssh/tunneling).  This will allow you to interact with something like Jupyter Notebook as if if was on your local system.    

The only change from the ssh command above is adding a parameter to the call.   
 
 ``` ssh -L localhost:8888:localhost:8888 -i "<key_name>.pem" <user_name>@<ip address> ```    
  
   >  The `-L localhost:8888:localhost:8888` tells the systems that any program that runs on port 8888 of the remote (the default Jupyter Notebook port) will be forwarded to the local computers port 8888.  This results in being able seemingly work on the local computer while the notebook is actually running on the remote computer.

 - A good walk through of this can be found [here](https://aws.amazon.com/blogs/machine-learning/get-started-with-deep-learning-using-the-aws-deep-learning-ami/).  This walk through focuses on using one of AWS Deep Learning images but the steps mentioned are the same regardless of the image you use.