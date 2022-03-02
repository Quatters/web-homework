const fs = require('fs');

const alphabet = '1234567890';

let text = '';

for (let i = 0; i < 1000; i++) {
  text = text + randomWord(1) + '\n';
}

fs.writeFileSync('file1', text);

function randomWord(length = 10) {
  if (Math.random() < 0.1) {
    return specialWord();
  }

  let word = '';
  for (let i = 0; i < length; i++) {
    word = word + randomLetter();
  }
  return 'обычная строка ' + word;
}

function specialWord() {
  const pattern = 'ко';
  let word = '';
  let count = Math.floor(Math.random() * 19 + 1);
  for (let i = 0; i < count; i++) {
    word += pattern;
    if (Math.random() < 0.5) {
      word += ' ';
    }
  }
  return word;
}

function randomLetter() {
  const index = Math.floor(Math.random() * alphabet.length);
  return alphabet[index];
}
