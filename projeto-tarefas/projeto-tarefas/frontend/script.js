
const listaTarefas = document.getElementById('lista-tarefas');
const input = document.getElementById('nova-tarefa');
const botaoAdicionar = document.getElementById('adicionar');

botaoAdicionar.addEventListener('click', () => {
    if (input.value.trim() !== '') {
        const li = document.createElement('li');
        li.textContent = input.value;
        const botaoRemover = document.createElement('button');
        botaoRemover.textContent = 'Remover';
        botaoRemover.addEventListener('click', () => li.remove());
        li.appendChild(botaoRemover);
        listaTarefas.appendChild(li);
        input.value = '';
    }
});
