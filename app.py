from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json

app = Flask(__name__)
app.secret_key = 'Sussurros Literários_secret_key_2025'

LIVROS = {
    1: {
        'id': 1,
        'titulo': 'As vantagens de ser invisível',
        'autor': 'Stephen Chbosky',
        'genero': 'Romance',
        'editora': 'MTV Books/Pocket Books',
        'sinopse': 'Manter-se à margem oferece uma única e passiva perspectiva. Mas, de uma hora para outra, sempre chega o momento de encarar a vida do centro dos holofotes. As cartas de Charlie são estranhas e únicas, hilárias e devastadoras.',
        'capa': '/static/images/livros/1.jpg',
        'nota': 4.7
    },
    2: {
        'id': 2,
        'titulo': 'É assim que acaba',
        'autor': 'Colleen Hoover',
        'genero': 'Romance',
        'editora': 'Galera',
        'sinopse': 'Lily se mudou de uma cidadezinha do Maine para Boston, se formou em marketing e abriu a própria floricultura. Quando conhece Ryle, um neurocirurgião confiante, ela se apaixona. Mas será que ela conseguirá enxergar a realidade do relacionamento?',
        'capa': '/static/images/livros/2.jpg',
        'nota': 4.8
    },
    3: {
        'id': 3,
        'titulo': 'Imperfeitos',
        'autor': 'Christina Lauren',
        'genero': 'Romance',
        'editora': 'Faro',
        'sinopse': 'Olive e Ethan são inimigos mortais. Mas quando são obrigados a dividir uma viagem de lua-de-mel ao Havaí, entre farpas e sarcasmos, descobrem que onde tem raiva tem fogo.',
        'capa': '/static/images/livros/3.jpg',
        'nota': 4.6
    },
    4: {
        'id': 4,
        'titulo': 'A culpa é das estrelas',
        'autor': 'John Green',
        'genero': 'Romance',
        'editora': 'E. P. Dutton',
        'sinopse': 'Hazel foi diagnosticada com câncer aos treze anos. Aos dezesseis, sobrevive graças a uma droga revolucionária. Ela passa os dias vendo tevê e lendo, mas sua vida muda quando conhece Augustus Waters.',
        'capa': '/static/images/livros/4.jpg',
        'nota': 4.9
    },
    5: {
        'id': 5,
        'titulo': 'Verity',
        'autor': 'Colleen Hoover',
        'genero': 'Suspense psicológico',
        'editora': 'Galera Record',
        'sinopse': 'Lowen Ashleigh, uma escritora em dificuldades, aceita terminar uma série de livros de Verity Crawford, uma famosa autora incapacitada. Ao se mudar para a casa de Verity, Lowen descobre um manuscrito perturbador com confissões sombrias que a fazem duvidar de tudo e de todos ao seu redor.',
        'capa': '/static/images/livros/5.jpg',
        'nota': 4.9
    },
    6: {
        'id': 6,
        'titulo': 'Dom Casmurro',
        'autor': 'Machado de Assis',
        'genero': 'Romance',
        'editora': 'Livraria Garnier',
        'sinopse': 'Bento Santiago retoma a infância na Rua de Matacavalos e conta a história do amor e das desventuras que viveu com Capitu, uma das personagens mais enigmáticas da literatura brasileira.',
        'capa': '/static/images/livros/6.jpg',
        'nota': 4.5
    },
    7: {
        'id': 7,
        'titulo': 'De Sangue e Cinzas',
        'autor': 'Jennifer L. Armentrout',
        'genero': 'Fantasia, Romance',
        'editora': 'Galera Record',
        'sinopse': 'Poppy foi escolhida desde o nascimento para ser A Donzela, uma figura sagrada que deve permanecer intocada até o dia de sua Ascensão. Mas ela deseja viver e lutar pelo próprio destino. Quando conhece Hawke, um guarda misterioso, tudo que ela acreditava começa a ruir, revelando segredos que mudarão o reino para sempre.',
        'capa': '/static/images/livros/7.jpg',
        'nota': 4.9
    },
    8: {
        'id': 8,
        'titulo': 'Em Chamas',
        'autor': 'Suzanne Collins',
        'genero': 'Ficção científica, Distopia, Ação',
        'editora': 'Rocco',
        'sinopse': 'Após vencer os Jogos, Katniss e Peeta se tornam símbolos de esperança para o povo oprimido. A Capital, temendo uma rebelião, decide realizar uma nova edição dos Jogos — reunindo apenas campeões anteriores. Katniss volta à arena, agora lutando por algo muito maior.',
        'capa': '/static/images/livros/8.jpg',
        'nota': 4.9
    },
    9: {
        'id': 9,
        'titulo': 'Trono de vidro',
        'autor': 'Sarah J. Maas',
        'genero': 'Fantasia',
        'editora': 'Bloomsbury',
        'sinopse': 'Celaena Sardothien é uma assassina de 18 anos. Aprisionada, ela recebe uma proposta: lutar em uma competição mortal pelo rei. Se vencer, será livre depois de alguns anos de serviço.',
        'capa': '/static/images/livros/9.jpg',
        'nota': 4.6
    },
    10: {
        'id': 10,
        'titulo': 'Orgulho e Preconceito',
        'autor': 'Jane Austen',
        'genero': 'Romance',
        'editora': 'T. Egerton, Whitehall',
        'sinopse': 'Elizabeth Bennet vive no campo inglês e enfrenta pressão para se casar. Quando conhece o rico e reservado Darcy, faíscas voam, mas sua natureza ameaça o relacionamento.',
        'capa': '/static/images/livros/10.jpg',
        'nota': 4.7
    },
    11: {
        'id': 11,
        'titulo': 'A Esperança',
        'autor': 'Suzanne Collins',
        'genero': 'Ficção científica, Distopia, Drama',
        'editora': 'Rocco',
        'sinopse': 'Katniss torna-se o símbolo da revolução contra a Capital. No meio da guerra, ela precisa lidar com perdas, dilemas morais e o peso de ser o “Tordo” — a esperança de um povo que luta por liberdade.',
        'capa': '/static/images/livros/11.jpg',
        'nota': 4.9
    },
    12: {
        'id': 12,
        'titulo': 'A Cantiga dos Pássaros e das Serpentes',
        'autor': 'Suzanne Collins',
        'genero': 'Ficção científica, Distopia, Prelúdio',
        'editora': 'Rocco',
        'sinopse': 'Décadas antes de Katniss, acompanhamos a juventude de Coriolanus Snow, futuro presidente da Capital. Designado como mentor de uma tributo do Distrito 12, ele começa a descobrir a complexidade dos Jogos e os caminhos que o levarão ao poder.',
        'capa': '/static/images/livros/12.jpg',
        'nota': 4.9
    },
    13: {
        'id': 13,
        'titulo': 'Não mate a vilã',
        'autor': 'J. F. S.',
        'genero': 'Fantasia',
        'editora': 'Amazon Kindle',
        'sinopse': 'Silvia sofre um acidente e acorda no corpo da vilã de um livro que acabou de ler. Condenada à morte, ela precisa mudar seu destino e sobreviver em um mundo onde nada é o que parece.',
        'capa': '/static/images/livros/13.jpg',
        'nota': 4.5
    },
    14: {
        'id': 14,
        'titulo': 'Jogos Vorazes',
        'autor': 'Suzanne Collins',
        'genero': 'Ficção Científica',
        'editora': 'Scholastic',
        'sinopse': 'Em Panem, doze distritos são comandados pela Capital. Todo ano, um garoto e uma garota de cada distrito são forçados a lutar até a morte nos Jogos Vorazes, transmitidos ao vivo pela TV.',
        'capa': '/static/images/livros/14.jpg',
        'nota': 4.8
    },
    15: {
        'id': 15,
        'titulo': 'Dias Perfeitos',
        'autor': 'Raphael Montes',
        'genero': 'Suspense psicológico',
        'editora': 'Companhia das Letras',
        'sinopse': 'Téo é um jovem estudante de medicina que leva uma vida tranquila até conhecer Clarice, uma garota livre e imprevisível. A partir desse encontro, sua rotina muda completamente, revelando um lado sombrio de sua personalidade.',
        'capa': '/static/images/livros/15.jpg',
        'nota': 4.6
    },
    16: {
        'id': 16,
        'titulo': 'Divergente',
        'autor': 'Veronica Roth',
        'genero': 'Ficção Científica',
        'editora': 'Rocco',
        'sinopse': 'Em uma sociedade dividida em facções baseadas em virtudes, Beatrice descobre ser uma divergente — alguém que não se encaixa em nenhum grupo — e passa a lutar contra um sistema que tenta controlá-la.',
        'capa': '/static/images/livros/16.jpg',
        'nota': 4.6
    },
    17: {
        'id': 17,
        'titulo': 'Maze Runner: Correr ou Morrer',
        'autor': 'James Dashner',
        'genero': 'Ficção Científica',
        'editora': 'Vergara & Riba',
        'sinopse': 'Thomas acorda em um labirinto sem memória e, junto de outros garotos, precisa desvendar os mistérios do lugar enquanto luta para sobreviver a perigos mortais.',
        'capa': '/static/images/livros/17.jpg',
        'nota': 4.5
    },
    18: {
        'id': 18,
        'titulo': 'A Seleção',
        'autor': 'Kiera Cass',
        'genero': 'Romance / Distopia',
        'editora': 'Seguinte',
        'sinopse': 'Em um futuro monárquico, trinta e cinco garotas competem pelo coração do príncipe Maxon e pela chance de mudar de vida — mas America Singer tem outros planos.',
        'capa': '/static/images/livros/18.jpg',
        'nota': 4.4
    },
    19: {
        'id': 19,
        'titulo': '1984',
        'autor': 'George Orwell',
        'genero': 'Ficção Distópica',
        'editora': 'Companhia das Letras',
        'sinopse': 'Em um regime totalitário que vigia todos os cidadãos, Winston Smith começa a questionar a verdade imposta pelo Partido e arrisca tudo em busca de liberdade e autenticidade.',
        'capa': '/static/images/livros/19.jpg',
        'nota': 4.9
    },
    20: {
        'id': 20,
        'titulo': 'A Revolução dos Bichos',
        'autor': 'George Orwell',
        'genero': 'Sátira / Política',
        'editora': 'Companhia das Letras',
        'sinopse': 'Em uma fazenda, os animais se rebelam contra os humanos, mas a luta por igualdade rapidamente se transforma em um novo regime de opressão.',
        'capa': '/static/images/livros/20.jpg',
        'nota': 4.7
    },
    21: {
        'id': 21,
        'titulo': 'A Mulher no Escuro',
        'autor': 'Raphael Montes',
        'genero': 'Suspense Psicológico',
        'editora': 'Companhia das Letras',
        'sinopse': 'Vítima de um trauma na infância, Victória leva uma vida reclusa até conhecer um homem que parece trazer luz de volta à sua rotina. Mas o passado nunca desaparece por completo.',
        'capa': '/static/images/livros/21.jpg',
        'nota': 4.6
    },
    22: {
        'id': 22,
        'titulo': 'O Vilarejo',
        'autor': 'Raphael Montes',
        'genero': 'Terror / Suspense',
        'editora': 'Suma de Letras',
        'sinopse': 'Em um pequeno vilarejo isolado, sete histórias se entrelaçam, cada uma inspirada em um dos sete pecados capitais. O resultado é um retrato perturbador da natureza humana.',
        'capa': '/static/images/livros/22.jpg',
        'nota': 4.7
    }
}

