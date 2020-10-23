from pathlib import Path
import mimetypes
# import re
import os
# from os import getcwd
# # def homepage():
# #     for (dirpath, dirnames, filenames) in os.walk('.\\webroot'):
# #         for x in filenames:
# #             return "".join((str(dirpath+'\\'+x)))


# # print(homepage())

# # home = [x for x in os.listdir('.\\webroot')]
# # print('\n'.join(home))

# print('\n'.join([x for x in os.listdir('.\\webroot')]))

# for (dirpath, dirnames, filenames) in os.walk('.\\webroot'):
#     for x in filenames:
#         print([dirpath+'\\'+x])

#     # for (dirpath, dirnames, filenames) in os.walk('.\\webroot'):
#     #     for x in filenames:
#     #         return "".join(dirpath+'\\'+x)


# os.open('C:\\Users\\v-ollock\\github\\PYTHON230\\socket-http-server\\webroot\\a_web_page.html', os.O_RDONLY )


# PATH = "C:\\Users\\v-ollock\\github\\PYTHON230\\socket-http-server\\webroot\\"

# list_of_files = {}
# content = ''
# for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
#     for filename in filenames:
#         if filename.endswith('.html'): 
#             list_of_files[filename] = os.sep.join([dirpath, filename])
#             file = open(os.path.join(dirpath, filename), 'r') 
#             # print(file.read())
#             content = file.read()
#             file.close()

# print(content)

# for x in os.listdir('.\\webroot'):
#     print(x)
#     print(os.path.isfile(x))


# bb = [
# ]
# print(bb[-2:-1])
# print(bb[-1:])

print(Path.cwd().joinpath('webroot'))


current_dir = os.path.dirname(os.path.realpath(__file__))
print(os.path.realpath(__file__))
print(current_dir)


current_dir = os.path.dirname(os.path.realpath(__file__))
query = os.path.join(current_dir, "webroot", 'a_web_page.html')
print(mimetypes.guess_type(query)[0])
print(mimetypes.guess_type(query))