# Define environment 
import gymnasium as gym
env = gym.make("ALE/Breakout-v5", render_mode = 'human')
import torch as t
import cv2
import numpy as np

# A1 Environment
# A1.1 Install packages
# A1.2 Create environment
# A1.3 Understanding action space
# A1.4 Taking random actions
# A1.5 Rendering actions
# A1.6 Understanding observation space

done = False
while not done:
    state = env.reset()
    # Random action
    action = env.action_space.sample()
    print(action) 
    # action_space = Discrete(4) 
    # 0 NOOP (No action)
    # 1 FIRE
    # 2 RIGHT
    # 3 LEFT
    # state, action, reward, done = 
    env.step(action)
    # frame = env.render()
    print(env.observation_space)
    frame = np.asarray(state[0])
    print(frame.shape)
    cv2.imshow("Frame", frame)
    cv2.waitKey(0)

env.close()

# Dataset pre-processing

# Define agent
# def dqn: 


# Define DQN network

# Define experience replay

# Define data pre-processing
