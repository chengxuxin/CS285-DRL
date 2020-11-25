import numpy as np
import pdb


class ArgMaxPolicy(object):

    def __init__(self, critic):
        self.critic = critic

    def set_critic(self, critic):
        self.critic = critic

    def get_action(self, obs):
        # MJ: changed the dimension check to a 3
        if len(obs.shape) > 3:
            observation = obs
        else:
            observation = obs[None]

        # TODO: get this from hw3
        # MJ: changed the dimension check to a 3

        ## TODO return the action that maxinmizes the Q-value 
        # at the current observation as the output
        q_values = self.critic.qa_values(observation)
        action = q_values.argmax(-1)

        return action[0]

    ####################################
    ####################################