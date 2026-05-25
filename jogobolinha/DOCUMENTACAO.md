# Documentação do projeto — comentários no código

Todos os arquivos principais foram comentados em **português** para facilitar estudo e manutenção.

## Mapa dos arquivos

### Jogo das bolinhas (Hand Slicer / LOGICA - SENAI)

| Arquivo | Descrição |
|---------|-----------|
| `index.html` | Versão **única** para GitHub Pages (HTML + JS + MediaPipe CDN) |
| `src/components/HandTrackingGame.tsx` | Mesmo jogo no projeto Next.js — **arquivo principal das bolinhas** |
| `src/app/hand-slicer/page.tsx` | Rota `/hand-slicer` que carrega o componente acima |

### Hand Rhythm (ritmo + música)

| Arquivo | Descrição |
|---------|-----------|
| `src/components/HandRhythmGame.tsx` | UI + loop do rhythm game |
| `src/lib/gameEngine.ts` | Gera círculos, detecta acertos, pontuação |
| `src/lib/renderer.ts` | Desenho no canvas |
| `src/lib/essentiaAnalyzer.ts` | Análise de BPM/batidas do áudio |
| `src/lib/constants.ts` | Dificuldade e tamanhos |
| `src/types/game.ts` | Tipos TypeScript |
| `src/app/hand-rhythm/page.tsx` | Rota `/hand-rhythm` |

### Pose Pong

| Arquivo | Descrição |
|---------|-----------|
| `src/app/pose-pong/PosePongGame.tsx` | Jogo completo (corpo + bola) |
| `src/app/pose-pong/PosePongClientWrapper.tsx` | Import dinâmico sem SSR |
| `src/app/pose-pong/page.tsx` | Rota `/pose-pong` |

### Bubble Shooter

| Arquivo | Descrição |
|---------|-----------|
| `src/app/hand-bubble-shooter/page.tsx` | Jogo inteiro neste arquivo |

### App Next.js

| Arquivo | Descrição |
|---------|-----------|
| `src/app/page.tsx` | Menu inicial com links para os 4 jogos |
| `src/app/layout.tsx` | Layout e fontes globais |
| `src/app/globals.css` | Tema Tailwind / cores |
| `next.config.ts` | Configuração Next.js |

### Configuração (comentário breve no topo)

- `eslint.config.mjs` — regras de lint
- `postcss.config.mjs` — Tailwind CSS

## Como rodar

```bash
npm install
npm run dev
```

Para só o jogo das bolinhas no GitHub: publique o `index.html` na raiz com GitHub Pages.
