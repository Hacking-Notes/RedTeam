--- ---

<h2>The Memory of a Program</h2>

Whenever we execute a program, all data will be processed somehow through the computer's RAM (Random Access Memory). If you think of a videogame, your HP, position, movement speed and direction are all stored somewhere in memory and updated as needed as the game goes. 

![Game memory layout](https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/e73c41674384b537096f1e800b3edd95.png)  

If you can modify the relevant memory positions, you could trick the game into thinking you have more HP than you should or even a higher score! This sounds relatively easy, but a program's memory space is vast and sparse, and finding the location where these variables are stored is nothing you'd want to do by hand. Hopefully, some tools will help us navigate memory and find where all the juicy information is at.