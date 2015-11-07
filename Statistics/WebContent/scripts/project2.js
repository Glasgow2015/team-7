window.onload = function() {
    var r = Raphael(10, 50, 1850, 1800);
    r.text(1000,250,"22 people die each day in the UK from\npancreatic cancer.\nMost people only learn about the pancreas \nwhen an illness affects someone they know.\n\n90% of patients are diagnosed too late for \npotentially curative surgery.").attr({font: "20px sans-serif"});
    r.text(1000,600,"Survival rates for pancreatic cancer have\nshown marginal gains in the last 40 years.\nPancreatic cancer still only has a 4% 5 year\nsurvival rate.").attr({font: "20px sans-serif"});
    r.text(1000,1100,"Pancreatic cancer is the 5th commonest cause\nof cancer death yet receives less than 1% of\nresearch funding.").attr({font: "20px sans-serif"});
    
    
    var pie = r.piechart(320, 240, 100, [90, 10], {donut : true, legend: ["Late Diagnosis", "On Time Diagnosis"], colors : ["", "bde"], legendpos: "east"});
    
    
    r.text(320, 100, "On Time Diagnosis").attr({ font: "20px sans-serif" });
    pie.hover(
		function () {
        var that = this.sector;
        this.sector.stop();
        this.sector.scale(1.1, 1.1, this.cx, this.cy);

        pie.each(function() {
           if(this.sector.id === that.id) {
            console.log(pie)
               tooltip = r.text(320, 220, this.sector.value.value).attr({"font-size": 0, "fill":"#000"});
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
    
    var donut = r.piechart(320, 600, 100, [4, 96], {donut : true, colors : ["#406", "#b7d"], legend: ["Survive beyond 5 years", "Do not survive"], legendpos: "east"});
    r.text(320, 470, "Survival Rate").attr({ font: "20px sans-serif" });
    donut.hover(
		function () {
        var that = this.sector;
        this.sector.stop();
        this.sector.scale(1.1, 1.1, this.cx, this.cy);

        donut.each(function() {
           if(this.sector.id === that.id) {
            console.log(donut)
               tooltip = r.text(320, 580, this.sector.value.value).attr({"font-size": 0, "fill":"#000"});
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
    
    fin = function () {
        this.flag = r.popup(this.bar.x, this.bar.y, this.bar.value || "0").insertBefore(this);
    },
    fout = function () {
        this.flag.animate({opacity: 0}, 300, function () {this.remove();});
    },
    
    txtattr = { font: "20px sans-serif"  };

    r.text(320, 900, "Relative research funding (in pounds) /\n death spent by cancer type").attr(txtattr);


    r.barchart(190, 950, 300, 220, [[1, 6, 11, 12, 23, 26, 28, 35]], {colors : ["#EA44F3"], type : "round"}).hover(fin, fout);
    r.text(365, 1220, "Hodgkin's decease").attr({font: "14px sans-serif"}).transform("t100,100r90t-100,0");
    r.text(328, 1220, "Skin cancer").attr({font: "14px sans-serif"}).transform("t100,100r90t-100,0");
    r.text(292, 1220, "Leukaemia").attr({font: "14px sans-serif"}).transform("t100,100r90t-100,0");
    r.text(292-35, 1220, "Cervical cancer").attr({font: "14px sans-serif"}).transform("t100,100r90t-100,0");
    r.text(292-75, 1220, "Sarcoma").attr({font: "14px sans-serif"}).transform("t100,100r90t-100,0");
    r.text(292-108, 1220, "Breast cancer").attr({font: "14px sans-serif"}).transform("t100,100r90t-100,0");
    r.text(292-144, 1240, "Non-Hodgkin's lymphoma").attr({font: "14px sans-serif"}).transform("t100,100r90t-100,0");
    r.text(292-144-35, 1240, "Pancreatic cancer").attr({font: "14px sans-serif"}).transform("t100,100r90t-100,0");
    
   
    
}

