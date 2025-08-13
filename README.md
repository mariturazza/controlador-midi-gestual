# Maestro – Música que Conecta

**Maestro** é uma iniciativa que une **educação**, **inclusão social** e **tecnologia**, utilizando **gestos capturados por câmera** para **configurar e reproduzir sons**. É voltado para escolas públicas, projetos sociais, hospitais e centros de reabilitação, oferecendo experiências acessíveis e inovadoras de **musicoterapia** e **criatividade musical**.

### Sobre o Projeto

Com base na leitura de **gestos das mãos em tempo real via câmera**, o Maestro transforma movimentos em **notas musicais, ritmos e efeitos sonoros**. Os usuários podem interagir com diferentes configurações, personalizar sons e explorar a criação musical de forma simples e intuitiva.

### Objetivos

- Estimular o **aprendizado por meio da música**;
- Promover a **inclusão de pessoas com deficiência** e de comunidades vulneráveis;
- Usar a **musicoterapia** para o bem-estar emocional e reabilitação;
- Criar um ambiente lúdico e educativo com foco em **criatividade e expressão corporal**.

### Tecnologias Utilizadas

- **HTML / CSS / JS** – Interface web
- **Python / OpenCV / MediaPipe (ou alternativa)** – Reconhecimento de gestos com câmera
- **Web Audio API / Pygame / MIDI** – Reprodução e manipulação de sons
- **Git / GitHub** – Controle de versão

### Como Funciona

1. O usuário posiciona as mãos em frente à câmera;
2. O sistema identifica os gestos e os traduz em comandos;
3. Sons são reproduzidos com base nos gestos;
4. É possível configurar diferentes "instrumentos", intensidades e efeitos.

### Como Rodar o Projeto Maestro

#### 1. Clonar o Repositório

Abra o terminal e execute:

```bash
git clone https://github.com/mariturazza/controlador-midi-gestual.git
cd controlador-midi-gestual
git branch
git switch desenvolvimento
code .
```
#### 2. Configurar o Ambiente Python

- Crie o ambiente virtual:

```bash
python -m venv .venv
```

- Ative o ambiente:

```bash
# Windows
.\.venv\Scripts\activate
```

- Instale as dependëncias:

```bash
pip install -r requirements.txt
```

- Instale a extensão Live Server no VS Code (para testes da interface web).

#### 3. Configurações do Projeto

- Navegue para a pasta do backend:

```bash
cd .\backend\
```

- Configure a porta MIDI em config\config.py:

```bash
MIDI_PORT_NAME = "loopMIDI Port 1"
```

#### 4. Instalar Aplicativos Necessários

- **Reaper** – DAW para reprodução e roteamento de áudio/MIDI.
- **loopMIDI** – Para criar portas MIDI virtuais.
- ⚠️ É necessário instalar também o **Microsoft Visual C++ 2010 Redistributable**, exigido por alguns plugins.


#### 5. Instalar VSTs Adicionais

- **MT Power Drum Kit** – [Download](https://www.powerdrumkit.com/download76187.php)  
- **Ample Guitar M Lite II** – [Download](https://plugins4free.com/plugin/2233/)  

> Durante a instalação, escolha uma **pasta padrão para VSTs**.  
> Recomendado: `C:\Program Files\Common Files\VST3`


#### 6. Configurar o loopMIDI

1. Abra o **loopMIDI**.  
2. Clique no botão **+** para criar uma nova porta.  
3. O nome da porta deve ser **idêntico** ao configurado em `MIDI_PORT_NAME` no código.

#### 7. Configurar o Reaper

1. Abra o **Reaper**.  
2. Vá em **Options → Preferences → Audio → Device**:  
   - Configure as entradas e saídas de áudio.  
   - Em **MIDI Inputs**, clique com o botão direito na porta criada no loopMIDI e selecione:  
     - **Enable input for track / record input**  
     - **Include input in 'All MIDI Inputs'**  
     - **Enable input for control messages**  
3. Vá em **Options → Preferences → Plug-ins → VST → Edit path list**:  
   - Adicione a pasta onde você instalou os VSTs adicionais.  
4. Vá em **File → Open Project**:  
   - Abra o arquivo `.RPP` incluído no repositório.

#### 8. Executar o Maestro

- Com o ambiente virtual ativo e a porta MIDI configurada, execute:

```bash
python midi_gesture_controler.py
```
- Posicione suas mãos em frente à câmera e interaja com os gestos para tocar instrumentos.

#### Observações Importantes

- Certifique-se de que o loopMIDI esteja rodando antes do Reaper.
- As VSTs adicionais são necessárias para reproduzir bateria e guitarra com qualidade.
- Ajuste o MIDI_PORT_NAME caso altere o nome da porta virtual.
- Para problemas de som ou latência, verifique as configurações de áudio do Reaper.


*"A música pode mudar o mundo porque pode mudar as pessoas." – Bono Vox*