import gym
from stable_baselines3 import PPO

env = gym.make("CartPole-v1")

# ===== Gym 0.26 → SB3 1.8 compatibility =====
orig_reset = env.reset
def reset_fix(**kwargs):
    obs, info = orig_reset(**kwargs)
    return obs
env.reset = reset_fix

orig_step = env.step
def step_fix(action):
    obs, reward, terminated, truncated, info = orig_step(action)
    done = terminated or truncated
    return obs, reward, done, info
env.step = step_fix
# ===========================================

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=1000)

print("Training completed successfully")