USUARIOS = {
    'emilly': {
        'id': 'emilly',
        'nome': 'Emilly',
        'email': 'emilly@livros.com.br',
        'foto': '/static/images/profile/emi.jpg',
        'generos_favoritos': ['Suspense psicológico', 'Romance'],
        'livros_lidos': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        'avaliacoes': {1: 4.8, 2: 5, 3: 4.8, 4: 4, 5: 4.9, 6: 4, 7: 5, 8: 4.8, 9: 5, 10: 5, 11: 4.7, 12: 4.6, 13: 4, 14: 5}
    },
    'vitor': {
        'id': 'vitor',
        'nome': 'Vitor',
        'email': 'vitor@livros.com.br',
        'foto': '/static/images/profile/vitor.jpg',
        'generos_favoritos': ['Ficção Científica', 'Romance'],
        'livros_lidos': [14, 6, 16, 17, 18, 19, 20],
        'avaliacoes': {16: 4, 17: 4.5, 18: 4.9, 19: 4.7, 20: 5, 14: 5, 6: 4.9}
    },
    'carolina': {
        'id': 'carolina',
        'nome': 'Carolina',
        'email': 'carolina@livros.com.br',
        'foto': '/static/images/profile/carol.jpg',
        'generos_favoritos': ['Romance'],
        'livros_lidos': [2, 16, 15, 22, 21],
        'avaliacoes': {22: 5, 21: 5, 15: 4, 2: 5, 16: 5}
    },
    'lucas': {
        'id': 'lucas',
        'nome': 'Lucas',
        'email': 'lucas@livros.com.br',
        'foto': '/static/images/profile/lucas.jpg',
        'generos_favoritos': ['Romance'],
        'livros_lidos': [1, 3, 14, 16, 17],
        'avaliacoes': {1: 4, 3: 4, 16: 4.8, 17: 4.9, 14: 5}
    }
}

