# ZCasino.Kamel
ZCasino project of Openclassroom
rules of game

 we will try to make a small program that we will call ZCasino. It will be a small game of roulette very simplified in which you can bet a certain amount and win or lose money (such is the fortune, the casino!). When you run out of money, you have lost.
Our rules of the game

Well, the roulette is very nice as a game, but a little too complicated for a first TP. So, we will simplify the rules and I present you right away what we get:

    The player bet on a number between 0 and 49 (50 numbers in all). By choosing his number, he deposits the amount he wants to bet.

    The roulette consists of 50 boxes naturally ranging from 0 to 49. The even numbers are black, the odd numbers are red. The dealer throws the roulette, drops the ball and when the roulette stops, raises the number of the box in which the ball has stopped. In our program, we will not repeat all these details "material" but these explanations are also for those who have had the chance to avoid the casino rooms so far. The number on which the ball stopped is, of course, the winning number.

    If the winning number is the one on which the player has bet (probability of 1/50, rather weak), the dealer gives him 3 times the amount wagered.

    Otherwise, the dealer looks to see if the number bet by the player is the same color as the winning number (if they are both odd or even odd). If so, the dealer gives him 50% of the bet. If this is not the case, the player loses his bet.
2743/5000
In the two winning scenarios seen above (the number wagered and the winning number are identical or have the same color), the dealer gives the player the amount initially wagered before adding his winnings. This means that in both scenarios the player gets money. Only in the third case does he lose the sum bet. We will use for dollar currency $ instead of the euro for encoding reasons under the Windows console.
Organize our project

For this project, we will not write a module. We will use those of Python, which are quite sufficient for the moment, especially that to generate the random, which I will present below. In the meantime, do not deprive yourself to create a directory and put the file ZCasino.py, everything will be played here.

You are able to write the ZCasino program as explained in the first part without difficulty ... except to generate random numbers. Python has dedicated a whole module to the generation of pseudo-random elements, the random module.
The random module

In this module, we will focus on the randrange function which can be used in two ways:

    specifying only one parameter (randrange (6) returns a random number between 0 and 5);

    specifying two parameters (randrange (1, 7): returns a random number between 1 and 6, which is useful, for example, to reproduce an experiment with a six-sided die).

To draw a random number between 0 and 49 and thus simulate the experience of the roulette game, we will use the randrange (50) instruction.

There are other ways to use randrange but we will not need it here and I would say that for this program, only the first use will be useful.

Do not hesitate to do tests in the shell (you have not forgotten where it is, huh?) And try several syntaxes of the randrange function. I remind you that it is in the random module, do not forget to import it.
Round a number

You may have noticed it, in the explanation of the rules I specified that if the player bet on the good color, he got 50% of his bet. Yes, but ... it's still better to work with integers. If the player bets $ 3, for example, he is paid $ 1.5. It is still acceptable, but if it continues, we may arrive at floating numbers with many digits after the decimal point. So as many round to the higher number. Thus, if the player bets $ 3, he is returned $ 2. For that, we will use a function of the math module named ceil. I let you watch what she does, there is nothing complicated.
