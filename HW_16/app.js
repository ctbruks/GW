var svgWidth = 1050;
var svgHeight = 700;

var chartMargin = { top: 20, right: 30, bottom: 20, left: 30 };
var chartWidth = svgWidth - chartMargin.left - chartMargin.right;
var chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

var svg = d3.select(".myChart")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight)
  .append("g")
  .attr("transform", "translate(" + chartMargin.left + "," + chartMargin.top + ")");

var chart = svg.append("g");

d3.csv("data/data2leo.csv", function(error, demoData) {
    if (error) throw error;
    console.log(demoData);
    demoData.forEach(function(data) {
        data.employed = +data.employed;
        data.good_better_health = +data.good_better_health;
    });
  // Create scale functions
  var yLinearScale = d3.scaleLinear()
    .range([chartHeight, 0]);
  var xLinearScale = d3.scaleLinear()
    .range([0, chartWidth]);
  // Create axis functions
  var bottomAxis = d3.axisBottom(xLinearScale);
  var leftAxis = d3.axisLeft(yLinearScale);

// Scale the domain
xLinearScale.domain([45, d3.max(demoData, function(data) {
        return +data.employed + 2;
  })]);
yLinearScale.domain([70, d3.max(demoData, function(data) {
        return +data.good_better_health + 2;
  })]);

  chart.selectAll("circle")
  .data(demoData)
  .enter().append("circle")
    .attr("cx", function(data, index) {
      return xLinearScale(data.employed);
    })
    .attr("cy", function(data, index) {
      return yLinearScale(data.good_better_health);
    })
    .attr("r", 15)
    .attr('fill', 'gray');



  chart.append("g")
    .attr("transform", `translate(0, ${chartHeight})`)
    .call(bottomAxis);

  chart.append("g")
    .call(leftAxis);

   chart.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 5)
    .attr("x", 0)
    .attr("dy", "1em")
    .attr("class", "axisText")
    .style('text-anchor','end')
    .text("Good or Better Health(%)");

   chart.append("text")
    .attr("class","label")
    .attr("y", 640)
    .attr("x", 825)
    .attr("dy", "1em")
    .style("text-anchor", "end")
    .text("Employed(%)");

  });
   
  
    //x = census data; y = risk data;
