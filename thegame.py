import matplotlib.pyplot as plt
import numpy as np
import numpy.matlib as mat
import matplotlib.animation as animation


class State():

    def __init__(self, world_state):
        self.world_state = world_state

    @property
    def shape(self):
        return self.world_state.shape

    def get_point(self, x, y):
        return self.world_state[x,y]

    def update_next_gen(self):
        self.world_state = self.calc_next_gen()
        return self

    def calc_next_gen(self):
        next_world_state = np.zeros(self.world_state.shape)
        for i in range(0,self.world_state.shape[0]):
            for j in range(0,self.world_state.shape[1]):
                if self.world_state[i,j]: # previously alive
                    if 2 <= self.count_live_neighbors(i,j) <= 3: #under/overpopulation will kill
                        next_world_state[i,j] = 1
                else: # previously dead
                    if self.count_live_neighbors(i,j) == 3: #reproduction
                        next_world_state[i, j] = 1
        return next_world_state

    def count_live_neighbors(self, i, j):
        buffered_world_state = np.zeros((self.world_state.shape[0]+2,self.world_state.shape[1]+2))
        buffered_world_state[1:-1,1:-1] = self.world_state
        buffered_world_state[i+1,j+1] = 0
        return np.sum(buffered_world_state[i:i+3,j:j+3])

    def override_local_state(self, location, local_state):
        back_spaces_x = int(np.floor(local_state.shape[0] / 2))
        forward_spaces_x = int(np.ceil(local_state.shape[0] / 2))
        back_spaces_y = int(np.floor(local_state.shape[1] / 2))
        forward_spaces_y = int(np.ceil(local_state.shape[1] / 2))
        x_start = location[0] - back_spaces_x
        x_end = location[0] + forward_spaces_x
        y_start = location[1] - back_spaces_y
        y_end = location[1] + forward_spaces_y
        self.world_state[x_start:x_end, y_start:y_end] = local_state


class Drawer():

    @staticmethod
    def make_empty_grid(board_size, small_square_size_px):
        empty_square = np.ones((small_square_size_px, small_square_size_px)) * 0.2
        empty_square[1:-1, 1:-1] = np.zeros((small_square_size_px - 2, small_square_size_px - 2))
        return mat.repmat(empty_square, board_size[0], board_size[1])

    @staticmethod
    def draw(state, small_square_size_px):
        empty_board = Drawer.make_empty_grid(state.shape, small_square_size_px)
        for i in range(0,state.shape[0]):
            for j in range(0,state.shape[1]):
                if state.get_point(i,j):
                    empty_board[i*small_square_size_px:(i+1)*small_square_size_px,
                    j*small_square_size_px:(j+1)*small_square_size_px] = Drawer.create_full_square(small_square_size_px)
        return plt.imshow(empty_board)

    @staticmethod
    def create_empty_square(small_square_size_px):
        empty_square = State.create_full_square(small_square_size_px)
        empty_square[1:-1, 1:-1] = np.zeros((small_square_size_px - 2, small_square_size_px - 2))
        return empty_square

    @staticmethod
    def create_full_square(small_square_size_px):
        empty_square = np.ones((small_square_size_px, small_square_size_px))
        return empty_square

class Animator():

    @staticmethod
    def start_animation(state):
        print('started!')
        fig = plt.figure("The Game of Life G+N")
        Z = []
        img = []
        frames_to_animate = 300
        small_square_size_px = 5
        for i in range(frames_to_animate):
            next_state = State(state.calc_next_gen())
            state = next_state
            Z.append(next_state)
            img.append([Drawer.draw(state, small_square_size_px)])
        print('animating!')
        ani = animation.ArtistAnimation(fig, img, interval=50, blit=True, repeat_delay=0)
        print('saving!')
        ani.save('gol.mp4')
        print('done!')
        plt.show()

class KnownCreatureFactory():

    @staticmethod
    def create_glider():
        state = np.zeros((3,3))
        state[0, 2] = 1
        state[1, 2] = 1
        state[2, 2] = 1
        state[2, 1] = 1
        state[1, 0] = 1
        return state

    @staticmethod
    def create_tub():
        state = np.zeros((3, 3))
        state[0, 1] = 1
        state[1, 0] = 1
        state[1, 2] = 1
        state[2, 1] = 1
        return state

    @staticmethod
    def create_acorn():
        state = np.zeros((7, 3))
        state[0, 0] = 1
        state[1, 0] = 1
        state[4, 0] = 1
        state[5, 0] = 1
        state[6, 0] = 1
        state[3, 1] = 1
        state[1, 2] = 1
        return state

if __name__ == "__main__":

    world = np.zeros((80,80))

    start_world = State(world)

    start_world.override_local_state((4,5),KnownCreatureFactory.create_glider())
    start_world.override_local_state((8,9),KnownCreatureFactory.create_glider())
    start_world.override_local_state((40,35),KnownCreatureFactory.create_tub())
    start_world.override_local_state((40, 40), KnownCreatureFactory.create_tub())

    # start_world.override_local_state((20,20), KnownCreatureFactory.create_acorn())

    Animator.start_animation(start_world)

    # start_world.draw(5)
    # plt.show()
