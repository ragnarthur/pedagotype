# Lista de textos base com IDs organizados por ordem de dificuldade (do menor para o maior)
TEXTS = sorted([
    {"id": 1, "text": "Educação é essencial."},
    {"id": 2, "text": "A aprendizagem é um processo contínuo e vital no desenvolvimento humano."},
    {"id": 3, "text": "Didática é a ciência que estuda os métodos e técnicas que facilitam o ensino e a aprendizagem."},
    {"id": 4, "text": "A filosofia da educação busca entender os princípios éticos e morais que fundamentam as práticas pedagógicas e suas implicações na formação do indivíduo."},
    {"id": 5, "text": "A sociologia da educação analisa como as estruturas sociais, como classe, gênero e etnia, influenciam o acesso e a qualidade da educação, bem como o papel da educação na manutenção ou transformação dessas estruturas."},
    {"id": 6, "text": "Ao longo dos séculos, a educação passou por diversas transformações, refletindo mudanças sociais, políticas e culturais. Desde a educação informal nas sociedades primitivas até os sistemas escolares modernos, cada período histórico contribuiu de forma única para a evolução das práticas educacionais."},
    {"id": 7, "text": "A metodologia de ensino envolve a escolha e aplicação de estratégias pedagógicas que sejam adequadas ao conteúdo a ser ensinado, ao perfil dos alunos e aos objetivos educacionais. O uso de metodologias ativas, como a aprendizagem baseada em projetos, tem ganhado destaque na promoção de um ensino mais participativo e centrado no aluno."},
    {"id": 8, "text": "A avaliação educacional não se restringe à simples medição do desempenho dos alunos, mas se estende à análise do processo de ensino-aprendizagem como um todo. Ela deve ser vista como uma ferramenta diagnóstica que, ao identificar dificuldades e potencialidades, possibilita o ajuste de estratégias pedagógicas e contribui para o desenvolvimento integral do aluno."},
    {"id": 9, "text": "A educação inclusiva é um paradigma educacional que promove a equidade, assegurando que todos os alunos, independentemente de suas diferenças físicas, cognitivas, culturais ou socioeconômicas, tenham acesso a um ambiente de aprendizagem adaptado às suas necessidades."},
    {"id": 10, "text": "As tecnologias digitais têm se tornado ferramentas imprescindíveis na educação contemporânea, oferecendo novas possibilidades para o ensino e a aprendizagem."},
    {"id": 11, "text": "O papel do professor na sala de aula vai além de transmitir conhecimento. Ele atua como facilitador do processo de aprendizagem, criando um ambiente propício para o desenvolvimento das habilidades e competências dos alunos."},
    {"id": 12, "text": "A educação ambiental é fundamental para a formação de cidadãos conscientes e responsáveis. Por meio dela, é possível promover a preservação dos recursos naturais e a sustentabilidade, essenciais para o futuro do planeta."},
    {"id": 13, "text": "A integração das artes na educação básica contribui para o desenvolvimento integral dos alunos, estimulando a criatividade, a sensibilidade e a expressão emocional."},
    {"id": 14, "text": "A inclusão digital é um desafio importante na educação atual. Com o avanço das tecnologias, é essencial garantir que todos os alunos tenham acesso às ferramentas digitais e saibam utilizá-las de forma crítica e consciente."},
    {"id": 15, "text": "A construção do conhecimento é um processo colaborativo, que envolve a interação entre professores, alunos e a comunidade."},
    {"id": 16, "text": "A interdisciplinaridade na educação permite a integração de diferentes áreas do conhecimento, promovendo uma visão mais completa e contextualizada dos conteúdos abordados."},
    {"id": 17, "text": "O ensino por competência foca no desenvolvimento de habilidades que preparam os alunos para os desafios do mundo contemporâneo."},
    {"id": 18, "text": "A pedagogia crítica propõe uma educação que vai além da simples transmissão de conhecimentos, incentivando os alunos a questionarem a realidade."},
    {"id": 19, "text": "O papel do educador é mediar o processo de construção do conhecimento, incentivando a autonomia e a criatividade dos alunos."},
    {"id": 20, "text": "A alfabetização é a base para a inclusão social, possibilitando que os indivíduos participem de forma ativa e crítica na sociedade."},
    {"id": 21, "text": "A ludicidade na educação é uma estratégia eficaz para o engajamento dos alunos, promovendo o aprendizado através de atividades recreativas."},
    {"id": 22, "text": "O currículo escolar deve refletir as necessidades e interesses dos alunos, promovendo um aprendizado relevante e contextualizado."},
    {"id": 23, "text": "A gestão democrática da escola envolve a participação de toda a comunidade escolar na tomada de decisões."},
    {"id": 24, "text": "O planejamento pedagógico é um processo fundamental para o sucesso das práticas educativas."},
    {"id": 25, "text": "A afetividade na relação professor-aluno é um elemento central para o desenvolvimento de um ambiente de aprendizado positivo e acolhedor."},
    {"id": 26, "text": "A educação infantil é a primeira etapa da formação escolar e desempenha um papel crucial no desenvolvimento cognitivo, emocional e social das crianças."},
    {"id": 27, "text": "A avaliação formativa é uma prática que visa acompanhar o progresso dos alunos ao longo do processo educativo."},
    {"id": 28, "text": "A aprendizagem colaborativa estimula o desenvolvimento de habilidades interpessoais e o trabalho em equipe."},
    {"id": 29, "text": "O ensino híbrido combina o aprendizado presencial com atividades online, oferecendo mais flexibilidade ao aluno."},
    {"id": 30, "text": "As avaliações diagnósticas ajudam a identificar as dificuldades dos alunos logo no início do processo educativo."},
    {"id": 31, "text": "A gestão do tempo é uma habilidade crucial para o sucesso acadêmico, ajudando os alunos a organizarem suas atividades."},
    {"id": 32, "text": "A motivação intrínseca é fundamental para que o aluno se sinta engajado no processo de aprendizagem."},
    {"id": 33, "text": "As competências socioemocionais são tão importantes quanto os conhecimentos acadêmicos para a formação de cidadãos completos."},
    {"id": 34, "text": "A prática reflexiva permite que o professor ajuste suas metodologias conforme as necessidades da turma."},
    {"id": 35, "text": "A leitura crítica promove a capacidade de interpretar e questionar o mundo ao redor, tornando os alunos cidadãos mais conscientes."},
    {"id": 36, "text": "O ensino personalizado ajusta o ritmo de aprendizado às necessidades específicas de cada aluno."},
    {"id": 37, "text": "A educação integral busca desenvolver todas as dimensões do ser humano: física, emocional, social e cognitiva."},
    {"id": 38, "text": "A pesquisa científica é uma ferramenta fundamental para a construção de novos conhecimentos."},
    {"id": 39, "text": "O ensino à distância se consolidou como uma alternativa viável para democratizar o acesso à educação."},
    {"id": 40, "text": "A participação da família no processo educativo é essencial para o desenvolvimento completo do aluno."},
    {"id": 41, "text": "A prática interdisciplinar possibilita a construção de saberes que dialogam com diferentes áreas do conhecimento."},
    {"id": 42, "text": "O uso de jogos educativos tem se mostrado eficaz na construção de habilidades e no desenvolvimento do raciocínio lógico."},
    {"id": 43, "text": "A formação docente contínua é essencial para acompanhar as inovações pedagógicas e tecnológicas."},
    {"id": 44, "text": "A mediação tecnológica na educação facilita o acesso a materiais e informações de qualidade, além de ampliar as possibilidades de ensino."},
    {"id": 45, "text": "A gamificação na educação utiliza elementos de jogos para engajar e motivar os alunos no processo de aprendizagem."},
    {"id": 46, "text": "A diversidade na sala de aula deve ser valorizada e considerada na construção das práticas pedagógicas."},
    {"id": 47, "text": "A formação de professores em tecnologias digitais tem se mostrado um fator chave para a modernização do ensino."}
], key=lambda x: len(x['text']))  # Ordena os textos pelo tamanho

# Função para obter o próximo texto em ordem
def get_ordered_text(index):
    """Retorna o texto e o ID na posição especificada pela ordem de dificuldade"""
    if index < len(TEXTS):
        return TEXTS[index]
    else:
        return None  # Se o índice exceder o número de textos, retorna None
