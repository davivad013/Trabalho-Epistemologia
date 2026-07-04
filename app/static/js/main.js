const continentInfo = {
  africa: { nome: "Africa", rota: "/cards/africa" },
  "america-do-norte": { nome: "America do Norte", rota: "/cards/america-do-norte" },
  "america-do-sul": { nome: "America do Sul", rota: "/cards/america-do-sul" },
  antartida: { nome: "Antartida", rota: "/cards/antartida" },
  asia: { nome: "Asia", rota: "/cards/asia" },
  europa: { nome: "Europa", rota: "/cards/europa" },
  oceania: { nome: "Oceania", rota: "/cards/oceania" }
};

const continentFromCountryContinent = {
  Africa: "africa",
  Asia: "asia",
  Europe: "europa",
  "North America": "america-do-norte",
  "South America": "america-do-sul",
  Oceania: "oceania",
  Antarctica: "antartida"
};

const viewButtons = document.querySelectorAll(".view-btn");
const panels = {
  flat: document.getElementById("flat-view"),
  globe: document.getElementById("globe-view")
};
const hoverBalloon = document.getElementById("hoverBalloon");

let globeStarted = false;
let flatMapStarted = false;
let globeInstance = null;
let cursorX = 0;
let cursorY = 0;
let lastBalloonSignature = "";

let authorsData = [];
let topologyData = null;
let naturalEarthData = null;

Promise.all([
  fetch("/api/info").then(res => res.json()),
  fetch("https://unpkg.com/world-atlas@2.0.2/countries-110m.json").then(res => res.json()),
  fetch("https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson").then(res => res.json())
]).then(([infoData, topo, neData]) => {
  authorsData = infoData;
  topologyData = topo;
  naturalEarthData = neData;
  
  const countries = window.topojson.feature(topologyData, topologyData.objects.countries);
  const byIsoN3 = {};
  naturalEarthData.features.forEach((feat) => {
    const isoN3 = feat.properties.ISO_N3;
    if (isoN3) {
      byIsoN3[isoN3] = feat;
    }
  });

  countries.features.forEach((feat) => {
    const countryId = String(feat.id).padStart(3, "0");
    const match = byIsoN3[countryId];
    feat.properties = {
      ADMIN: match?.properties?.NAME || `Pais ${feat.id}`,
      CONTINENT: match?.properties?.CONTINENT || "Desconhecido"
    };
    feat.__isHovered = false;
  });
  
  topologyData.processedFeatures = countries.features;

  if (document.getElementById("flat-view").classList.contains("active")) {
    initFlatMap();
    flatMapStarted = true;
  }
  if (document.getElementById("globe-view").classList.contains("active")) {
    initGlobe();
    globeStarted = true;
  }
});

function colorByContinent(continent) {
  if (continent === "Africa") return "rgba(124, 233, 197, 0.52)";
  if (continent === "Asia") return "rgba(92, 188, 255, 0.48)";
  if (continent === "Europe") return "rgba(212, 177, 255, 0.49)";
  if (continent === "North America") return "rgba(255, 183, 132, 0.48)";
  if (continent === "South America") return "rgba(249, 131, 177, 0.49)";
  if (continent === "Oceania") return "rgba(141, 255, 209, 0.45)";
  return "rgba(220, 231, 255, 0.34)";
}

let balloonHideTimeout;
function moveBalloon(x, y) {
  const offset = 16;
  const maxX = window.innerWidth - hoverBalloon.offsetWidth - 12;
  const maxY = window.innerHeight - hoverBalloon.offsetHeight - 12;
  const xPos = Math.max(12, Math.min(x + offset, maxX));
  const yPos = Math.max(12, Math.min(y + offset, maxY));
  hoverBalloon.style.transform = `translate3d(${xPos}px, ${yPos}px, 0)`;
}

hoverBalloon.addEventListener("mouseenter", () => {
  if(balloonHideTimeout) clearTimeout(balloonHideTimeout);
});
hoverBalloon.addEventListener("mouseleave", () => {
  scheduleHideBalloon();
});

