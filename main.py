import gymnasium as gym
import matplotlib.pyplot as plt

#create our training environment
env = gym.make('FrozenLake-v1', render_mode='human')
#reset the environment to start a new episode
observation, info = env.reset()

print("_____OBSERVATION SPACE_____ \n")
print("Observation Space Shape", env.observation_space.shape)
print("Sample observation", env.observation_space.sample())

print("\n _____ACTION SPACE_____ \n")
print("Action Space Shape", env.action_space.n)
print("Action Space Sample", env.action_space.sample())

for _ in range(1000):
    action = env.action_space.sample()

    observation, reward, terminated, truncated, info = env.step(action)

    #if the game is terminated or truncated(timeout)
    if terminated or truncated:
        #reset the environment
        print("Environment is reset")
        observation, info = env.reset()

env.close()

