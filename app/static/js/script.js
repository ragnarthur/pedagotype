document.addEventListener("DOMContentLoaded", function () {
    const textElement = document.getElementById("text");
    const inputElement = document.getElementById("input");
    const modalCurrentScoreElement = document.getElementById("modal-current-score");

    const resultElement = document.getElementById("result");
    const finalScoreElement = document.getElementById("final-score");
    const totalScoreElement = document.getElementById("total-score");
    const currentScoreElement = document.getElementById("current-score");
    const nextTextBtn = document.getElementById("next-text-btn");

    let currentIndex = 0;
    let startTime = null;
    let timerInterval = null;
    let totalScore = 0;
    let currentScore = 0;
    let errorOccurred = false;
    let isBlocked = false;  // Flag para bloquear o teclado após erro

    // Variáveis para acentos
    let isComposing = false;  // Verifica se o usuário está digitando um caractere acentuado

    // Carrega o primeiro texto
    fetchNextText(currentIndex);

    // Função para carregar o próximo texto
    function fetchNextText(index) {
        fetch(`/get_text?index=${index}`)
            .then(response => response.json())
            .then(data => {
                textElement.innerText = data.text;  // Define o texto no HTML
                inputElement.value = '';  // Limpa o campo de entrada
                resultElement.innerText = '';
                startTime = null;
                errorOccurred = false;  // Reinicia o estado de erro
                isBlocked = false;  // Desbloqueia o teclado
                updateDisplayedText('');  // Limpa o texto exibido
            })
            .catch(error => console.error("Erro ao carregar o texto:", error));
    }

    // Função para capturar e processar a entrada do usuário
    inputElement.addEventListener("input", function (event) {
        const inputText = inputElement.value;
        const originalText = textElement.innerText;

        // Bloqueia o teclado se houver erro e o caractere não for backspace, exceto durante a composição de acentos
        if (isBlocked && !isComposing && event.inputType !== 'deleteContentBackward') {
            inputElement.value = inputText.slice(0, -1);  // Remove o caractere incorreto
            return;
        }

        // Verifica se o texto digitado está correto até o ponto atual
        let isCorrect = checkCorrectness(inputText, originalText);

        if (!isCorrect) {
            inputElement.classList.add("shake");  // Aplica efeito de erro
            errorOccurred = true;
            isBlocked = true;  // Bloqueia o teclado para outros caracteres
        } else {
            inputElement.classList.remove("shake");
            errorOccurred = false;
            isBlocked = false;  // Desbloqueia o teclado quando o erro é corrigido
            updateDisplayedText(inputText);  // Atualiza o texto exibido
        }

        // Se o texto for digitado corretamente
        if (inputText === originalText && !errorOccurred) {
            clearInterval(timerInterval);  // Para o timer
            calculateScore(inputText, originalText);  // Calcula a pontuação
            showCongratsModal();  // Exibe o modal de parabéns
        }
    });

    // Função para detectar se o usuário está digitando um caractere composto (acentuado)
    inputElement.addEventListener('compositionstart', function () {
        isComposing = true;
    });

    inputElement.addEventListener('compositionend', function () {
        isComposing = false;  // O caractere composto foi finalizado
    });

    // Função para verificar se o texto digitado está correto até o ponto atual
    function checkCorrectness(inputText, originalText) {
        for (let i = 0; i < inputText.length; i++) {
            if (inputText[i] !== originalText[i]) {
                return false;
            }
        }
        return true;
    }

    // Função para atualizar o texto exibido, aplicando cores para os caracteres corretos
    function updateDisplayedText(inputText) {
        const originalText = textElement.innerText;
        let formattedText = '';

        for (let i = 0; i < originalText.length; i++) {
            if (i < inputText.length) {
                formattedText += `<span class="correct">${originalText[i]}</span>`;
            } else if (i === inputText.length) {
                formattedText += `<span class="current">${originalText[i]}</span>`;
            } else {
                formattedText += originalText[i];
            }
        }

        textElement.innerHTML = formattedText;
    }

    // Função para calcular a pontuação
    function calculateScore(inputText, originalText) {
        const currentTime = new Date();
        const elapsedTime = Math.floor((currentTime - startTime) / 1000);
        const baseScore = Math.max(0, Math.floor((originalText.length * 100) / elapsedTime));
        currentScore = baseScore;
        totalScore += currentScore;

        currentScoreElement.innerText = currentScore;
        totalScoreElement.innerText = totalScore;
        modalCurrentScoreElement.innerText = currentScore;  // Atualiza pontuação no modal
    }

    // Função para exibir o modal de parabéns
    function showCongratsModal() {
        $('#congratsModal').modal('show');  // Exibe o modal
    }

    // Evento para o botão no modal para carregar o próximo texto
    nextTextBtn.addEventListener('click', function () {
        $('#congratsModal').modal('hide');  // Fecha o modal
        fetchNextText(++currentIndex);  // Carrega o próximo texto
    });

    // Inicia o timer quando o usuário começa a digitar
    inputElement.addEventListener("input", function () {
        if (!startTime) {
            startTime = new Date();  // Inicia o cronômetro
            timerInterval = setInterval(updateTimer, 1000);  // Atualiza o cronômetro a cada segundo
        }
    });

    // Função para atualizar o cronômetro
    function updateTimer() {
        const currentTime = new Date();
        const timeElapsed = Math.floor((currentTime - startTime) / 1000);
        resultElement.innerText = `Tempo: ${timeElapsed} segundos`;
    }
});
