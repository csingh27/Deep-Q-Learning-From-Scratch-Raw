# Define environment 
import gymnasium as gym
env = gym.make("ALE/Breakout-v5", render_mode = 'human')
import torch as t
import cv2
import numpy as np
import pandas as pd

# A1 Environment
# A1.1 Install packages
# A1.2 Create environment
# A1.3 Understanding action space
# A1.4 Taking random actions
# A1.5 Rendering actions
# A1.6 Understanding observation space


# A3.2 Define a dataframe for experience replay buffer
columns = ["State", "Action", "Reward", "Done"]
rb = pd.DataFrame(columns=columns)

# A2 Dataset pre-processing
def frame_preprocessing(frame):
    # A2 Dataset preprocessing
    # A2.1 Convert RGB to gray scale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # A2.2 Downsampling to 110x84
    new_width = 110
    new_height = 84
    downsampled_frame = cv2.resize(gray_frame, (110, 84))
    # A2.3 Cropping the image
    state = downsampled_frame[110-84:,:]
    return state

# A3 Define replay buffer
def experience_replay(s, a, r, d):
    rb.loc[len(rb)] = [state, action, reward, done]
    return rb

def mini_batch(rb):
    return 0

def state_sequence():
    return 0

done = False
while not done:
    state = env.reset()
    frame = np.asarray(state[0])
    # print(frame.shape)

    state = frame_preprocessing(frame)
    # print(state.shape)

    # Random action
    action = env.action_space.sample()
    print(action) 
    # action_space = Discrete(4) 
    # 0 NOOP (No action)
    # 1 FIRE
    # 2 RIGHT
    # 3 LEFT
    # state, action, reward, done = 
    # A3.1 Define state, action, reward
    state, action, reward, done, truncate = env.step(action) # truncate is when the episode length exceeds the set timelimit
    replay_buffer = experience_replay(state, action, reward, done)
    print(replay_buffer)

    # frame = env.render()
    # print(env.observation_space)

    # Display frame
    # cv2.imshow("Frame", frame)
    # cv2.imshow("State", state)
    # cv2.waitKey(0)

env.close()

# Define agent
# def dqn: 


# Define DQN network

# Define experience replay

# Define data pre-processing