function scheduleHideBalloon() {
  if(balloonHideTimeout) clearTimeout(balloonHideTimeout);
  balloonHideTimeout = setTimeout(() => {
    hoverBalloon.classList.remove("visible");
    lastBalloonSignature = "";
  }, 250);
}

window.openAuthorModal = function(id) {
  const author = authorsData.find(a => a.id === id);
  if(!author) return;
  const modal = document.getElementById('authorModal');
  const details = document.getElementById('authorDetails');
  
  let booksHtml = '';
  if (author.books && author.books.length > 0) {
    booksHtml = `
      <div class="author-works">
        <h3>Obras</h3>
        <ul>
          ${author.books.map(b => `<li>${b.title} ${b.year ? '('+b.year+')' : ''}</li>`).join('')}
        </ul>
      </div>
    `;
  }

  details.innerHTML = `
    <div class="author-detail-header">
      <h2>${author.flag ? author.flag + ' ' : ''}${author.name}</h2>
      <p><strong>Nacionalidade:</strong> ${author.nationality} | <strong>Período:</strong> ${author.birth || '?'} - ${author.death || 'Presente'}</p>
    </div>
    <p>${author.longDescription || author.shortDescription || 'Sem descrição.'}</p>
    ${booksHtml}
  `;
  modal.removeAttribute('hidden');
};

document.getElementById('closeModalBtn').addEventListener('click', () => {
  document.getElementById('authorModal').setAttribute('hidden', 'true');
});

function buildAuthorBalloonContent(continentKey, continentName) {
  const filtered = authorsData.filter(a => {
      const c = a.continent;
      if (continentKey === 'america-do-norte' && c === 'América do Norte') return true;
      if (continentKey === 'america-do-sul' && c === 'América do Sul') return true;
      if (continentKey === 'africa' && c === 'África') return true;
      if (continentKey === 'asia' && c === 'Ásia') return true;
      if (continentKey === 'oceania' && c === 'Oceania') return true;
      if (continentKey === 'europa' && c === 'Europa') return true;
      if (continentKey === 'antartida' && c === 'Antártida') return true;
      return false;
  });

  if (filtered.length === 0) {
    return `<strong>${continentName}</strong><div class="balloon-subtitle">Nenhum autor registrado.</div>`;
  }

  let list = filtered.map(a => `<button class="author-btn" onclick="openAuthorModal('${a.id}')">${a.flag ? a.flag + ' ' : ''}${a.name}</button>`).join('');
  return `<strong>${continentName}</strong><div class="balloon-subtitle">Autores e Contribuições:</div><div class="author-list">${list}</div>`;
}

function showBalloon(content, x, y) {
  if(balloonHideTimeout) clearTimeout(balloonHideTimeout);
  if (lastBalloonSignature !== content) {
    hoverBalloon.innerHTML = content;
    lastBalloonSignature = content;
  }
  moveBalloon(x, y);
  hoverBalloon.classList.add("visible");
}

function hideBalloon() {
  scheduleHideBalloon();
}

function activarView(view) {
  Object.entries(panels).forEach(([key, panel]) => {
    panel.classList.toggle("active", key === view);
  });

  viewButtons.forEach((button) => {
    button.classList.toggle("active", button.dataset.view === view);
  });

  if (view === "globe" && !globeStarted && topologyData) {
    initGlobe();
    globeStarted = true;
  }
  if (view === "flat" && !flatMapStarted && topologyData) {
    initFlatMap();
    flatMapStarted = true;
  }
}

viewButtons.forEach((button) => {
  button.addEventListener("click", () => {
    activarView(button.dataset.view);
  });
});

document.addEventListener("mousemove", (event) => {
  cursorX = event.clientX;
  cursorY = event.clientY;
});

