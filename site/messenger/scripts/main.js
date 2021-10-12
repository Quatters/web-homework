import * as bot from './answer-bot.js';
import { refreshChat } from './chat-handler.js';
import * as you from './you.js';

const textarea = document.querySelector('.autoresizable');
const sendButton = document.querySelector('#send-btn');
let currentUser;

window.onload = function () {
	textarea.setAttribute('style', 'height:' + 38 + 'px;overflow-y:hidden;');
	textarea.addEventListener('input', onInput);

	sendButton.addEventListener('click', onSendButtonClick);

	bot.htmlFragment.addEventListener('click', selectBot);
	you.htmlFragment.addEventListener('click', selectYou);

	let botHistoryJson = window.localStorage.getItem('botHistory');
	if (botHistoryJson !== null) bot.loadHistory(JSON.parse(botHistoryJson, bot.history));

	let youHistoryJson = window.localStorage.getItem('youHistory');
	if (youHistoryJson !== null) you.loadHistory(JSON.parse(youHistoryJson, you.history));

	if (window.localStorage.getItem('currentUser') === 'you') selectYou();
	else selectBot();
};

function onInput(event) {
	if (event.inputType === 'insertLineBreak') {
		submit(event.currentTarget.value.trim());
		return;
	}

	this.style.height = 38 + 'px';
	this.style.height = this.scrollHeight + 'px';
}

function submit(value) {
	if (value.length <= 0) return;

	textarea.value = '';
	currentUser.send('Вы', value);

	const chat = document.querySelector('.messages-wrapper');
	chat.scrollTop = chat.scrollHeight;
}

function selectBot() {
	if (currentUser === bot) return;

	refreshChat(bot.history);
	currentUser = bot;

	bot.htmlFragment.classList.add('active');
	you.htmlFragment.classList.remove('active');

	window.localStorage.setItem('currentUser', 'bot');
}

function selectYou() {
	if (currentUser === you) return;

	refreshChat(you.history);
	currentUser = you;

	you.htmlFragment.classList.add('active');
	bot.htmlFragment.classList.remove('active');

	window.localStorage.setItem('currentUser', 'you');
}

function onSendButtonClick() {
	submit(textarea.value.trim());
}
