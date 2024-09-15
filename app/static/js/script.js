document.addEventListener("DOMContentLoaded", function () {
    const textElement = document.getElementById("text");
    const inputElement = document.getElementById("input");
    const modalElement = document.getElementById("scoreModal"); // Modal de pontuação
    const modalCurrentScoreElement = document.getElementById("modal-current-score");

    const resultElement = document.getElementById("result");

    const totalScoreElement = document.getElementById("total-score");
    const currentScoreElement = document.getElementById("current-score");

    let currentIndex = 0;
    let currentTextId = null;  // Armazena o ID do texto atual
    let startTime = null;
    let totalScore = 0;
    let currentScore = 0;
    let errorOccurred = false;
    let isBlocked = false;  // Flag para bloquear o teclado após erro
    let isComposing = false;  // Verifica se o usuário está digitando um caractere acentuado
    let timerInterval;  // Declaração da variável timerInterval

    // Função para carregar o último texto salvo ou iniciar o próximo texto
    fetchLastTextId();

    // Função para obter o último texto salvo do backend
    function fetchLastTextId() {
        fetch('/get_last_text_id')
            .then(response => response.json())
            .then(data => {
                if (data.last_text_id !== undefined) {
                    currentIndex = data.last_text_id + 1;  // Continua a partir do próximo texto
                    fetchNextText(currentIndex);  // Carrega o próximo texto
                } else {
                    fetchNextText(currentIndex);  // Caso contrário, inicia do primeiro texto
                }
            })
            .catch(error => console.error("Erro ao carregar o último texto salvo:", error));
    }

    // Função para carregar o próximo texto
    function fetchNextText(index) {
        fetch(`/get_text?index=${index}`)
            .then(response => response.json())
            .then(data => {
                if (data && data.text) {
                    textElement.innerText = data.text;  // Define o texto corretamente no HTML
                    currentTextId = data.id;  // Salva o ID do texto carregado
                    inputElement.value = '';  // Limpa o campo de entrada
                    modalElement.classList.remove('show');  // Esconde o modal
                    startTime = null;
                    errorOccurred = false;  // Reinicia o estado de erro
                    isBlocked = false;  // Desbloqueia o teclado
                    updateDisplayedText('');  // Limpa o texto exibido
                } else {
                    console.error("Erro: O texto não foi encontrado.");
                }
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
            textElement.classList.add("shake");  // Aplica o efeito de shake no texto de referência
            errorOccurred = true;
            isBlocked = true;  // Bloqueia o teclado para outros caracteres

            // Remover a animação de shake após um tempo
            setTimeout(() => {
                textElement.classList.remove("shake");
            }, 500);  // A animação de shake será removida após 500ms
        } else {
            textElement.classList.remove("shake");
            errorOccurred = false;
            isBlocked = false;  // Desbloqueia o teclado quando o erro é corrigido
            updateDisplayedText(inputText);  // Atualiza o texto exibido
        }

        // Se o texto for digitado corretamente e completamente
        if (inputText === originalText && !errorOccurred) {
            clearInterval(timerInterval);  // Para o timer
            calculateScore(inputText, originalText);  // Calcula a pontuação
            saveScoreAndText();  // Salva a pontuação e o texto no banco de dados
        }

        // Exibe o box de tempo quando o usuário começa a digitar
        if (!resultElement.classList.contains("visible")) {
            resultElement.classList.add("visible");
        }
    });

    // Função para salvar a pontuação e o texto no banco de dados
    function saveScoreAndText() {
        const data = {
            score: currentScore,
            text_id: currentTextId  // Envia o ID do texto atual
        };

        fetch('/save_score', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.message);
            showScoreModal();  // Exibe o modal de pontuação
        })
        .catch(error => console.error("Erro ao salvar a pontuação:", error));
    }

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
        modalCurrentScoreElement.innerText = currentScore;  // Exibe a pontuação no modal
    }

    // Função para exibir o modal de pontuação
    function showScoreModal() {
        modalElement.classList.add('show');  // Exibe o modal

        // Fecha o modal automaticamente e carrega o próximo texto
        setTimeout(function () {
            modalElement.classList.remove('show');  // Esconde o modal
            fetchNextText(++currentIndex);  // Carrega o próximo texto
        }, 3000);  // Exibe o modal por 3 segundos
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