AUTORES = {
    'Stephen Chbosky': {
        'livros': [1],
        'bio': 'Escritor e cineasta americano, autor do aclamado romance "As vantagens de ser invisível".'
    },
    'Colleen Hoover': {
        'livros': [2, 5],
        'bio': 'Escritora americana de romances contemporâneos e thrillers psicológicos. Conhecida por obras intensas e emocionais.'
    },
    'Christina Lauren': {
        'livros': [3],
        'bio': 'Dupla de autoras americanas (Christina Hobbs e Lauren Billings), conhecidas por romances leves e divertidos.'
    },
    'John Green': {
        'livros': [4],
        'bio': 'Escritor, vlogger e produtor americano. Autor de romances adolescentes de grande sucesso como "A culpa é das estrelas".'
    },
    'Machado de Assis': {
        'livros': [6],
        'bio': 'Escritor brasileiro, considerado o maior nome da literatura nacional, autor de "Dom Casmurro" e fundador da Academia Brasileira de Letras.'
    },
    'Jennifer L. Armentrout': {
        'livros': [7],
        'bio': 'Autora americana de fantasia e romance, conhecida por séries de sucesso como "De Sangue e Cinzas" e "Lux".'
    },
    'Suzanne Collins': {
        'livros': [8, 11, 12, 14],
        'bio': 'Escritora americana de ficção científica distópica, criadora da saga "Jogos Vorazes".'
    },
    'Sarah J. Maas': {
        'livros': [9],
        'bio': 'Escritora americana de fantasia jovem adulta, autora das séries "Trono de Vidro" e "Corte de Espinhos e Rosas".'
    },
    'Jane Austen': {
        'livros': [10],
        'bio': 'Romancista inglesa do período regencial, conhecida por suas críticas sociais e personagens femininas fortes.'
    },
    'J. F. S.': {
        'livros': [13],
        'bio': 'Autora brasileira de fantasia e romance, conhecida por narrativas com reviravoltas e universos alternativos.'
    },
    'Raphael Montes': {
        'livros': [15, 21, 22],
        'bio': 'Escritor e roteirista brasileiro, reconhecido por suas histórias de suspense, terror e psicologia sombria.'
    },
    'Veronica Roth': {
        'livros': [16],
        'bio': 'Autora americana de ficção científica e distopia, famosa pela série "Divergente".'
    },
    'James Dashner': {
        'livros': [17],
        'bio': 'Escritor americano de ficção científica e aventura, autor da série "Maze Runner".'
    },
    'Kiera Cass': {
        'livros': [18],
        'bio': 'Autora americana de romances distópicos e de época, conhecida pela série "A Seleção".'
    },
    'George Orwell': {
        'livros': [19, 20],
        'bio': 'Escritor e jornalista britânico, autor de clássicos distópicos como "1984" e "A Revolução dos Bichos".'
    }
}

