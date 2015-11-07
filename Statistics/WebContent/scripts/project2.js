window.onload = function() {
    var r = Raphael(10, 50, 640, 480);
    var pie = r.piechart(320, 240, 100, [90, 10], {donut : true, legend: ["Late Diagnosis", "On Time Diagnosis"], legendpos: "east"});

    r.text(320, 100, "On Time Diagnosis Rate").attr({ font: "20px sans-serif" });
    pie.hover(
		function () {
        var that = this.sector;
        this.sector.stop();
        this.sector.scale(1.1, 1.1, this.cx, this.cy);

        pie.each(function() {
           if(this.sector.id === that.id) {
            console.log(pie)
               tooltip = r.text(320, 240, this.sector.value.value).attr({"font-size": 32, "fill":"#000"});
           }
        });

        if (this.label) {
            this.label[0].stop();
            this.label[0].attr({ r: 7.5 });
            this.label[1].attr({ "font-weight": 700 });
        }
    }, 

	function () {
        this.sector.animate({ transform: 's1 1 ' + this.cx + ' ' + this.cy }, 400, "bounce");
        tooltip.remove();

        if (this.label) {
            this.label[0].animate({ r: 5 }, 400, "bounce");
            this.label[1].attr({ "font-weight": 300 });
        }
    });
 
}
