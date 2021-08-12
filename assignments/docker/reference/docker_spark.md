# Using Spark & PySpark with Docker
Courtesy Moses Marsh, Lead DSI instructor  

## Downloading and running the container
We will be using docker images provided by Jupyter Docker Stacks. The user guide is [here](https://jupyter-docker-stacks.readthedocs.io/en/latest/). The following instructions are adapted from the user guide.

To create and start a container with Spark, PySpark, SciPy, and Jupyter, run the following command in your terminal.
```bash
$ docker run --name sparkbook -p 8881:8888 -v "$PWD":/home/jovyan/work jupyter/pyspark-notebook start.sh jupyter lab --LabApp.token=''
```
- this will take a while to download the first time you run it
- here I've given this container the name `sparkbook`. You can call it whatever you like.
- the `-p` flag is exposing port `8881`, so as not to collide with any other notebooks you have running.
- the `-v` flag connects the filesystem in the container to your computer's filesystem. See the documentation for [docker volumes](https://docs.docker.com/storage/volumes/). 
  - Here, the container's folder `/home/jovyan/work` will be mapped to whichever folder you ran the `docker run` command from (`$PWD`). If you want to make your entire home folder visible to the docker container, navigate to `~` before running the above command. If you only want the container to see, say, a folder you cloned from github, navigate to `/path/to/repo_folder` first. Then you can **make changes from inside the container** and **run git commands outside the container** 
  - For Windows you will have to change the `$PWD` in the above command. 
- `start.sh` is a script in the container that allows for notebook configuration
- `--LabApp.token=''` turns off secured access. Remove this flag if you are ever doing anything serious. 
- If you want to run the server in the background, add the docker flag `-d` to the above command

To stop the container, type in a different terminal window
```bash
$ docker stop sparkbook
```

To start this container up in the future, you only need to type
```bash
$ docker start sparkbook
```


## Accessing the Jupyter server running in the container

In your web browser, go to `localhost:8881`. Ta-da!

## PySpark

Open a new notebook and paste the following code
```python
import pyspark as ps
import random

spark = (ps.sql.SparkSession.builder
        .appName("sandbox")
        .getOrCreate()
        )

sc = spark.sparkContext

random.seed(1)

def sample(p):
    x, y = random.random(), random.random()
    return 1 if x*x + y*y < 1 else 0

count = (sc.parallelize(range(0, 10000000))
           .map(sample)
           .reduce(lambda a, b: a + b)
        )

print("Pi is (very) roughly {}".format(4.0 * count / 10000000))
```
If this code runs, you are ready.

## One last thing

To do the afternoon exercise, you need to install `nltk` and nltk packages on the container.

```bash
$ docker exec -it sparkbook bash
jovyan@839db31a6a90:~$ pip install nltk
jovyan@839db31a6a90:~$ python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('averaged_perceptron_tagger')
>>> exit()
jovyan@839db31a6a90:~$ exit
$
```