GENEROS = {
    'Romance': {
        'livros': [1, 2, 3, 4, 6, 10, 18],
        'cor': '#e74c3c'
    },
    'Fantasia': {
        'livros': [7, 9, 13],
        'cor': '#9b59b6'
    },
    'Ficção científica': {
        'livros': [8, 11, 12, 14, 16, 17, 19],
        'cor': '#3498db'
    },
    'Distopia': {
        'livros': [8, 11, 12, 14, 16, 18, 19],
        'cor': '#1abc9c'
    },
    'Drama': {
        'livros': [11],
        'cor': '#f39c12'
    },
    'Suspense psicológico': {
        'livros': [21, 5],
        'cor': '#34495e'
    },
    'Terror / Suspense': {
        'livros': [22],
        'cor': '#7f8c8d'
    },
    'Sátira / Política': {
        'livros': [20],
        'cor': '#c0392b'
    }
}

def get_recomendacoes(usuario_id):
    if usuario_id not in USUARIOS:
        return []
    
    usuario = USUARIOS[usuario_id]
    livros_lidos = set(usuario['livros_lidos'])
    generos_favoritos = set(usuario['generos_favoritos'])
    
    recomendacoes = {}
    for outro_id, outro_usuario in USUARIOS.items():
        if outro_id == usuario_id:
            continue
        
        livros_em_comum = livros_lidos.intersection(set(outro_usuario['livros_lidos']))
        if len(livros_em_comum) >= 1:
            for livro_id in outro_usuario['livros_lidos']:
                if livro_id not in livros_lidos:
                    recomendacoes[livro_id] = recomendacoes.get(livro_id, 0) + 1
    
    livros_recomendados = sorted(recomendacoes.items(), key=lambda x: x[1], reverse=True)
    return [LIVROS[livro_id] for livro_id, _ in livros_recomendados[:6]]

