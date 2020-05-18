1. Don't change the file name anywhere just like 
    -> ws (directory name)
    -> mlwork 
    -> hello2.py (contains the code of mnist dataset)
2. Copy the directory into your root directory of your linux and building your docker file by using the command
    -> cd ws/
    -> docker build -t ml:1 . (you should be present at the same directory)
    -> docker run ml:1