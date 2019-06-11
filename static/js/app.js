function buildCharts(sample) {

  // fetch the sample data for the plots
  var url = `/samples/${sample}`;
  d3.json(url).then(function(data) {


    //Pie Chart
    d3.json(url).then(function(data) {  
    var pie_values = data.sample_values.slice(0,10);
      var pie_labels = data.Year.slice(0,10);
      // var pie_hover = data.otu_labels.slice(0,10);
      var piecolors = []
      var data = [{
        values: pie_values,
        labels: pie_labels,
        hovertext: pie_hover,
        type: 'pie',
        
      }];

      Plotly.newPlot('pie', data);

    });
  });   
}


function init() {
  
  var selector = d3.select("#selDataset");

  
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data 
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();