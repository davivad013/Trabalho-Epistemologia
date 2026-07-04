import re

with open("app/static/js/main.js", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update initFlatMap to include zoom
flat_map_g_old = '''  svg.append("g")
      .selectAll("path")'''
flat_map_g_new = '''  const g = svg.append("g");
  
  const zoom = d3.zoom()
      .scaleExtent([1, 8])
      .on("zoom", (event) => {
          g.attr("transform", event.transform);
      });
  svg.call(zoom);

  g.selectAll("path")'''
content = content.replace(flat_map_g_old, flat_map_g_new)

# 2. Update initAuthorsMap to include zoom, color classes, and clickable images
authors_map_g_old = '''  svg.append("g")
      .selectAll("path")
      .data(topologyData.processedFeatures)
      .join("path")
      .attr("d", path)
      .attr("class", d => {
          return `continent-path authors-map-path`;
      })'''
authors_map_g_new = '''  const mainG = svg.append("g");
  
  const zoom = d3.zoom()
      .scaleExtent([1, 8])
      .on("zoom", (event) => {
          mainG.attr("transform", event.transform);
      });
  svg.call(zoom);

  mainG.selectAll("path")
      .data(topologyData.processedFeatures)
      .join("path")
      .attr("d", path)
      .attr("class", d => {
          const cont = d.properties.CONTINENT;
          const key = continentFromCountryContinent[cont];
          return `continent-path authors-map-path ${key ? 'cont-' + key : ''}`;
      })'''
content = content.replace(authors_map_g_old, authors_map_g_new)

# replace imageGroup = svg.append("g"); with imageGroup = mainG.append("g");
content = content.replace('const imageGroup = svg.append("g");', 'const imageGroup = mainG.append("g");')

# replace the image attributes to make them clickable
image_old = '''.style("clip-path", "circle(50% at 50% 50%)")
              .style("pointer-events", "none");'''
image_new = '''.style("clip-path", "circle(50% at 50% 50%)")
              .style("pointer-events", "auto")
              .style("cursor", "pointer")
              .on("click", function(event) {
                  event.stopPropagation();
                  openAuthorModal(a.id);
              });'''
content = content.replace(image_old, image_new)

with open("app/static/js/main.js", "w", encoding="utf-8") as f:
    f.write(content)
print("Maps updated")
