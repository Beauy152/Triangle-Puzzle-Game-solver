from pieces import *
from copy import deepcopy,copy
from time import perf_counter
from multiprocessing import Process

pieces = getPieces()
solutions = []

#function to check if board it complete?
#check num remaining pieces, if 0 then save solution?
def Solve(piece,available=None,board=None,s_r=0,s_i=1):
    if board is None: board = getBoard()
    if available is None: available = pieces.copy()
    def check(row,index):
        #add extra check if final row
        #if index is even/odd, we can determine required orientation
        req_orientation = DOWN if index % 2 == 0 else UP
        #check correct piece orientation, if wrong, fix it
        #rotating once swaps orientations
        if piece.orientation != req_orientation: piece.rotate(1)

        middle_match = board[row+1][index].m if board[row+1][index] is not None else None
            

        to_match = [board[row][index-1].r,
                    middle_match if req_orientation is UP else board[row-1][index-1].m,
                    board[row][index+1].l if board[row][index+1] is not None else None]

        for _ in range(3):#2
            match = False
            p_cols = piece.getCols() 
            if (p_cols[0] == to_match[0]) and (p_cols[-1] == to_match[-1] \
                or to_match[-1] is None):#l & r match
                if p_cols[1] == to_match[1] or to_match[1] is None:#match above middle if piece in down orientation
                    match = True
                    break
                else:
                    piece.rotate_2()
            else:
                piece.rotate_2()
        return match

    #find next position
    available.remove(piece)

    if check(s_r,s_i):#if piece fits, check next piece pos
        board[s_r][s_i] = piece

        if len(available) == 0: print(board)#solutions.append(deepcopy(board))

        if s_i == len(board[s_r])-2 :#max index of given row
            s_r += 1
            s_i = 1
        else: s_i += 1 

        for p in available:
            Solve(p,available.copy(),deepcopy(board),s_r,s_i)
    

#main
def main():
    num_processors = 6 # change to num of pieces
    jobs = []
    for piece in pieces:
        p = Process(target=Solve, args=(piece,pieces.copy()))
        jobs.append(p)
        p.start()
        p.i

    for job in jobs:
        if not job.is_alive():
            
    #start_time = perf_counter()

    # for piece in pieces:
    #     Solve(piece)

    #
    # print(f"Solutions calculated in {perf_counter() - start_time:0.4f} Seconds...")
    # print("found {0} solutions...".format(len(solutions)))
    # for i,s in enumerate(solutions):
    #     print("solution {0}:".format(i))
    #     for line in s:
    #         print(line)
if __name__ == "__main__":
    main()