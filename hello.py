import os

if __name__ == '__main__':
	f = open(os.environ['OUTPUT_PATH'], 'w')
    f.write('hello world final') 
    f.write('testing it part 2')
    f.write('last test2')
    f.write('test review test')
    f.write('this is a comment')