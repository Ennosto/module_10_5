import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='UTF8') as file:
        readline_ = file.readline()
        for string in readline_:
            all_data.append(string)


filenames = [f'./file {number}.txt' for number in range(1, 5)]
print(filenames)

start_time = time.time()
read_info(filenames[0])
read_info(filenames[1])
read_info(filenames[2])
read_info(filenames[3])
finish_time = time.time()

print(f'Время линейного запуска в милисекундах: {(finish_time-start_time) * 1000}')

if __name__ == '__main__':
    start_time = time.time()
    process_1 = multiprocessing.Process(target=read_info(filenames[0]),)
    process_2 = multiprocessing.Process(target=read_info(filenames[1]),)
    process_3 = multiprocessing.Process(target=read_info(filenames[2]),)
    process_4 = multiprocessing.Process(target=read_info(filenames[3]),)
    finish_time = time.time()
    print(f'Время в многопроцессорного запуска милисекундах: {(finish_time-start_time) * 1000}')
