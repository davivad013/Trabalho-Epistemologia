import re

with open("app/static/js/main.js", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add authorsMapStarted
content = content.replace("let flatMapStarted = false;", "let flatMapStarted = false;\nlet authorsMapStarted = false;")

# 2. Add authors-map to panels
content = content.replace('flat: document.getElementById("flat-view"),', 'flat: document.getElementById("flat-view"),\n  "authors-map": document.getElementById("authors-map-view"),')

# 3. Initial active panel check
content = content.replace('if (document.getElementById("flat-view").classList.contains("active")) {', 
'''if (document.getElementById("authors-map-view").classList.contains("active")) {
    initAuthorsMap();
    authorsMapStarted = true;
  }
  if (document.getElementById("flat-view").classList.contains("active")) {''')

# 4. In activarView
content = content.replace('if (view === "flat" && !flatMapStarted && topologyData) {',
'''if (view === "authors-map" && !authorsMapStarted && topologyData) {
    initAuthorsMap();
    authorsMapStarted = true;
  }
  if (view === "flat" && !flatMapStarted && topologyData) {''')

# 5. In openAuthorModal, add the image
old_modal = '''  details.innerHTML = `
    <div class="author-detail-header">
      <h2>${author.flag ? author.flag + ' ' : ''}${author.name}</h2>
      <p><strong>Nacionalidade:</strong> ${author.nationality} | <strong>Período:</strong> ${author.birth || '?'} - ${author.death || 'Presente'}</p>
    </div>'''
new_modal = '''  details.innerHTML = `
    <div class="author-detail-header" style="display: flex; align-items: center; gap: 1rem;">
      <img src="${author.image || ''}" class="author-modal-img" alt="${author.name}" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; border: 2px solid var(--accent);">
      <div>
        <h2>${author.flag ? author.flag + ' ' : ''}${author.name}</h2>
        <p><strong>Nacionalidade:</strong> ${author.nationality} | <strong>Período:</strong> ${author.birth || '?'} - ${author.death || 'Presente'}</p>
      </div>
    </div>'''
content = content.replace(old_modal, new_modal)

# 6. In initFlatMap, ignore Europe
content = content.replace('const cont = d.properties.CONTINENT;\n          const key = continentFromCountryContinent[cont];',
'''const cont = d.properties.CONTINENT;
          if (cont === "Europe") return;
          const key = continentFromCountryContinent[cont];''')

# 7. Update initGlobe to use Continent instead of feature for altitude and color
old_globe_1 = '''.polygonSideColor((feat) => {
      if (feat.__isHovered) {
        return "rgba(3, 36, 68, 0.95)";
      }
      return "rgba(0, 25, 50, 0.08)";
    })
    .polygonAltitude((feat) => (feat.__isHovered ? 0.04 : 0.01))'''
new_globe_1 = '''.polygonSideColor((feat) => {
      if (feat.properties.CONTINENT === "Europe") return "rgba(0, 25, 50, 0.08)";
      if (globeInstance && globeInstance.__lastHoveredContinent === feat.properties.CONTINENT) {
        return "rgba(3, 36, 68, 0.95)";
      }
      return "rgba(0, 25, 50, 0.08)";
    })
    .polygonAltitude((feat) => {
      if (feat.properties.CONTINENT === "Europe") return 0.01;
      return (globeInstance && globeInstance.__lastHoveredContinent === feat.properties.CONTINENT) ? 0.04 : 0.01;
    })'''
content = content.replace(old_globe_1, new_globe_1)

# 8. Update onPolygonHover in initGlobe
old_hover = '''.onPolygonHover((polygon) => {
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
    });'''
new_hover = '''.onPolygonHover((polygon) => {
      let hoverCont = polygon ? polygon.properties.CONTINENT : null;
      if (hoverCont === "Europe") hoverCont = null;

      if (globeInstance.__lastHoveredContinent !== hoverCont) {
        globeInstance.__lastHoveredContinent = hoverCont;
        globe.polygonsData([...globeInstance.__polygonData]);
      }

      if (!hoverCont) {
        hideBalloon();
        return;
      }

      const continentKey = continentFromCountryContinent[hoverCont];
      if (continentKey) {
        const nome = continentInfo[continentKey]?.nome || hoverCont;
        showBalloon(buildAuthorBalloonContent(continentKey, nome), cursorX, cursorY);
      }
    });'''
content = content.replace(old_hover, new_hover)

# Add initAuthorsMap and buildCountryAuthorBalloonContent at the end
authors_map_code = '''
function buildCountryAuthorBalloonContent(authors) {
  if (authors.length === 0) return ``;
  let list = authors.map(a => `<button class="author-btn" onclick="openAuthorModal('${a.id}')">${a.flag ? a.flag + ' ' : ''}${a.name}</button>`).join('');
  return `<div class="author-list">${list}</div>`;
}

function initAuthorsMap() {
  if (!topologyData) return;
  const container = document.getElementById("authors-map-container");
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
          return `continent-path authors-map-path`;
      })
      .on("mouseenter", function(event, d) {
          const cont = d.properties.CONTINENT;
          if (cont === "Europe") return;
          
          const countryIso = String(d.id).padStart(3, "0");
          const countryAuthors = authorsData.filter(a => a.countryIso === countryIso);
          if (countryAuthors.length > 0) {
              d3.select(this).classed("hovered-country", true);
              showBalloon(buildCountryAuthorBalloonContent(countryAuthors), event.clientX, event.clientY);
          }
      })
      .on("mouseleave", function(event, d) {
          d3.select(this).classed("hovered-country", false);
          hideBalloon();
      });

  const imageGroup = svg.append("g");
  const countryImageCounts = {};
  
  authorsData.filter(a => a.countryIso).forEach(a => {
      const feat = topologyData.processedFeatures.find(f => String(f.id).padStart(3, "0") === a.countryIso);
      if (feat && feat.properties.CONTINENT !== "Europe") {
          const centroid = path.centroid(feat);
          const iso = a.countryIso;
          if (!countryImageCounts[iso]) countryImageCounts[iso] = 0;
          const index = countryImageCounts[iso]++;
          
          const offsets = [[0,0], [20, 0], [-20, 0], [0, 20], [0, -20], [20, 20], [-20, -20]];
          const offX = offsets[index % offsets.length][0];
          const offY = offsets[index % offsets.length][1];
          
          const size = 32;
          const r = size / 2;
          
          const g = imageGroup.append("g")
              .attr("transform", `translate(${centroid[0] + offX - r}, ${centroid[1] + offY - r})`)
              .style("pointer-events", "none");
              
          g.append("image")
              .attr("href", a.image)
              .attr("width", size)
              .attr("height", size)
              .style("clip-path", "circle(50% at 50% 50%)")
              .style("pointer-events", "none");
      }
  });
}
'''
content += authors_map_code

with open("app/static/js/main.js", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated main.js")
