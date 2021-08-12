import gym
import random

env = gym.make("FrozenLake-v0")
env.reset()
env.render()
reward = 0.00
forbidden = [5, 7, 11, 12]
actions = {
    'Left': 0,
    'Down': 1,
    'Right': 2,
    'Up': 3}
counter = 0
done = True
while done:
    counter = counter+1
    winning_sequence = [random.choice(["Left", "Down", "Right"]),
                        random.choice(["Left", "Down", "Right"]),
                        random.choice(["Left", "Down"]),
                        random.choice(["Left", "Down", "Right", "Up"])]
    for a in winning_sequence:
        new_state, reward, done, info = env.step(actions[a])
        print()
        env.render()
        print("Reward: {:.2f}".format(reward))
        if new_state in forbidden:
            env.reset()
            break
        if new_state == 15:
            done = False
            break
print("no.of attempts", counter)
print("the winning sequence", winning_sequence)
