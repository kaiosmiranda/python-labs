# Lab G3 - Branch e Pull Request

**Objetivo:** Praticar o fluxo completo de trabalho com branches no Git — criar uma branch, fazer commits, abrir um Pull Request no GitHub, fazer o merge e limpar a branch local.

---

## 📝 Lista de Tarefas

### 1. Criar uma nova branch a partir da `main`

A convenção de nomenclatura de branches mais usada no mercado é o padrão **kebab-case** com um prefixo que indica o tipo de trabalho:

| Prefixo     | Quando usar                              | Exemplo                        |
|-------------|------------------------------------------|--------------------------------|
| `feature/`  | Nova funcionalidade                      | `feature/adiciona-calculo-media` |
| `fix/`      | Correção de bug                          | `fix/corrige-divisao-por-zero`   |
| `docs/`     | Documentação                             | `docs/atualiza-readme`           |
| `chore/`    | Manutenção / configuração               | `chore/configura-gitignore`      |
| `refactor/` | Refatoração sem mudança de comportamento | `refactor/simplifica-funcao`     |

> Esse padrão vem do *Conventional Commits* e é amplamente adotado em times que usam GitHub Flow ou GitFlow.

**Comando para criar e já entrar na branch:**
```bash
git checkout -b feature/lab-g3-branch-e-pull-request
```

---

### 2. Fazer alterações reais na branch (mínimo 2 commits)

**Commit 1 — Criar a pasta e o arquivo de notas:**
```bash
# (a pasta lab-g3 e o arquivo notas.md já existem, então apenas salve as edições)
git add lab-g3/notas.md
git commit -m "docs: adiciona notas do lab G3 sobre branches e pull requests"
```

**Commit 2 — Adicionar um arquivo de exemplo (opcional mas recomendado):**
```bash
# Crie um arquivo qualquer, ex: lab-g3/exemplo.py
git add lab-g3/
git commit -m "feat: adiciona arquivo de exemplo no lab G3"
```

---

### 3. Subir a branch para o GitHub e abrir um Pull Request

**Subir a branch:**
```bash
git push origin feature/lab-g3-branch-e-pull-request
```

**Abrir o Pull Request no GitHub:**
1. Acesse o repositório no GitHub
2. Clique em **"Compare & pull request"** (aparece automaticamente após o push)
3. Preencha com uma descrição real, por exemplo:

> **Título:** `docs: adiciona lab G3 - prática de branches e pull requests`
>
> **Descrição:**
> Este PR adiciona a pasta `lab-g3/` com as notas e exercícios referentes ao laboratório sobre branches e pull requests.
>
> **O que foi feito:**
> - Criação da branch `feature/lab-g3-branch-e-pull-request` a partir da `main`
> - Adição do arquivo `notas.md` com as instruções e conceitos do lab
> - Adição de arquivo de exemplo na pasta
>
> **Por quê:** Praticar o fluxo completo de trabalho com branches, simulando como é feito em times reais de desenvolvimento.

4. Clique em **"Create pull request"** — **não faça o merge ainda**

---

### 4. Fazer o merge pelo GitHub

1. No PR aberto, clique em **"Merge pull request"**
2. Confirme clicando em **"Confirm merge"**
3. Opcionalmente delete a branch remota pelo GitHub (ele oferece o botão logo após o merge)

---

### 5. Atualizar a `main` local e deletar a branch

**Voltar para a main e puxar as atualizações:**
```bash
git checkout main
git pull origin main
```

**Deletar a branch local:**
```bash
git branch -d feature/lab-g3-branch-e-pull-request
```

> `-d` é seguro: só deleta se a branch já foi mergeada. Use `-D` (maiúsculo) para forçar a deleção.

**Verificar que a branch foi removida:**
```bash
git branch
```

---

## ✅ Fluxo Resumido

```
main → cria branch → faz commits → push → abre PR → merge no GitHub → pull main local → deleta branch
```
