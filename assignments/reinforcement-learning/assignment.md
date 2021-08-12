# Reinforcement Learning
- [Reinforcement Learning](#reinforcement-learning)
  - [Introduction](#introduction)
  - [Basic](#basic)
    - [Part 1: Prepare the environments](#part-1-prepare-the-environments)
    - [Part 2: Random walk solution](#part-2-random-walk-solution)
  - [Advanced](#advanced)
    - [Part 3: Q-learning solution](#part-3-q-learning-solution)
    - [Part 4: `Deep` Q-learning solution](#part-4-deep-q-learning-solution)
## Introduction

Open AI gym comes with many reinforcement learning [environments](https://gym.openai.com/envs/). However,
these models can take a long time to train, so in the interest of getting results in a reasonable period of time the [toy text environments](https://gym.openai.com/envs/#toy_text) are recommended. Specifically in this assignment, we are going to use the [frozen lake](https://gym.openai.com/envs/FrozenLake-v0/) environment.

You are going to walk on a `4 x 4` frozen lake represented by a piece of text as following.

```plaintext
SFFF       (S: starting point, safe)
FHFH       (F: frozen surface, safe)
FFFH       (H: hole, fall to your doom)
HFFG       (G: goal, where the frisbee is located)
```

## Basic

In the basic part, we are going to prepare the environment and run a random walk example.

### Part 1: Prepare the environments

There are some libraries to run reinforcement learning with Keras/Tensorflow but the dependency is kind of messy, for example not supporting TF2. We have created a [`requirements.txt`](./requirements.txt) for you. Set up a virtual environment using `conda` or `virtualenv` and install the dependency.

If you have difficulty using `pip install -r requirements.txt`, you may need to install the following specific version of `keras` and `keras-rl2` directly.

```shell
pip install keras==2.3.1 #The latest keras version that doesn't requrie TF 2.2+
git clone https://github.com/wau/keras-rl2.git
cd keras-rl
python install .
```


> Note, if you can't set up the environment, you can still continue to complete part 2 and part 3. Only [part 4](#part-4-deep-q-learning-solution) requires `keras-rl2==1.0.4`. Move on if you spend more than 10 minutes setting up the environment.

### Part 2: Random walk solution

The random walk solution is provided for you in [src/random_walk.py](src/random_walk.py), run it and understand the code.

## Advanced

In the advanced part, we are going to implement the Q-learning by either explicitly using the update rule or letting a neural network learn the Q function. Note that your solution may look different from the solution, which is totally fine.

### Part 3: Q-learning solution

Recall that in the lecture note, the Q-function update rule works as following.

```python
def eps_greedy_q_learning_with_table(env, num_episodes=100):
    q_table = np.zeros((5, 2)) # what is the dimension in the frozen lake case?
    y = 0.95 # discount factor
    eps = 0.5 # epsilon-greedy explore threshold
    lr = 0.8 # learning rate
    decay_factor = 0.99999 # as time goes on, decrease willingness to explore
    for i in range(num_episodes):
        if i % 25 == 0: 
            print("Episode {0}".format(i))
        s = env.reset()
        eps *= decay_factor
        done = False
        while not done:
            # select the action with highest cumulative reward
            if np.random.random() < eps or np.sum(q_table[s, :]) == 0:
                a = np.random.randint(0, 2)
            else:
                a = np.argmax(q_table[s, :])
            new_s, r, done, _ = env.step(a)
            q_table[s, a] = (1 - lr) * q_table[s, a] + lr * (r + y * np.max(q_table[new_s, :]))
            s = new_s
    return q_table
```

What you need to do is to modify this algorithm to apply it on the frozen lake enviornment. The following code snippet might be helpful for you to initialize the `Q` table.

```python
Q = np.zeros([env.observation_space.n, env.action_space.n])
```

Run `2000` episodes, in your code, also document the rewards for the `2000` runs. Calculate the highest average rewards for `consecutive 100 runs`. How large is it? For example, if the average reward for runs from the 1800th to the 1900th is the highest and it is 0.94 then your result is 0.94.

### Part 4: `Deep` Q-learning solution

Recall in the lecture, the vanilla `Keras` code for deep Q-learning is as following.

```python
def q_learning_keras(env, num_episodes=150):
    # create the keras model
    model = Sequential()
    model.add(InputLayer(batch_input_shape=(1, 5)))
    model.add(Dense(10, activation='sigmoid'))
    model.add(Dense(2, activation='linear'))
    model.compile(loss='mse', optimizer='adam', metrics=['mae'])
    # now execute the q learning
    y = 0.95
    eps = 0.5
    decay_factor = 0.999
    r_avg_list = []
    for i in range(num_episodes):
        s = env.reset()
        eps *= decay_factor
        if i % 25 == 0:
            print("Episode {} of {}".format(i + 1, num_episodes))
        done = False
        r_sum = 0
        while not done:
            if np.random.random() < eps:
                a = np.random.randint(0, 2)
            else:
                a = np.argmax(model.predict(np.identity(5)[s:s + 1]))
            new_s, r, done, _ = env.step(a)
            target = r + y * np.max(model.predict(np.identity(5)[new_s:new_s + 1]))
            target_vec = model.predict(np.identity(5)[s:s + 1])[0]
            target_vec[a] = target
            model.fit(np.identity(5)[s:s + 1], target_vec.reshape(-1, 2), epochs=1, verbose=0)
            s = new_s
            r_sum += r
        r_avg_list.append(r_sum / 1000)
    plt.plot(r_avg_list)
    plt.ylabel('Average reward per episode')
    plt.xlabel('Number of episodes')
    plt.show()
    for i in range(5):
        print("State {} - action {}".format(i, model.predict(np.identity(5)[i:i + 1])))
```

You have two options to complete this part.

1. You can modify the code above to apply it to the frozen lake environment.
2. Or you can choose to use `keras-rl2`. A code sample is provided as listed [here](https://gist.github.com/rongpenl/c0a8e183575acdf9ab4f368f260467de). However, the code example is outdated due to the bump from `keras-rl` to `keras-rl2`. You may need to study the official [keras-rl2 examples](https://github.com/wau/keras-rl2/tree/master/examples) to get it all working.

Once your code works, similar to part 3, calculate the highest average reward for `consecutive 100 runs`. Is your score lower or higher?
