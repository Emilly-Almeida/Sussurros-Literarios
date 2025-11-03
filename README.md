# <a href= "https://sussurros-literarios.onrender.com"> Sussurros Literários - Sistema de Recomendação de Livros com Grafos </a>

## Sobre o Projeto

**Sussurros Literários** é um protótipo visual interativo de sistema de recomendação de livros baseado em **banco de dados de grafos (Neo4j)**. O sistema conecta leitores, livros, autores, editoras e gêneros literários através de relações visuais representadas como nós e arestas.

## Funcionalidades

### 🏠 Dashboard
- Barra de busca por livro, autor ou gênero
- Recomendações personalizadas baseadas em gostos similares
- Botão "Explorar conexões" para visualização do grafo
- Estatísticas rápidas do usuário

### 👤 Tela de Perfil do Usuário
- Informações do leitor (nome, foto, preferências)
- Histórico de leitura com cards de livros e avaliações
- Gráfico de grafo mostrando conexões com outros leitores
- Visualização de leitores similares

### 📖 Tela de Detalhes do Livro
- Informações completas (capa, título, autor, gênero, sinopse, nota)
- Seção "Leitores que gostaram também leram..."
- Visualização de relações: [Autor] → [Livro] → [Gênero] → [Outros Livros]
- Leitores que gostaram do livro

### 🔍 Tela de Exploração de Grafos
- Visualização interativa com **Vis.js**
- Nós: Leitor, Livro, Autor, Gênero, Editora
- Arestas: LEU, GOSTOU_DE, PERTENCE_A, ESCREVEU
- Consultas exemplares em Cypher (Neo4j)
- Filtros por tipo de visualização

### 🔐 Tela de Login/Cadastro
- Formulário de autenticação
- Cadastro com seleção de gêneros favoritos
- Usuários de demonstração incluídos

## Usuários de Demonstração

Use qualquer um destes e-mails para fazer login (senha não é necessária):

- **emilly@livros.com.br** - Emilly (Fantasia, Ficção Científica)
- **vitor@livros.com.br** - Vitor (Ficção Científica, Romance)
- **carolina@livros.com.br** - Carolina (Fantasia, Romance)
- **lucas@livros.com.br** - Lucas (Fantasia)

## Dados Simulados

O sistema inclui dados mockados que simulam um banco de dados Neo4j:

- **14 Livros**: As vantagens de ser invisível, É assim que acaba, A culpa é das estrelas, Jogos Vorazes, etc.
- **4 Usuários**: Com diferentes preferências e históricos
- **14 Autores**: Stephen Chbosky, Colleen Hoover, John Green, etc.
- **4 Gêneros**: Romance, Fantasia, Ficção Científica, Filosofia

## Relações do Grafo

### Tipos de Nós
- **Usuario**: Leitores da plataforma
- **Livro**: Obras literárias
- **Autor**: Escritores
- **Genero**: Categorias literárias
- **Editora**: Casas publicadoras

### Tipos de Relações (Arestas)
- **LEU**: Usuário leu um livro
- **GOSTOU_DE**: Usuário gostou/avaliou um livro
- **ESCREVEU**: Autor escreveu um livro
- **PERTENCE_A**: Livro pertence a um gênero
- **PUBLICADO_POR**: Livro publicado por uma editora

## Objetivo Acadêmico

Este protótipo demonstra como **bancos de dados orientados a grafos (Neo4j)** permitem:

1. **Recomendações Inteligentes**: Baseadas em leitores similares e padrões de leitura
2. **Visualização de Relacionamentos**: Conexões complexas entre entidades
3. **Consultas Eficientes**: Queries Cypher para explorar relações
4. **Análise de Comunidades**: Identificação de grupos com gostos similares

## Tecnologias Utilizadas

- **Backend**: Python + Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Visualização de Grafos**: Vis.js Network
- **Design**: CSS Grid, Flexbox, Gradientes
- **Ícones**: Font Awesome 6

## Consultas Neo4j Exemplares

O sistema demonstra consultas Cypher típicas:

```cypher
// Livros que um usuário leu
MATCH (u:Usuario {nome: 'Emilly Cruz'})-[:LEU]->(l:Livro)
RETURN l.titulo

// Recomendações baseadas em leitores similares
MATCH (u:Usuario {nome: 'Emilly Cruz'})-[:LEU]->(:Livro)<-[:LEU]-(outros:Usuario)
MATCH (outros)-[:LEU]->(rec:Livro)
WHERE NOT (u)-[:LEU]->(rec)
RETURN rec.titulo, COUNT(*) as score
ORDER BY score DESC
```

