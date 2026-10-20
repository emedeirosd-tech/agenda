# Projeto: Agenda de Compromissos

**Integrante:** Eduarda Medeiros Silva

## 1. Objetivo

Fazer um programa em Python para organizar compromissos. O usuário pode
**adicionar**, **ver** e **remover** compromissos da sua agenda.

## 2. Lógica (Regras de Negócio)

| Código | Regra |
|--------|-------|
| RN01 | O título do compromisso é obrigatório. |
| RN02 | A data é obrigatória. |
| RN03 | A hora é obrigatória. |
| RN04 | Não pode ter dois compromissos na mesma data e hora. |
| RN05 | A agenda aceita no máximo 10 compromissos. |
| RN06 | Para remover um compromisso, o programa pede confirmação (s/n). |

## 3. Possíveis telas

O projeto tem mais de uma tela e cada tela fica em um arquivo.

### Tela 1 - Menu principal (`main.py`)

```
===== MENU PRINCIPAL =====
1 - Abrir agenda
2 - Ver regras de negócio
0 - Sair
```

### Tela 2 - Agenda (`agenda.py`)

```
===== TELA DA AGENDA =====
1 - Adicionar compromisso
2 - Ver compromissos
3 - Remover compromisso
0 - Voltar
```

## 4. Arquivos do projeto

- `main.py`: tela inicial (menu principal)
- `agenda.py`: tela da agenda e regras de negócio

## 5. Como executar

Colocar os dois arquivos na mesma pasta e rodar no terminal:

```
python main.py
```

## 6. Melhorias para o futuro

- Salvar os compromissos em um arquivo (hoje eles somem quando o programa fecha)
- Editar um compromisso
- Validar se a data e a hora são válidas
