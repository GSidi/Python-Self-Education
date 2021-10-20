import time
import multiprocessing

square_result = []
cube_result = []

def calc_square(numbers):
    global square_result
    for n in numbers:
        sq = n*n
        print("Square is: ", sq)
        square_result.append(sq)
        print("Square results: " , str(square_result))
        

def calc_cube(numbers):
    global cube_result
    for n in numbers:
        cu = n*n*n
        print("Cube is: ", cu)
        cube_result.append(cu)
        print("Cube results: " , str(cube_result))



if __name__ == "__main__":
    arr = [1,2,3,4,5]
    p1 = multiprocessing.Process(target=calc_square,args=(arr, ))
    p2 = multiprocessing.Process(target=calc_cube,args=(arr, ))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

 
    
    print("FINITO LA MUSICA")
