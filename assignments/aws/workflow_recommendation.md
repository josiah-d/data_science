# Frictionless Cloud Computing

Here's what to do:
1. Create an EC2 instance with permission to write to s3 (without ever having to copy your AWS credentials to the instance!)
 
    -  Go to AWS Console
    -  Choose Roles
    -  Create Role
    -  AWS Service -> EC2, click Next: Permissions
    -  Search box -> type S3 -> check AmazonS3FullAccess, Next: Review
    -  Create Role
    -  Now, create a new EC2 instance (or choose an existing one) and assign it the IAM role that you just created. It will appear on a dropdown list.
    -  SSH into your EC2 instance and use `aws s3 cp <origin> <destination> to copy a file from EC2 to s3!
2. Create a new github repository with source code for your project. Just like normal.
3. Clone github repository onto your EC2 instance to keep your code and compure resources synced. 
    - You can go straight ahead and `git clone https://github.com/username/reponame` to your EC2 instance and your done.  
    - To remove the friction of supplying your username/password every time you push/pull, run the following commands **on your remote machine**:
        - Create an SSH key: `ssh-keygen -b 4096`
        - Tell SSH to use it. (this assumes that there's no existing SSH config on the instance) `echo "IdentityFile ~/.ssh/id_rsa" > ~/.ssh/config`
        - Then copy and paste the public key as a new authorized SSH key on GitHub `cat ~/.ssh/id_rsa.pub`
        - Then `git clone git@github.com:username/reponame` just works.
4. Write code on your local machine (or your remote instance!), and keep all machines synced with frequent add/commit/push/pull.  This is the beauty of version control!
5. That's it!
