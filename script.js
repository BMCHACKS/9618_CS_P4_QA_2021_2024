const canvas = document.getElementById('matrix');
const ctx = canvas.getContext('2d');

canvas.height = window.innerHeight;
canvas.width = window.innerWidth;

const characters = 'BMC'; 
const fontSize = 10; 
const columns = Math.floor(canvas.width / fontSize);
const drops = Array(columns).fill(0);

function draw() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#0F0'; 
    ctx.font = fontSize + 'px monospace';

    for (let i = 0; i < drops.length; i++) {
        const text = characters.charAt(i % characters.length);
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);
        
        
        if (drops[i] * fontSize > canvas.height) {
            drops[i] = 0; 
        }
        drops[i]++; 
    }
}

setInterval(draw, 100); 

const terminalOutput = document.getElementById('output');
const terminalInput = document.getElementById('input');
const container = document.getElementById('container');
const terminal = document.getElementById('terminal');

//function initTerminal() {
//    terminalOutput.textContent += 'Press Enter to Continue: ';
//}
terminal.style.display = 'none';
container.style.display = 'block';

terminalInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        const code = terminalInput.value;
        if (code === '') {
            terminalOutput.textContent += '\nAccess granted.\n';
            terminalInput.style.display = 'none';
            container.style.display = 'block';
            terminal.style.display = 'none'; 
        } else {
            terminalOutput.textContent += 'Press Enter..';
        }
        terminalInput.value = '';
    }
});


container.addEventListener('mousemove', (event) => {
    const { clientX, clientY } = event;
    const { left, top, width, height } = container.getBoundingClientRect();


    const centerX = left + width /2;
    const centerY = top + height /2;


    const deltaX = clientX - centerX;
    const deltaY = clientY - centerY;


    const tiltX = (deltaY / height) * 30;
    const tiltY = (deltaX / width) * -30; 


    container.style.transform = `rotateX(${tiltX}deg) rotateY(${tiltY}deg)`;
});


container.addEventListener('mouseleave', () => {
    container.style.transform = 'rotateX(0deg) rotateY(0deg)';
});

//initTerminal();
