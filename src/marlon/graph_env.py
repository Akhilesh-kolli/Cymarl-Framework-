import numpy as np
import gym
from gym import spaces


class GraphCyberEnv(gym.Env):
    """
    Research-ready Cyber MARL Environment
    Graph-based attack/defense simulation
    """

    def __init__(self, node_count=6, max_steps=25):
        super(GraphCyberEnv, self).__init__()

        self.node_count = node_count
        self.max_steps = max_steps

        # ---- Network topology (adjacency matrix) ----
        # Example enterprise network layout
        self.graph = np.array([
            [0,1,1,0,0,0],
            [1,0,1,1,0,0],
            [1,1,0,1,1,0],
            [0,1,1,0,1,1],
            [0,0,1,1,0,1],
            [0,0,0,1,1,0],
        ], dtype=np.int32)

        # ---- Critical nodes (high-value servers) ----
        self.critical_nodes = {2,4}

        # ---- Gym spaces ----
        self.action_space = spaces.Discrete(self.node_count + 1)

        self.observation_space = spaces.Box(
            low=0,
            high=1,
            shape=(self.node_count,),
            dtype=np.float32
        )

        self.reset()

    # --------------------------------------------------
    # RESET
    # --------------------------------------------------
    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.state = np.zeros(self.node_count, dtype=np.float32)

        # initial foothold
        entry = np.random.randint(0, self.node_count)
        self.state[entry] = 1

        self.current_step = 0
        return self.state.copy()

    # --------------------------------------------------
    # STEP
    # --------------------------------------------------
    def step(self, action):
        action = int(action)
        
        self.current_step += 1
        reward = 0.0

        # ---------- ATTACK ACTION ----------
        if action < self.node_count:

            compromised = np.where(self.state == 1)[0]

            # check if reachable from compromised nodes
            reachable = False
            for node in compromised:
                if self.graph[node, action] == 1:
                    reachable = True
                    break

            if reachable and self.state[action] == 0:
                self.state[action] = 1
                reward = 1.0

                # bonus for critical nodes
                if action in self.critical_nodes:
                    reward += 1.0

            else:
                reward = -0.3

        # ---------- DEFENDER ACTION ----------
        else:
            compromised = np.where(self.state == 1)[0]

            if len(compromised) > 0:
                node = np.random.choice(compromised)
                self.state[node] = 0
                reward = 0.6
            else:
                reward = -0.1

        done = self.current_step >= self.max_steps
        return self.state.copy(), reward, done, {}

    # --------------------------------------------------
    # RENDER
    # --------------------------------------------------
    def render(self):
        print(f"Step {self.current_step}: {self.state}")
