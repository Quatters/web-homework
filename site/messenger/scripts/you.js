import { addMessage, updateLastMessage } from './chat-handler.js';

const htmlFragment = document.querySelectorAll('.user-wrapper').item(1);

let history = [];

function send(author, message) {
	history.push({ author, message });
	addMessage(author, message);

	window.localStorage.setItem('youHistory', JSON.stringify(history));

	updateLastMessage({ htmlFragment, history });
}

function loadHistory(_history) {
	history = _history;
	updateLastMessage({ htmlFragment, history });
}

export { send, loadHistory, history, htmlFragment };
