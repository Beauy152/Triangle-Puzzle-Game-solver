from pieces import *
from copy import deepcopy,copy
from time import perf_counter
from multiprocessing import Pool,freeze_support

pieces = getPieces()
solutions = []


# def multiprocess(func,n_processors):
#     with Pool(processes=n_processors) as pool:
#         return pool.map(func,pieces)

#function to check if board it complete?
#check num remaining pieces, if 0 then save solution?
def Solve(piece,available=None,board=getBoard(),s_r=0,s_i=1,depth=1):
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

        for _ in range(3):#3
            match = False
            p_cols = piece.getCols() 
            if (p_cols[0] == to_match[0]) and \
                (p_cols[-1] == to_match[-1] or to_match[-1] is None):#l & r match
                if p_cols[1] == to_match[1] or to_match[1] is None:#match above middle if piece in down orientation
                    match = True
                    break
                else:
                    piece.rotate_2()
            else:
                piece.rotate_2()
        return match
    print(depth)
    print(piece)
    if depth == 1: available = pieces.copy()
    #find next position
    available.remove(piece)

    if check(s_r,s_i):#if piece fits, check next piece pos
        board[s_r][s_i] = piece

        if len(available) == 0: solutions.append(deepcopy(board))

        if s_i == len(board[s_r])-2:#max index of given row
            s_r += 1
            s_i = 1
        else:
            s_i += 1 


        for p in available:
            temp_board = deepcopy(board)
            Solve(p,available.copy(),temp_board,s_r,s_i,depth+1)
    
#main
def main():
    # time_start = perf_counter()
    #
    num_processors = 6 # change to num of pieces
    #
    # params = []
    # for piece in pieces:
    #     params.append([piece,pieces.copy()])
        #Solve(piece,pieces.copy())

    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
    #results = multiprocess(Solve,num_processors)#(0,1,getBoard(),piece,pieces.copy())
    #print(results)
    

    # print("found {0} solutions...".format(len(solutions)))

    # for i,s in enumerate(solutions):
    #     print("solution {0}:".format(i))
    #     for line in s:
    #         print(line)


if __name__ == "__main__":
    freeze_support()
    main()