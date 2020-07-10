from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

import time,random,os



def task(n):

    print('%s is ruuning' %os.getpid())

    time.sleep(random.randint(1,3))

    return n**2



def handle(res):

    print('handle res %s' %res)



if __name__ == '__main__':

    #同步调用

    pool=ProcessPoolExecutor(2)



    for i in range(5):

        res=pool.submit(task,i).result()

        # print(res)

        handle(res)



    pool.shutdown(wait=True)

    # pool.submit(task,33333)

    print('主')