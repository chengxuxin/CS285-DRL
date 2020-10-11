import numpy as np
import cs285.infrastructure.pytorch_util as ptu

class ArgMaxPolicy(object):

    def __init__(self, critic):
        self.critic = critic

    def get_action(self, obs):
        if len(obs.shape) > 3:
            observation = obs
        else:
            observation = obs[None]
        
        ## TODO return the action that maxinmizes the Q-value 
        # at the current observation as the output
        observation = ptu.from_numpy(observation)
        q_values = self.critic.q_net(observation).detach()
        q_values = ptu.to_numpy(q_values)
        # print(q_values.shape)
        actions = np.argmax(q_values, axis=1)
        # print(actions.shape)
        return actions