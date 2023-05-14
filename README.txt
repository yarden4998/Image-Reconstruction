In this assignment I received a jpg file containing a scrambled image and a SQLite database.

My mission was to descarmble that image. 

The scrambled image was divided into square tiles (37x37 pixels). Randomly, each tile was rotated 90 degrees left or right. The SQLite database contains for every tile its original position, new position and direction of rotation (left/right).

At first, I checked how the data was represented and what is the database header. Notice that the table containing the data named 'transform'.

The process to descramble the image contains 2 sub-processes. 

The first was to extract each tile from the scrambled image into a list. It's done by cropping the image into small 37x37 pixels images. 

The second was to iterate over each row and each column in the SQLite dataset, extracting the tile from its place in the list (which is built according to its place in the scrambled image given by the dataset), applying the correct rotation according to the dataset and placing the tile at the desired place in the descrambled image file as given in the dataset.

Language used: 
Python

Libraries used:
Sqlite3
Pillow (PIL)

Instructions:
To run the program, make sure you have the above-mentioned libraries installed. The input for the program is a jpg file containing a scrambled image and a SQLite database which needed to be exist in the same folder as the program, named "assignment.jpg" and "assignment.sqlite" accordingly. The output is a descrambled image. Once you have all the files, run the Python program to get the descrambled image.