#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gym
from gym import spaces
import numpy as np
import random
import matplotlib.pyplot as plt

class GridWorldEnv:
    def __init__(self, size, initial_state=(0, 0), obstacles=[(1, 1), (2, 2)], goal_position=(3, 3)):
        super(GridWorldEnv, self).__init__()
        self.size = size
        self.state = initial_state  # Start at top-left corner
        self.goal_position = goal_position  # Set the goal position
        self.obstacles = obstacles
        self.action_space = spaces.Discrete(4)  # 0: Up, 1: Down, 2: Left, 3: Right

    def reset(self):
        self.state = (0, 0)  # Reset the start at top-left corner
        return self.state

    def step(self, action):  # 0: Up, 1: Down, 2: Left, 3: Right
        x, y = self.state
        if action == 0 and x > 0: x -= 1
        elif action == 1 and x < self.size - 1: x += 1
        elif action == 2 and y > 0: y -= 1
        elif action == 3 and y < self.size - 1: y += 1

        new_state = (x, y)

        # Assign default reward (penalty) for each move
        reward = -1
        done = False
        if new_state == self.goal_position:  # Reward for reaching the goal
            reward = 10
            done = True
        elif new_state in self.obstacles:  # Penalty for hitting an obstacle
            reward = -10

        self.state = new_state
        return new_state, reward, done

    # Grid Display
    def render(self):
        grid = np.zeros((self.size, self.size))
        grid[self.state] = 7  # Current position
        grid[self.goal_position] = 99  # Goal
        for obs in self.obstacles:
            grid[obs] = 44  # Obstacle
        print(grid)

class QLearningAgent:
    def __init__(self, n_states, n_actions, size, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0):
        self.q_table = np.zeros((n_states, n_actions))  # Initialize the q table with 0.
        self.size = size
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.max_exploration_rate = 1.0
        self.min_exploration_rate = 0.01
        self.exploration_decay_rate = 0.001

    def choose_action(self, state):
        # self.exploration_rate indicates epsilon for epsilon-greedy RL strategy
        if random.uniform(0, 1) < self.exploration_rate:  # Exploration
            return random.randint(0, 3)  # randomly selects an action from 0 to 3
        else:
            state_index = self.grid_to_index(state)
            return np.argmax(self.q_table[state_index])  # Exploit using the Q-table

    def learn(self, state, action, reward, next_state):
        state_index = self.grid_to_index(state)
        next_state_index = self.grid_to_index(next_state)
        old_value = self.q_table[state_index, action]
        next_max = np.max(self.q_table[next_state_index])

        # Q-Learning formula
        self.q_table[state_index, action] = old_value + self.learning_rate * (reward + self.discount_factor * next_max - old_value)

    def grid_to_index(self, position):
        x, y = position
        return x * self.size + y

def main():
    env = GridWorldEnv(size=4)
    agent = QLearningAgent(n_states=16, n_actions=4, size=4)

    
    total_episodes = 10  # Run for 10 episodes
    max_steps_per_episode = 20

    steps_per_episode = []
    successes = []
    total_rewards = []

    for episode in range(total_episodes):
        state = env.reset()
        total_reward = 0
        step_count = 0
        episode_success = 0
        print(f'*************Episode {episode + 1}*************\n')
        print('Steps taken in this episode are as following: \n')
        for step in range(max_steps_per_episode):
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.learn(state, action, reward, next_state)

            state = next_state
            total_reward += reward
            step_count += 1
            print(f"Step {step_count}: Action taken - {action}, Reward - {reward}, New State - {state}")
            if (step + 1) % 5 == 0:  # Display grid after every 5 steps
                env.render()

            if done:
                episode_success = 1  # Mark success if the goal is reached
                break
            
        # Collect data for plots
        steps_per_episode.append(step_count)
        total_rewards.append(total_reward)
        successes.append(episode_success)

        # Display Q-table after each episode
        # print(f'\n\n*****Episode {episode + 1}*****')
  
        print("\n\nTotal rewards for this episode:", total_rewards[episode])
        print('\nQ-Table for this episode:\n')
        print(agent.q_table)
        print('\n')
        # Decay exploration rate
        agent.exploration_rate = max(agent.min_exploration_rate, agent.exploration_rate * np.exp(-agent.exploration_decay_rate * episode))


 

if __name__ == "__main__":
    main()





