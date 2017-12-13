import neat
import pickle
import sys
from FlapPyBird.flappy import FlappyBirdApp


def run_winner(n=1):
    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         'config')
    
    #load Gnome
    genomes = pickle.load(open('winner.pkl', 'rb'))
    
    for i in range(0,n):
        # Play game and get results
        flappy_Bio = FlappyBirdApp([genomes], config)
        flappy_Bio.play()

def main():
    if len(sys.argv)>1:
        run_winner(int(sys.argv[1]))
    else:
        run_winner()

if __name__ == "__main__":
	main()