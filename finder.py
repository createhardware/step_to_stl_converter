# example 1
#  из минусов - ему нужен путь к папке, но это может не быть проблемой
# 
import os
import glob

work_dir = os.getcwd()
# print(glob.glob("D:\hard_soft_projects\STEP_to_STL_scrypts\*"))
print(glob.glob(work_dir + "\\*" ))


# TODO: import pysimplegui
# find pattern - "1200"
# output directory
# add stl convrter?




# import os
 
for root, dirs, files in os.walk(work_dir):
    for file in files:
        if file.endswith('.STEP'):
            # print(os.path.join(root, file))
            if glob.fnmatch.fnmatch(file, "*1200*.STEP"):
                print(file)
                print(os.path.join(root, file))
                
                
