# Python-Projects 

---

<h2> Project - 1: Rock Paper Scissors 🎮 </h2>

<h3> 📌 Description </h3>  
<p style="font-size:16px">  
This is a classic Rock–Paper–Scissors game where the player competes against the computer.  
The computer makes a random choice, and the winner is decided based on standard rules:  

<h4> Game Rules: </h4>
<ul>
<li>Rock beats Scissors</li>  
<li>Scissors beats Paper</li>  
<li>Paper beats Rock</li>  
</ul>
</p>  

---

<h3> ⚙️ APPROACH </h3>  
<p style="font-size:16px">  

1. Create a list of options: <code>["rock", "paper", "scissors"]</code>.  
2. Ask the player to choose their move by entering a number:  
   - <b>'0'</b> for Rock  
   - <b>'1'</b> for Paper  
   - <b>'2'</b> for Scissors  
3. Generate a random number between 0 and 2 for the computer’s choice.  
4. Display both the player’s choice and the computer’s choice.  
5. Compare choices using the rules of Rock–Paper–Scissors:  
   - If both choices are the same → it’s a <b>draw</b>.  
   - Rock beats Scissors → Rock wins.  
   - Scissors beats Paper → Scissors wins.  
   - Paper beats Rock → Paper wins.  
6. Print the result (<b>Win, Lose, or Draw</b>).  

</p>  

---

<h3> 🎮 Example Gameplay </h3>  <img width="580" height="218" alt="Screenshot 2025-08-16 225236" src="https://github.com/user-attachments/assets/cd476db4-9a00-43f2-ac80-3a00624ef815" />

<img width="578" height="234" alt="Screenshot 2025-08-16 225344" src="https://github.com/user-attachments/assets/cb1069e7-7edf-4665-b187-6dbf67e9d8b2" />
<img width="580" height="235" alt="Screenshot 2025-08-16 225329" src="https://github.com/user-attachments/assets/02e4f808-20ea-484e-b78a-caa56de11f1d" />
<img width="583" height="237" alt="Screenshot 2025-08-16 225308" src="https://github.com/user-attachments/assets/424049ab-b2d5-40dc-a863-2cc892ffa147" />


---

<h2> Project - 2: PyPassword Generator 🔑 </h2>

<h3> 📌 Description </h3>  
<p style="font-size:16px">  
This is a Python-based Password Generator that creates strong and secure random passwords.  
The user specifies how many letters, numbers, and symbols should be included, and the program generates a shuffled password containing all selected elements.  
</p>  

---

<h3> ⚙️ APPROACH </h3>  
<p style="font-size:16px">  

