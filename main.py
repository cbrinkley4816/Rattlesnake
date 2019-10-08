import os
import os.path
import time

print('Please place your files you wish to rename in the input folder.')
dir = os.listdir('input')
dir.sort()

try:
  # just a test to see if any files exist
  len(dir[0])
except IndexError:
  print("No files found!")

elements = len(dir)

def rename():

  prefix = input('Please add the prefix for your file names: ')
  prefixOld = prefix + ' - '
  num = 1
  extNum = 0
  for i in range(elements):
    print(dir)
    prefix = prefixOld + str(num)
    extension = os.path.splitext(dir[extNum])[1]
    finalName = prefix + extension
    os.rename('input/' + dir[extNum], 'input/' + finalName)
    print(os.listdir('input/'))
    del prefix
    num = num + 1
    extNum = extNum + 1

print(dir)
print('')
userCheck = input('Are these the files you wish to rename (Y/N): ')
if userCheck == 'Y' or userCheck == 'y':
  rename()
else:
  print('')
  print('Program has quit. Please move the files')
  print('you wish to rename into the input folder.')
