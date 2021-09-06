# Tic-Tac-Toe
Implementation of the popular game, with both single and 2 player modes
Single Player mode uses Alpha-beta pruning for the computer, creating a unbeatable opponent.

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/naruarjun/SADAM-reproducibility.git
   ```
2. Install virtualenv
   ```sh
   python3 -m pip install --user virtualenv
   ```
3. Make a virtual Environnment and activate it
   ```sh
   virtualenv /path_to_env
   source /path_to_env/bin/activate
   ```
4. Make sure, **tkinter** is installed on the system
    ```sh
    # Installation command will vary based on OS
    apt-get install python3-tk
    ```
5. Install the requirements
   ```sh
   pip install -r requirements.txt 
   ```


## Usage

There are 2 modes, in which the game can be played, and the same can be selected via the buttons given on the top-left corner of the tkinter window that opens up. There are 2 ways in which the computer can play, namely by using Alpha-Beta pruning, or by using Minimax algorithm. The method has to be chosen at the time of launching the application as shown below. 

1. Minimax mode
    ```sh
    python ttt_new.py --method minimax
    ```
2. Alpha Beta Pruning method
    ```sh
    python ttt_new.py --method abprune
    ```

## Screenshots from the application

Below are the links to our corresponsing projects on Weights and Biases

#### Launch Window
[Launch Window](Images/BeforeStart.png)

#### During the Game
[During the game](Images/DuringGame.png)
