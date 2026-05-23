# Aplicação interativa com hand tracking

Hub de projetos com rastreamento de mãos (MediaPipe) e experiências 3D no navegador.

### Página inicial (desenvolvedor)
- Coloque sua foto em **`assets/avatar.jpg`** (200×200 px, rosto centralizado).
- Edite nome e subtítulo no cabeçalho de `index.html` (classe `.dev-name` e `.dev-role`).

### Como usar
1. Abra **`index.html`** — página inicial com links para todos os projetos.
2. Ou abra diretamente qualquer arquivo `.html` da pasta.

| Arquivo | Origem |
|---------|--------|
| `naruto.html` | — |
| `piano-neon.html` | [test33](https://smm.axtarget.xyz/test33.html) |
| `globo-3d.html` | [test6](https://smm.axtarget.xyz/test6.html) |
| `texto.html` | [test19](https://smm.axtarget.xyz/test19.html) |
| `particulas.html` | [test25](https://smm.axtarget.xyz/test25.html) |
| `esfera.html` | [test9](https://smm.axtarget.xyz/test9.html) |
| `teclado-virtual.html` | [test16](https://smm.axtarget.xyz/test16.html) |
| `simbiote.html` | [test24](https://smm.axtarget.xyz/test24.html) |
| `interacao-neon.html` | [test29](https://smm.axtarget.xyz/test29.html) |
| `faiscas-fogo.html` | [test30](https://smm.axtarget.xyz/test30.html) |
| `particulas-ar.html` | [test31](https://smm.axtarget.xyz/test31.html) |
| `galaxia-quantica.html` | [test32](https://smm.axtarget.xyz/test32.html) |
| `caveira-neon.html` | [test35](https://smm.axtarget.xyz/test35.html) |
| `arco-iris.html` | [test37](https://smm.axtarget.xyz/test37.html) |
| `cubos-3d.html` | [test41](https://smm.axtarget.xyz/test41.html) |

### Gestos por projeto

**Naruto** — mão direita aberta: Sasuke · mão esquerda aberta: Naruto

**Piano Neon** — pinça nas teclas · mão esq. Dó–Fá · mão dir. Sol–Dó+

**Globo 3D** — mão dir.: mover/parar · mão esq.: girar · pinça: zoom

**Partículas 3D (`texto.html`)** — digite até 15 letras · mouse afasta partículas

**Partículas Neon (`particulas.html`)** — 1/2/3 dedos: empurra/estrela/esfera · pinça esq.: zoom

**Esfera (`esfera.html`)** — dir.: pinça estica, punho explode · esq.: move o conjunto

**Teclado Virtual** — pinça na tecla: digitar · mão aberta: apagar

**Simbiote** — mão dir. (azul): gira · mão esq. (vermelha): corrupção/explosão

**Interação Neon** — aproxime dedos das duas mãos para raios · punhos: desconectar

**Faíscas de Fogo** — indicador levantado: desenhar · polegar↑ + indicador fechado: limpar

**Partículas AR** — uma mão: pinça = linha / fechada = Terra; duas mãos: cubo, esfera ou Terra

**Galáxia Quântica** — punho contrai · mão aberta expande · indicador+anel desintegra

**Caveira Neon** — indicador perto espalha partículas (dourado) e restaura (azul)

**Arco-íris** — indicador desenha · pinça arrasta traço · botão **Limpar tudo**

**Grade de Cubos 3D** — mão perto revela cubos · punho: todos acendem em azul

### Requisitos
- Navegador com câmera (exceto `texto.html`, que usa mouse/teclado)
- Permissão de webcam nos projetos com MediaPipe
- Conexão com internet (CDN MediaPipe / Three.js / texturas)
