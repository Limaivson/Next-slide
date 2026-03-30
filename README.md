# 📊 Next Slide

Controle remoto de slides via rede local.  
Permite avançar ou voltar slides de um computador remoto.

---

## 🚀 Como funciona

O projeto tem dois lados:

### 🖥️ Servidor (apresentador)
- Fica rodando no computador que está apresentando
- Recebe comandos pela rede
- Usa `pyautogui` para simular teclas:
  - ➡️ seta direita → próximo slide
  - ⬅️ seta esquerda → slide anterior

---

### 🎮 Cliente (controle)
- Roda em outro computador
- Detecta automaticamente o servidor na rede (UDP broadcast)
- Envia comandos:
  - `"next"`
  - `"prev"`

---

## 🧱 Estrutura do projeto
```
Next-slide/
├── server.py # Servidor TCP + descoberta UDP
├── discovery.py # Descoberta do servidor na rede
├── client.py # Cliente que envia comandos
├── main_slide_owner.py # Inicializa o servidor
├── main_advance_slide.py # Controle via teclado
```

---

## ⚙️ Pré-requisitos

Instale as dependências:

```bash
pip install pyautogui keyboard
```
⚠️ Importante:

pyautogui controla o teclado/mouse
keyboard pode precisar de permissões de administrador no Linux

▶️ Como rodar
🖥️ 1. Rodar o servidor (no PC da apresentação)

```
python main_slide_owner.py
```

Saída esperada:
```
Discovery...
Server found
```

✔ Isso inicia:

Servidor TCP (porta 5000)
Discovery UDP (porta 5001)

🎮 2. Rodar o cliente (no PC de controle)
```
python main_advance_slide.py
```

Controles:

→ (seta direita) = próximo slide  
← (seta esquerda) = slide anterior  
s = sair

🔗 Comunicação
🔍 Descoberta automática

Cliente envia broadcast:
```
DISCOVER_SERVER
```

Servidor responde:
```
SERVER_HERE
```

📡 Comandos TCP

Comando	    Ação
next	    Próximo slide
prev	    Slide anterior

🧪 Fluxo completo

1. Servidor inicia (main_slide_owner.py)
2. Cliente inicia (main_advance_slide.py)
3. Cliente descobre IP automaticamente
4. Ao pressionar tecla:
    - envia comando via TCP
5. Servidor executa com pyautogui

⚠️ Problemas comuns

❌ Não encontra o servidor
 - Verifique se estão na mesma rede
 - Firewall pode estar bloqueando porta 5001 (UDP)

❌ Comando não funciona
 - Verifique se o foco está na apresentação (PowerPoint, PDF, etc.)
 - pyautogui depende da janela ativa

❌ Erro com keyboard no Linux

Execute com sudo:
```
sudo python main_advance_slide.py
```
