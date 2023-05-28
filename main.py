# Define environment 
import gymnasium as gym
env = gym.make("ALE/Breakout-v5", render_mode = 'human')

done = False
while not done:
    state = env.reset()
    action = env.action_space.sample()
    print(action) 
    # action_space = Discrete(4) 
    # 0 NOOP (No action)
    # 1 FIRE
    # 2 RIGHT
    # 3 LEFT
    # state, action, reward, done = 
    env.step(action)
    env.render()

env.close()

# Define agent

# Define DQN network

# Define experience replay

# Define data pre-processing
