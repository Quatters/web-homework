export default function sayHello(parent) {
  const node = document.createElement('p');
  node.innerText = 'Hello from first script';
  parent.append(node);
}
