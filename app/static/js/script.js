document.addEventListener("DOMContentLoaded", function () {
    const textElement = document.getElementById("text");
    const inputElement = document.getElementById("input");

    // Desabilitar Ctrl + C e Ctrl + V
    inputElement.addEventListener("keydown", function (event) {
        if (event.ctrlKey && (event.key === "c" || event.key === "v")) {
            event.preventDefault();
            console.log("Ctrl+C e Ctrl+V estão desabilitados!");
        }
    });

    const resultElement = document.getElementById("result");
    const finalScoreElement = document.getElementById("final-score");
    const totalScoreElement = document.getElementById("total-score");
    const currentScoreElement = document.getElementById("current-score");
    const nextTextBtn = document.getElementById("next-text-btn");
    const submitScoreBtn = document.getElementById("submit-score-btn");

    // Variáveis de controle
    let currentIndex = 0;
    let startTime = null;
    let timerInterval = null;
    let totalScore = 0;
    let currentScore = 0;
    let errorOccurred = false;

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
                updateDisplayedText('');  // Limpa o texto exibido
            })
            .catch(error => console.error("Erro ao carregar o texto:", error));
    }

    // Função para capturar e processar a entrada do usuário
    inputElement.addEventListener("input", function () {
        const inputText = inputElement.value;
        const originalText = textElement.innerText;

        // Verifica se o texto digitado está correto até o ponto atual
        let isCorrect = checkCorrectness(inputText, originalText);

        if (!isCorrect) {
            inputElement.classList.add("shake");  // Aplica efeito de erro
            errorOccurred = true;
        } else {
            inputElement.classList.remove("shake");
            errorOccurred = false;
            updateDisplayedText(inputText);  // Atualiza o texto exibido
        }

        // Se o texto for digitado corretamente
        if (inputText === originalText && !errorOccurred) {
            clearInterval(timerInterval);  // Para o timer
            calculateScore(inputText, originalText);  // Calcula a pontuação
            submitScoreBtn.style.display = 'inline-block';  // Mostra o botão de enviar pontuação
        }
    });

    // Função para verificar se o texto digitado está correto até o ponto atual
    function checkCorrectness(inputText, originalText) {
        for (let i = 0; i < inputText.length; i++) {
            // Verifica caractere por caractere, inclusive acentos
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
    }

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