def get_leitores_similares(usuario_id):
    if usuario_id not in USUARIOS:
        return []
    
    usuario = USUARIOS[usuario_id]
    livros_lidos = set(usuario['livros_lidos'])
    
    similares = []
    for outro_id, outro_usuario in USUARIOS.items():
        if outro_id == usuario_id:
            continue
        
        livros_em_comum = livros_lidos.intersection(set(outro_usuario['livros_lidos']))
        if len(livros_em_comum) > 0:
            similares.append({
                'usuario': outro_usuario,
                'livros_em_comum': len(livros_em_comum)
            })
    
    return sorted(similares, key=lambda x: x['livros_em_comum'], reverse=True)

@app.route('/')
def index():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('dashboard'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').lower()
        for usuario_id, dados in USUARIOS.items():
            if dados['email'] == email:
                session['usuario_id'] = usuario_id
                return redirect(url_for('dashboard'))
        return render_template('login.html', erro='Usuário não encontrado')
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        return render_template('cadastro.html', sucesso=True)
    return render_template('cadastro.html')

@app.route('/logout')
def logout():
    session.pop('usuario_id', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    usuario_id = session['usuario_id']
    usuario = USUARIOS[usuario_id]
    recomendacoes = get_recomendacoes(usuario_id)
    
    return render_template('dashboard.html', usuario=usuario, recomendacoes=recomendacoes)

@app.route('/perfil')
@app.route('/perfil/<usuario_id>')
def perfil(usuario_id=None):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    if usuario_id is None:
        usuario_id = session['usuario_id']
    
    if usuario_id not in USUARIOS:
        return "Usuário não encontrado", 404
    
    usuario = USUARIOS[usuario_id]
    livros_lidos = [LIVROS[lid] for lid in usuario['livros_lidos']]
    leitores_similares = get_leitores_similares(usuario_id)
    
    return render_template('perfil.html', 
                         usuario=usuario, 
                         livros_lidos=livros_lidos,
                         leitores_similares=leitores_similares,
                         avaliacoes=usuario['avaliacoes'])

@app.route('/livro/<int:livro_id>')
def livro(livro_id):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    if livro_id not in LIVROS:
        return "Livro não encontrado", 404
    
    livro = LIVROS[livro_id]
    
    similares = []
    for lid, l in LIVROS.items():
        if lid != livro_id and (l['genero'] == livro['genero'] or l['autor'] == livro['autor']):
            similares.append(l)
    
    leitores = []
    for uid, u in USUARIOS.items():
        if livro_id in u['livros_lidos']:
            leitores.append(u)
    
    return render_template('livro.html', 
                         livro=livro, 
                         similares=similares[:4],
                         leitores=leitores[:6])

@app.route('/explorar')
def explorar():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    return render_template('explorar.html')

@app.route('/api/grafo')
def api_grafo():
    tipo = request.args.get('tipo', 'completo')
    id_ref = request.args.get('id')
    
    nodes = []
    edges = []
    
    if tipo == 'completo':
        for uid, u in USUARIOS.items():
            nodes.append({
                'id': f'user_{uid}',
                'label': u['nome'],
                'group': 'usuario',
                'title': f"Leitor: {u['nome']}"
            })
        
        for lid, l in LIVROS.items():
            nodes.append({
                'id': f'book_{lid}',
                'label': l['titulo'],
                'group': 'livro',
                'title': f"Livro: {l['titulo']}\nAutor: {l['autor']}"
            })
        
        for autor in AUTORES.keys():
            nodes.append({
                'id': f'author_{autor}',
                'label': autor,
                'group': 'autor',
                'title': f"Autor: {autor}"
            })
        
        for genero in GENEROS.keys():
            nodes.append({
                'id': f'genre_{genero}',
                'label': genero,
                'group': 'genero',
                'title': f"Gênero: {genero}"
            })
        
        for uid, u in USUARIOS.items():
            for lid in u['livros_lidos']:
                edges.append({
                    'from': f'user_{uid}',
                    'to': f'book_{lid}',
                    'label': 'LEU',
                    'arrows': 'to'
                })
        
        for lid, l in LIVROS.items():
            edges.append({
                'from': f'author_{l["autor"]}',
                'to': f'book_{lid}',
                'label': 'ESCREVEU',
                'arrows': 'to'
            })
            edges.append({
                'from': f'book_{lid}',
                'to': f'genre_{l["genero"]}',
                'label': 'PERTENCE_A',
                'arrows': 'to'
            })
    
    elif tipo == 'usuario' and id_ref:
        if id_ref in USUARIOS:
            u = USUARIOS[id_ref]
            nodes.append({
                'id': f'user_{id_ref}',
                'label': u['nome'],
                'group': 'usuario',
                'title': f"Leitor: {u['nome']}"
            })
            
            for lid in u['livros_lidos']:
                l = LIVROS[lid]
                nodes.append({
                    'id': f'book_{lid}',
                    'label': l['titulo'],
                    'group': 'livro',
                    'title': f"Livro: {l['titulo']}"
                })
                edges.append({
                    'from': f'user_{id_ref}',
                    'to': f'book_{lid}',
                    'label': 'LEU',
                    'arrows': 'to'
                })
            
            similares = get_leitores_similares(id_ref)
            for sim in similares[:3]:
                outro_id = sim['usuario']['id']
                nodes.append({
                    'id': f'user_{outro_id}',
                    'label': sim['usuario']['nome'],
                    'group': 'usuario',
                    'title': f"Leitor: {sim['usuario']['nome']}"
                })
                edges.append({
                    'from': f'user_{id_ref}',
                    'to': f'user_{outro_id}',
                    'label': 'SIMILAR',
                    'dashes': True
                })
    
    return jsonify({'nodes': nodes, 'edges': edges})

@app.route('/buscar')
def buscar():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    query = request.args.get('q', '').lower()
    resultados = []
    
    if query:
        for lid, l in LIVROS.items():
            if query in l['titulo'].lower() or query in l['autor'].lower() or query in l['genero'].lower():
                resultados.append({
                    'tipo': 'livro',
                    'id': lid,
                    'titulo': l['titulo'],
                    'subtitulo': f"{l['autor']} - {l['genero']}",
                    'url': url_for('livro', livro_id=lid)
                })
        
        for autor in AUTORES.keys():
            if query in autor.lower():
                resultados.append({
                    'tipo': 'autor',
                    'titulo': autor,
                    'subtitulo': 'Autor',
                    'url': '#'
                })
    
    return render_template('buscar.html', query=query, resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