function initFlatMap() {
  if (!topologyData) return;
  const container = document.getElementById("flat-map-container");
  container.innerHTML = "";
  
  const width = container.clientWidth || 960;
  const height = container.clientHeight || 500;
  
  const svg = d3.select(container).append("svg")
      .attr("viewBox", `0 0 960 500`)
      .attr("preserveAspectRatio", "xMidYMid meet");
      
  const projection = d3.geoEquirectangular()
      .scale(153)
      .translate([480, 250])
      .rotate([60, 0, 180]);
      
  const path = d3.geoPath().projection(projection);
  
  svg.append("g")
      .selectAll("path")
      .data(topologyData.processedFeatures)
      .join("path")
      .attr("d", path)
      .attr("class", d => {
          const cont = d.properties.CONTINENT;
          const key = continentFromCountryContinent[cont];
          return `continent-path ${key ? 'cont-' + key : ''}`;
      })
      .on("mouseenter", function(event, d) {
          const cont = d.properties.CONTINENT;
          const key = continentFromCountryContinent[cont];
          if(key) {
              d3.selectAll(`.cont-${key}`).classed("hovered", true);
              const nome = continentInfo[key]?.nome || cont;
              showBalloon(buildAuthorBalloonContent(key, nome), event.clientX, event.clientY);
          }
      })
      .on("mouseleave", function(event, d) {
          const cont = d.properties.CONTINENT;
          const key = continentFromCountryContinent[cont];
          if(key) {
              d3.selectAll(`.cont-${key}`).classed("hovered", false);
              hideBalloon();
          }
      });
}

function initGlobe() {
  if (!topologyData) return;
  const globeContainer = document.getElementById("globeViz");

  const globe = Globe()(globeContainer)
    .backgroundColor("rgba(7, 5, 37, 0)")
    .globeImageUrl("https://unpkg.com/three-globe/example/img/earth-dark.jpg")
    .bumpImageUrl("https://unpkg.com/three-globe/example/img/earth-topology.png")
    .showAtmosphere(true)
    .atmosphereColor("#6ac5ff")
    .atmosphereAltitude(0.23)
    .polygonCapColor((feat) => colorByContinent(feat.properties.CONTINENT))
    .polygonSideColor((feat) => {
      if (feat.__isHovered) {
        return "rgba(3, 36, 68, 0.95)";
      }
      return "rgba(0, 25, 50, 0.08)";
    })
    .polygonAltitude((feat) => (feat.__isHovered ? 0.04 : 0.01))
    .polygonsTransitionDuration(220)
    .polygonStrokeColor(() => "rgba(180, 221, 255, 0.35)")
    .onPolygonHover((polygon) => {
      if (globeInstance?.__lastHovered && globeInstance.__lastHovered !== polygon) {
        globeInstance.__lastHovered.__isHovered = false;
      }

      if (!polygon) {
        hideBalloon();
        if (globeInstance?.__lastHovered) {
          globeInstance.__lastHovered.__isHovered = false;
          globe.polygonsData([...globeInstance.__polygonData]);
          globeInstance.__lastHovered = null;
        }
        return;
      }

      const props = polygon.properties || {};
      const continent = props.CONTINENT || "continente desconhecido";
      const continentKey = continentFromCountryContinent[continent];
      
      if (continentKey) {
        const nome = continentInfo[continentKey]?.nome || continent;
        showBalloon(buildAuthorBalloonContent(continentKey, nome), cursorX, cursorY);
      }

      polygon.__isHovered = true;
      globeInstance.__lastHovered = polygon;
      globe.polygonsData([...globeInstance.__polygonData]);
    });

  globeInstance = globe;
  globeInstance.__polygonData = topologyData.processedFeatures;
  globeInstance.__lastHovered = null;
  globe.polygonsData(topologyData.processedFeatures);
  
  globe.controls().autoRotate = true;
  globe.controls().autoRotateSpeed = 0.32;
  globe.pointOfView({ lat: -15, lng: -60, altitude: 2.05 });
}
