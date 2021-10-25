import { addMessage, updateLastMessage } from './chat-handler.js';

const showName = 'Бот вопрос/ответ';

const noAnswers = ['Нет.', 'nope', 'Не-а)', 'Ответ отрицательный.'];
const yesAnswers = ['Да.', 'Ага', 'Точно!', 'Верно.'];

const htmlFragment = document.querySelectorAll('.user-wrapper').item(0);

let history = [
  {
    author: 'Бот вопрос/ответ',
    message: 'Привет! Здесь вы можете задать вопрос, на который я отвечу "Да" или "Нет".',
  },
];

function getAnswer(question) {
  if (!question.endsWith('?')) {
    return 'Вопрос обычно заканчивается знаком "?" :)';
  }

  if (Math.random() > 0.5) {
    return yesAnswers[Math.floor(Math.random() * yesAnswers.length)];
  } else {
    return noAnswers[Math.floor(Math.random() * noAnswers.length)];
  }
}

function send(author, message) {
  history.push({ author, message });
  addMessage(author, message);

  const answer = getAnswer(message);
  history.push({
    author: showName,
    message: answer,
  });
  addMessage(showName, answer);

  updateLastMessage({ htmlFragment, history });

  window.localStorage.setItem('botHistory', JSON.stringify(history));
}

function loadHistory(_history) {
  history = _history;
  updateLastMessage({ htmlFragment, history });
}

export { send, loadHistory, history, htmlFragment };