1. Create three lists containing:  
   - <b>letters</b> (both uppercase and lowercase alphabets)  
   - <b>numbers</b> (0–9)  
   - <b>symbols</b> (!, #, $, %, &, (, ), *, +)  
2. Ask the user how many letters, symbols, and numbers they want in the password.  
3. Use <code>random.choice()</code> to randomly select elements from each list based on user input.  
4. Store all selected characters in a list.  
5. Shuffle the list using <code>random.shuffle()</code> to make the password unpredictable.  
6. Join the shuffled list into a single string.  
7. Display the final password to the user.  

</p>  

---

<h3> 🎮 Example Gameplay </h3>  
<img width="512" height="333" alt="Screenshot 2025-08-16 232525" src="https://github.com/user-attachments/assets/92d514d4-d35c-4c83-bd3f-2b116c996a33" />

---

<h2>🎮 Project 3 - Hangman Game </h2>

<h3>📌 Statement </h3>
  <p>
    This is a classic <strong>Hangman Game</strong> built using <strong>Python</strong>. 
    The game selects a random word from a word list and the player has to guess it letter by letter 
    before running out of lives. The game also displays hangman ASCII art for each incorrect guess.
  </p>

  <h3>🚀 Features</h3>
  <ul>
    <li>Random word selection from a word list.</li>
    <li>Displays underscores for letters to be guessed.</li>
    <li>Tracks correct guesses and updates the word display.</li>
    <li>Reduces lives for each wrong guess.</li>
    <li>ASCII Art representation of hangman stages.</li>
    <li>Win/lose conditions with clear messages.</li>
  </ul>

  <h3>📂 Project Structure</h3>
  <pre>
  ├── Hangman_wordsList.py   # Contains the list of words
  ├── Hangman_AsciiArt.py    # Contains ASCII art for hangman stages
  ├── Hangman_game.py             # Main game file
  </pre>

  <h3>⚙️ Requirements</h3>
  <ul>
    <li>Python </li>
    <li>No external libraries required</li>
  </ul>

  <h3>▶️ How to Run</h3>
  <ol>
    <li>Clone the repository:</li>
    <pre>git clone &lt;https://github.com/gajjelamanikantagoud/Python-Projects-/blob/main/Project-3%20Hangman_Game.zip&gt;</pre>
    <li>Navigate to the project folder:</li>
    <pre>cd project-3 Hangman_game</pre>
    <li>Run the game:</li>
    <pre>python Hangman_game.py</pre>
  </ol>

  <h3>📸 Example Gameplay</h3><img width="928" height="840" alt="Screenshot 2025-08-17 003339" src="https://github.com/user-attachments/assets/54b7ac8d-bd3d-4219-8916-bd20a1a74352" />
<img width="894" height="834" alt="Screenshot 2025-08-17 003406" src="https://github.com/user-attachments/assets/32a5300b-9837-43c8-8d87-def5c91d0003" />
<img width="910" height="789" alt="Screenshot 2025-08-17 003431" src="https://github.com/user-attachments/assets/f3ed9501-3647-47c1-8427-752c4b13586b" />

---

 <h2>🔐 Project 4 - Caesar Cipher </h2>

  <p>
    This project is a simple implementation of the <strong>Caesar Cipher</strong> encryption technique in <strong>Python</strong>.  
    The program allows the user to <b>encode</b> (encrypt) or <b>decode</b> (decrypt) messages by shifting each letter of the text 
    forward or backward in the alphabet by a user-defined amount.  
    It also gracefully handles large shift values and preserves non-alphabetic characters such as spaces and symbols.
  </p>

  <h3>🚀 Features</h3>
  <ul>
    <li>Encrypt messages by shifting letters forward in the alphabet.</li>
    <li>Decrypt messages by shifting letters backward.</li>
    <li>Handles shifts larger than the alphabet size using modular arithmetic.</li>
    <li>Keeps spaces, numbers, and symbols unchanged.</li>
    <li>Interactive: lets the user continue encoding/decoding multiple times.</li>
    <li>Includes ASCII art logo (imported from <code>art.py</code>).</li>
  </ul>

  <h3>📂 Project Structure</h3>
  <pre>
  ├── art.py          # Contains ASCII art logo
  ├── caesar.py       # Main Caesar Cipher game logic
  </pre>

  <h3>⚙️ Requirements</h3>
  <ul>
    <li>Python 3.x</li>
    <li>No external libraries required</li>
  </ul>

  <h3>▶️ How to Run</h3>
  <ol>
    <li>Clone the repository:</li>
    <pre>git clone &lt;your-repo-link&gt;</pre>
    <li>Navigate to the project folder:</li>
    <pre>cd project-4-caesar-cipher</pre>
    <li>Run the program:</li>
    <pre>python caesarcipher.py</pre>
  </ol>

  <h3>📸 Example Gameplay</h3>
  
<img width="765" height="760" alt="Screenshot 2025-08-17 012619" src="https://github.com/user-attachments/assets/673a075a-66f2-464c-b4ab-97120c34aa89" />
<img width="620" height="321" alt="Screenshot 2025-08-17 012636" src="https://github.com/user-attachments/assets/5940a8bd-8866-4365-80e0-3f73faa09e36" />


