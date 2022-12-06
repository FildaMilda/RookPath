

class Square:

    def __init__(self, distance, start=False, end=False):

        self.distance = distance
        self.visited = False
        self.start = start
        self.end = end

    def __repr__(self):
        return f"{self.distance}"

    def set_distance(self, distance):
        self.distance = distance

class chessBoard:

    def __init__(self):

        self.width = 8
        self.height = 8

        self.moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def decode_input(self):

        row = [[] for _ in range(self.height)]
        self.board = [list(row) for _ in range(self.width)]

        for r in range(self.height):
            input_row = input()
            
            c = 0
            for char in input_row:

                if char == ".":
                    self.board[r][c] = Square(-1)

                elif char == "x":
                    self.board[r][c] = Square(-2)

                elif char == "v":
                    self.board[r][c] = Square(0, True)
                    self.start = (r, c)

                elif char == "c":
                    self.board[r][c] = Square(-1, end=True)
                    self.end = (r, c)

                c += 1

        return self.board

    def set_distance(self, r, c, distance):
        self.board[r][c] = distance

    def idk(self, squares):

        visited_squares = []

        for square in squares:
            for move in self.moves:

                r, c = square

                for _ in range(self.width):

                    r += move[0]
                    c += move[1]

                    if r in range(0, self.height) and c in range(0, self.width):
                        if self.board[r][c].distance == -2:
                            break
                        
                        else:
                            if not self.board[r][c].visited and self.start != (r, c):

                                self.board[r][c].visited = True
                                self.board[r][c].distance = self.board[square[0]][square[1]].distance + 1
                                visited_squares.append((r, c))

        return visited_squares

    def all_squares_visited(self):

        for row in self.board:
            for square in row:

                if square.distance == -1 and not square.visited:
                    return False

        return True

    def run(self):

        self.decode_input()
        vis_squares = self.idk([self.start])

        for _ in range(100):

            if self.all_squares_visited():
                print(self.board[self.end[0]][self.end[1]].distance)
                break

            else:
                vis_squares = self.idk(vis_squares)

        else:
            print(self.board[self.end[0]][self.end[1]].distance)

c = chessBoard()
c.run()
