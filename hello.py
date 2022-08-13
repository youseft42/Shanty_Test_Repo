import os

if __name__ == '__main__':
	f = open(os.environ['OUTPUT_PATH'], 'w')
    f.write('hello world final') 
    f.write('testing it')