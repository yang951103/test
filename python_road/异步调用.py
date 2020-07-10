from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

import time,random,os



def task(n):

    print('%s is ruuning' %os.getpid())

    time.sleep(random.randint(1,3))

    # res=n**2

    # handle(res)

    return n**2



def handle(res):

    res=res.result()

    print('handle res %s' %res)



if __name__ == '__main__':

    #异步调用

    pool=ProcessPoolExecutor(2)



    for i in range(5):

        obj=pool.submit(task,i)

        obj.add_done_callback(handle) #handle(obj)



    pool.shutdown(wait=True)

    print('主')