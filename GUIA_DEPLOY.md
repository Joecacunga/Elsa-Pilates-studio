# Guia de Deploy - ESTÚDIO ELSA PILATES

Este guia fornece instruções passo a passo para fazer o deploy da aplicação "ESTÚDIO ELSA PILATES" no Streamlit Cloud utilizando o GitHub.

## 📘 Resumo Rápido

| Etapa | Ação |
|-------|------|
| 🧱 Preparação | Ter o projeto pronto localmente |
| 📥 GitHub | Criar repositório e fazer upload dos ficheiros |
| 🌐 Streamlit Cloud | Conectar repositório e fazer deploy |
| ✅ Teste | Aceder à aplicação e testar funcionalidades |

---

## Passo 1: Preparar o Projeto Localmente

Antes de fazer o upload para o GitHub, certifique-se de que todos os ficheiros estão presentes e a aplicação funciona localmente.

### Estrutura de Ficheiros Necessária

```
estudio_elsa_pilates_streamlit/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .streamlit/
│   └── config.toml
├── database/
│   └── models.py
└── pages/
    ├── 1_👥_Gestão_de_Alunos.py
    ├── 2_📅_Gestão_de_Aulas.py
    ├── 3_💰_Gestão_Financeira.py
    ├── 4_🛒_Gestão_de_Produtos.py
    ├── 5_📈_Relatórios.py
    ├── 7_🛒_Loja.py
    ├── 8_💳_Pagamentos.py
    └── 9_👤_Meu_Perfil.py
```

### Testar Localmente

Execute a aplicação localmente para garantir que está a funcionar:

```bash
cd estudio_elsa_pilates_streamlit
pip install -r requirements.txt
streamlit run app.py
```

Aceda a `http://localhost:8501` e teste as funcionalidades principais.

---

## Passo 2: Criar Repositório no GitHub

### 2.1. Criar uma Conta no GitHub

