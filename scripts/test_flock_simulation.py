import os
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.environ["SDL_VIDEODRIVER"] = "dummy"

from ple.games.flappybird import FlappyBird
from ple import PLE


game = FlappyBird()
p = PLE(game, fps=30, display_screen=True)
print(p.getActionSet())
# agent = myAgentHere(allowed_actions=p.getActionSet())
#
# p.init()
# reward = 0.0
#
# for i in range(30):
#    if p.game_over():
#            p.reset_game()
#
#    observation = p.getScreenRGB()
#    action = agent.pickAction(reward, observation)
#    reward = p.act(action)