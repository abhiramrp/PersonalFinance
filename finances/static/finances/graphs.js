
// source: https://medium.com/code-nebula/automatically-generate-chart-colors-with-chart-js-d3s-color-scales-f62e282b2b41

const colorScale = d3.interpolateSpectral; 
      
const colorRangeInfo = {
    colorStart: 0,
    colorEnd: 1,
    useEndAsStart: false,
}; 

function calculatePoint(i, intervalSize, colorRangeInfo) {
    var { colorStart, colorEnd, useEndAsStart } = colorRangeInfo;
    return (useEndAsStart
      ? (colorEnd - (i * intervalSize))
      : (colorStart + (i * intervalSize)));
}

function interpolateColors(dataLength, colorScale, colorRangeInfo) {
    var { colorStart, colorEnd } = colorRangeInfo;
    var colorRange = colorEnd - colorStart;
    var intervalSize = colorRange / dataLength;
    var i, colorPoint;
    var colorArray = [];
  
    for (i = 0; i < dataLength; i++) {
      colorPoint = calculatePoint(i, intervalSize, colorRangeInfo);
      colorArray.push(colorScale(colorPoint));
    }
  
    return colorArray;
}  

function createPiechart(labels, data, title, id ) {
    let COLORS = interpolateColors(labels.length, colorScale, colorRangeInfo);

    const d = {
        labels: labels,
        datasets: [{
            label: title, 
            data: data,
            backgroundColor: COLORS, 
            hoverBackgroundColor: COLORS
        }]
    };

    const config = {
        type: 'pie', 
        data: d,
        
    };

    const eChart = new Chart(
        document.getElementById(id), 
        config
    );

    return eChart; 

}