Se ainda não tem uma conta no GitHub, aceda a [https://github.com](https://github.com) e crie uma conta gratuita.

### 2.2. Criar um Novo Repositório

1. Faça login no GitHub
2. Clique no botão **"+"** no canto superior direito e selecione **"New repository"**
3. Preencha os detalhes:
   - **Repository name**: `estudio-elsa-pilates` (ou outro nome à sua escolha)
   - **Description**: "Sistema de Gestão para Estúdios de Pilates"
   - **Visibilidade**: Escolha **Public** (para usar o Streamlit Cloud gratuito) ou **Private** (se tiver uma conta paga)
4. **Não** inicialize o repositório com README, .gitignore ou licença (já temos estes ficheiros)
5. Clique em **"Create repository"**

### 2.3. Fazer Upload dos Ficheiros

Existem duas formas de fazer o upload:

#### Opção A: Via Interface Web do GitHub (Mais Fácil)

1. No seu repositório recém-criado, clique em **"uploading an existing file"**
2. Arraste e solte todos os ficheiros e pastas do projeto
3. Adicione uma mensagem de commit (ex: "Initial commit")
4. Clique em **"Commit changes"**

#### Opção B: Via Git Command Line (Mais Profissional)

Se tem o Git instalado no seu computador:

```bash
cd estudio_elsa_pilates_streamlit
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/SEU_USERNAME/estudio-elsa-pilates.git
git push -u origin main
```

Substitua `SEU_USERNAME` pelo seu nome de utilizador do GitHub.

---

## Passo 3: Deploy no Streamlit Cloud

### 3.1. Criar uma Conta no Streamlit Cloud

1. Aceda a [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Clique em **"Sign up"** ou **"Get started"**
3. **Conecte com a sua conta do GitHub** (recomendado) ou crie uma conta com email

### 3.2. Conectar o Repositório GitHub

1. No dashboard do Streamlit Cloud, clique em **"New app"**
2. Autorize o Streamlit Cloud a aceder aos seus repositórios do GitHub (se solicitado)
3. Selecione o repositório **`estudio-elsa-pilates`** (ou o nome que escolheu)
4. Configure os detalhes do deploy:
   - **Branch**: `main` (ou `master`, dependendo do nome do branch)
   - **Main file path**: `app.py`
   - **App URL**: Escolha um nome único para o URL (ex: `estudio-elsa-pilates`)

### 3.3. Configurações Avançadas (Opcional)

Clique em **"Advanced settings"** se precisar de:
- Definir variáveis de ambiente (secrets)
- Escolher a versão do Python (recomendado: 3.11)
- Configurar recursos de memória

Para esta aplicação, as configurações padrão são suficientes.

### 3.4. Iniciar o Deploy

1. Clique em **"Deploy!"**
2. Aguarde enquanto o Streamlit Cloud:
   - Clona o repositório
   - Instala as dependências do `requirements.txt`
   - Inicia a aplicação
3. O processo geralmente demora 2-5 minutos

### 3.5. Aceder à Aplicação

Quando o deploy estiver concluído:
- O Streamlit Cloud fornecerá um URL público (ex: `https://estudio-elsa-pilates.streamlit.app`)
- Aceda ao URL e teste a aplicação
- Faça login com as credenciais de teste:
  - **Administrador**: `admin` / `password`
  - **Instrutor**: `instructor` / `password`
  - **Aluno**: `student` / `password`

---

## Passo 4: Atualizações Futuras

Sempre que fizer alterações ao código:

1. **Faça commit das alterações no GitHub**:
   - Via interface web: edite os ficheiros diretamente no GitHub e faça commit
   - Via Git: `git add .`, `git commit -m "Descrição da alteração"`, `git push`

2. **O Streamlit Cloud irá automaticamente**:
   - Detetar as alterações no repositório
   - Fazer redeploy da aplicação
   - Atualizar a aplicação em produção

---

## 🔒 Segurança e Boas Práticas

### Proteger Palavras-passe

Para uso em produção, **não armazene palavras-passe em texto simples**. Implemente:

1. **Hash de palavras-passe** usando `bcrypt` ou `argon2`
2. **Variáveis de ambiente** para secrets no Streamlit Cloud:
   - No dashboard do Streamlit Cloud, vá a **"Settings" > "Secrets"**
   - Adicione secrets no formato TOML:
     ```toml
     [passwords]
     admin = "hash_da_password_admin"
     ```

### Base de Dados em Produção

A base de dados SQLite incluída no repositório é reiniciada a cada deploy. Para dados persistentes:

1. **Use Streamlit Cloud Secrets** para armazenar dados sensíveis
2. **Considere uma base de dados externa** (ex: PostgreSQL no Heroku, Supabase, ou PlanetScale) para dados que precisam de persistir

### HTTPS

O Streamlit Cloud fornece automaticamente HTTPS para todas as aplicações, garantindo comunicação segura.

---

## 📞 Suporte

Se encontrar problemas durante o deploy:

1. **Verifique os logs** no Streamlit Cloud (botão "Manage app" > "Logs")
2. **Consulte a documentação oficial**: [https://docs.streamlit.io/streamlit-community-cloud](https://docs.streamlit.io/streamlit-community-cloud)
3. **Comunidade Streamlit**: [https://discuss.streamlit.io](https://discuss.streamlit.io)

---

## ✅ Checklist de Deploy

- [ ] Projeto testado localmente
- [ ] Repositório criado no GitHub
- [ ] Ficheiros enviados para o GitHub
- [ ] Conta criada no Streamlit Cloud
- [ ] Repositório conectado ao Streamlit Cloud
- [ ] Deploy iniciado e concluído
- [ ] Aplicação acessível via URL público
- [ ] Funcionalidades testadas em produção
- [ ] Credenciais de teste funcionam

---

**Parabéns!** A sua aplicação "ESTÚDIO ELSA PILATES" está agora disponível publicamente na internet através do Streamlit Cloud.

---

**Desenvolvido por**: Manus AI  
**Data**: Outubro de 2025

