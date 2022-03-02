function addMessage(author, message) {
  const place = document.querySelector('.messages-wrapper');
  const fragment = document.getElementById('submit-template').content.cloneNode(true);

  fragment.querySelector('.message-author').innerText = author;
  fragment.querySelector('.message-body').innerText = message;

  if (author !== 'Вы') {
    fragment.querySelector('.message-wrapper').classList.remove('justify-content-end');
  }

  place.append(fragment);
}

function updateLastMessage(user) {
  if (user.history.length <= 0) return;

  let message = user.history[user.history.length - 1].message;

  if (message.length > 30) {
    message = message.substr(0, 30) + '...';
  }

  user.htmlFragment.querySelector('.last-message').innerText = message;
}

function refreshChat(history) {
  let chat = document.querySelector('.messages-wrapper');

  chat.innerHTML = '';
  history.forEach(item => addMessage(item.author, item.message));
}

export { addMessage, updateLastMessage, refreshChat };
