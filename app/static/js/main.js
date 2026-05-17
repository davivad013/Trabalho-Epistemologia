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
let globeInstance = null;
let cursorX = 0;
let cursorY = 0;
let lastBalloonSignature = "";

function colorByContinent(continent) {
  if (continent === "Africa") {
    return "rgba(124, 233, 197, 0.52)";
  }
  if (continent === "Asia") {
    return "rgba(92, 188, 255, 0.48)";
  }
  if (continent === "Europe") {
    return "rgba(212, 177, 255, 0.49)";
  }
  if (continent === "North America") {
    return "rgba(255, 183, 132, 0.48)";
  }
  if (continent === "South America") {
    return "rgba(249, 131, 177, 0.49)";
  }
  if (continent === "Oceania") {
    return "rgba(141, 255, 209, 0.45)";
  }
  return "rgba(220, 231, 255, 0.34)";
}

function moveBalloon(x, y) {
  const offset = 16;
  const maxX = window.innerWidth - hoverBalloon.offsetWidth - 12;
  const maxY = window.innerHeight - hoverBalloon.offsetHeight - 12;
  const xPos = Math.max(12, Math.min(x + offset, maxX));
  const yPos = Math.max(12, Math.min(y + offset, maxY));
  hoverBalloon.style.transform = `translate3d(${xPos}px, ${yPos}px, 0)`;
}

function buildBalloonContent(title, subtitle, route) {
  return `<strong>${title}</strong><div class="balloon-subtitle">${subtitle}</div><iframe title="Linha do tempo" loading="lazy" src="${route}"></iframe>`;
}

function showBalloon(content, x, y) {
  if (lastBalloonSignature !== content) {
    hoverBalloon.innerHTML = content;
    lastBalloonSignature = content;
  }
  moveBalloon(x, y);
  hoverBalloon.classList.add("visible");
}

function hideBalloon() {
  hoverBalloon.classList.remove("visible");
  lastBalloonSignature = "";
}

function activarView(view) {
  Object.entries(panels).forEach(([key, panel]) => {
    panel.classList.toggle("active", key === view);
  });

  viewButtons.forEach((button) => {
    button.classList.toggle("active", button.dataset.view === view);
  });

  if (view === "globe" && !globeStarted) {
    initGlobe();
    globeStarted = true;
  }
}

viewButtons.forEach((button) => {
  button.addEventListener("click", () => {
    activarView(button.dataset.view);
  });
});

document.querySelectorAll(".continent-hotspot").forEach((hotspot) => {
  hotspot.addEventListener("mouseenter", (event) => {
    const continentKey = hotspot.dataset.continent;
    const nome = continentInfo[continentKey]?.nome || hotspot.getAttribute("aria-label") || "Continente";
    const resumo = hotspot.dataset.blurb || "Clique para explorar a linha do tempo.";
    const rota = continentInfo[continentKey]?.rota;
    if (!rota) {
      return;
    }
    showBalloon(buildBalloonContent(nome, resumo, rota), event.clientX, event.clientY);
  });
  hotspot.addEventListener("mousemove", (event) => {
    moveBalloon(event.clientX, event.clientY);
  });
  hotspot.addEventListener("mouseleave", hideBalloon);
  hotspot.addEventListener("focus", (event) => {
    const continentKey = hotspot.dataset.continent;
    const nome = continentInfo[continentKey]?.nome || hotspot.getAttribute("aria-label") || "Continente";
    const resumo = hotspot.dataset.blurb || "Clique para explorar a linha do tempo.";
    const rota = continentInfo[continentKey]?.rota;
    if (!rota) {
      return;
    }
    showBalloon(buildBalloonContent(nome, resumo, rota), event.clientX || cursorX, event.clientY || cursorY);
  });
  hotspot.addEventListener("blur", hideBalloon);
});

document.addEventListener("mousemove", (event) => {
  cursorX = event.clientX;
  cursorY = event.clientY;
});

function initGlobe() {
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
      const countryName = props.ADMIN || "Pais sem nome";
      const continent = props.CONTINENT || "continente desconhecido";
      const continentKey = continentFromCountryContinent[continent];
      const route = continentInfo[continentKey]?.rota;

      if (route) {
        showBalloon(
          buildBalloonContent(countryName, `Continente: ${continent}`, route),
          cursorX,
          cursorY
        );
      }

      polygon.__isHovered = true;
      globeInstance.__lastHovered = polygon;
      globe.polygonsData([...globeInstance.__polygonData]);
    });

  globeInstance = globe;
  globe.controls().autoRotate = true;
  globe.controls().autoRotateSpeed = 0.32;
  globe.pointOfView({ lat: 12, lng: 20, altitude: 2.05 });

  fetch("https://unpkg.com/world-atlas@2.0.2/countries-110m.json")
    .then((res) => res.json())
    .then((topology) => {
      const countries = window.topojson.feature(topology, topology.objects.countries);
      return fetch("https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson")
        .then((res) => res.json())
        .then((naturalEarth) => {
          const byIsoN3 = {};
          naturalEarth.features.forEach((feat) => {
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

          globeInstance.__polygonData = countries.features;
          globeInstance.__lastHovered = null;
          globe.polygonsData(countries.features);
        });
    })
    .catch(() => {
      showBalloon("<strong>Erro</strong><div class=\"balloon-subtitle\">Nao foi possivel carregar dados do globo.</div>", window.innerWidth / 2, 110);
    });
}
