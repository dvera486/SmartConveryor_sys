// main.js
let scene, camera, renderer, conveyor, boxes = [], boxCount = 0;
let speed = 10.0, baseSpeed = 10.0, running = true;
const boxWidth = 1, boxHeight = 1, boxDepth = 1;
let beltLength = 40; // Make belt much longer

function init() {
  scene = new THREE.Scene();
  // Responsive sizing
  const container = document.getElementById('scene-container');
  container.style.width = '100vw';
  container.style.height = '80vh';
  const width = container.offsetWidth || window.innerWidth;
  const height = container.offsetHeight || window.innerHeight * 0.8;
  camera = new THREE.PerspectiveCamera(75, width/height, 0.1, 100);
  renderer = new THREE.WebGLRenderer();
  renderer.setSize(width, height);
  container.appendChild(renderer.domElement);

  // Conveyor belt (longer)
  const beltGeometry = new THREE.BoxGeometry(beltLength, 0.5, 2);
  const beltMaterial = new THREE.MeshPhongMaterial({ color: 0x444444 });
  conveyor = new THREE.Mesh(beltGeometry, beltMaterial);
  conveyor.position.y = -1;
  scene.add(conveyor);

  // Lighting
  const light = new THREE.PointLight(0xffffff, 1);
  light.position.set(0, 10, 10);
  scene.add(light);

  camera.position.set(0, 5, 15);
  camera.lookAt(0, 0, 0);

  animate();
}

function addBox() {
  const geometry = new THREE.BoxGeometry(boxWidth, boxHeight, boxDepth);
  const material = new THREE.MeshPhongMaterial({ color: 0x0077ff });
  const box = new THREE.Mesh(geometry, material);
  // Start at left end of longer belt
  box.position.set(-beltLength/2 + 0.5, 0, 0);
  scene.add(box);
  boxes.push(box);
  boxCount++;
  updateSpeed();
  updateLabels();
}

function removeBox() {
  if (boxes.length > 0) {
    const box = boxes.pop();
    scene.remove(box);
    boxCount--;
    updateSpeed();
    updateLabels();
  }
}

function updateSpeed() {
  speed = Math.max(1.0, baseSpeed - 0.5 * boxCount);
}

function updateLabels() {
  document.getElementById('speed').textContent = `Speed: ${speed.toFixed(2)}`;
  document.getElementById('boxCount').textContent = `Boxes: ${boxCount}`;
}

function animate() {
  requestAnimationFrame(animate);
  if (running) {
    for (let box of boxes) {
      box.position.x += speed * 0.01;
      if (box.position.x > beltLength/2 - 0.5) box.position.x = -beltLength/2 + 0.5;
    }
  }
  renderer.render(scene, camera);
}

// Controls
window.onload = () => {
    // Handle window resize
    window.addEventListener('resize', () => {
      const container = document.getElementById('scene-container');
      const width = container.offsetWidth || window.innerWidth;
      const height = container.offsetHeight || window.innerHeight * 0.8;
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
      renderer.setSize(width, height);
    });
  init();
  document.getElementById('addBox').onclick = addBox;
  document.getElementById('removeBox').onclick = removeBox;
  document.getElementById('start').onclick = () => { running = true; };
  document.getElementById('stop').onclick = () => { running = false; };
  updateLabels();
};
