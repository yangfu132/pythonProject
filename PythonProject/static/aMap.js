
(function() {
    'use strict';
    return window.MapModule || (function(){
        var MapModule = window.MapModule || (window.MapModule = {

            initMap : function(){
                this.map = new AMap.Map("container", {
                    resizeEnable: true,
                    zoom: 13
                });
                //window.mapObject.listP.length();
                self.showMarkerLabel = false;
                self.showLine = false;
                this.addMarker(window.mapObject.listP, self.showMarkerLabel,self.showLine);
            },

            
            addMarker : function(pointArray, isShowDistance,isShowLabel){
                this.currentPointArray = pointArray;

                this.map.clearMap();

                var lineArray = [];
                
                for(var i = 0; i < pointArray.length; i++){
                    var m1 = this.pointToMarker(pointArray[i],i,isShowLabel);
                    lineArray.push(m1);
                }
                this.map.setFitView();
                //alert("isShowDistance" + isShowDistance);
                //alert("isShowLabel" + isShowLabel);
                if (isShowDistance)
                {
                    this.addLine(lineArray, isShowDistance);
                }
            },
            
            filterPoint : function(lineArray, distanceMin) {

                var filterArray = [];

                for (var i = 1; i < lineArray.length; i++) {
                    var m1 = this.pointToMarker(lineArray[i-1],i-1,true);
                    var m2 = this.pointToMarker(lineArray[i],i,true);

                    var p1 = m1.getPosition();
                    var p2 = m2.getPosition();
                    var distance = Math.round(p1.distance(p2));

                    if(distance >= distanceMin) {
                        filterArray.push(lineArray[i-1]);
                        filterArray.push(lineArray[i]);
                    }
                }

                return filterArray;
            },

            pointToMarker : function(point,strLabel,isShowLabel){
                var m1 = new AMap.Marker({
                    map: this.map,
                    draggable:false,
                    position: new AMap.LngLat(point["lon"], point["lat"]),
                    topWhenClick:true
                });
                strLabel = window.mapObject.listP.indexOf(point);
                if (isShowLabel)
                {
                    m1.setLabel({
                        offset: new AMap.Pixel(0, 0),  //设置文本标注偏移量
                        content: strLabel, //设置文本标注内容
                        direction: 'top' //设置文本标注方位
                    });
                }

                var tip = "速度:"+ point["speed"] +"，精度:" + point["accuracy"] + 
                "，海拔:" + point["altitude"] + "，经度:" + point["lon"] +"，纬度:" + point["lat"] + "，时间:" + point["time"] + "，索引：" + strLabel;
                m1.setExtData({"tip":tip,"originIndex":strLabel});
                m1.on('click', function() {
                    var extraData = this.getExtData();
                    $('#infoPoint').val(extraData["tip"]);
                });

                return m1;
            },

            addLine : function(lineArray, isShowDistance){
                var isListP = lineArray.length == window.mapObject.listP;
                for (var i = 1; i < lineArray.length; i++) {
                    var m1 = lineArray[i-1];
                    var m2 = lineArray[i];
                    if (!isListP)
                    {
                        //var posM1 = m1.tip.content;
                        //var posM2 = m2.tip.content;
                        //if (posM2 - posM1 != 1)
                            //continue;
                        var extraData1 = m1.getExtData();
                        var extraData2 = m2.getExtData();
                        if (extraData2["originIndex"] - extraData1["originIndex"] != 1)
                            continue;
                    }

                    var p1 = m1.getPosition();
                    var p2 = m2.getPosition();
                    var textPos = p1.divideBy(2).add(p2.divideBy(2));
                    var distance = Math.round(p1.distance(p2));
                    var path = [p1,p2];

                    var line = new AMap.Polyline({
                        map:this.map,
                        strokeColor:'#80d8ff',
                        isOutline:true,
                        outlineColor:'white',
                        path:path
                    });
                    line.setPath(path);
                    
                    if (isShowDistance) {
                        var text = new AMap.Text({
                            text:'两点相距'+distance+'米',
                            position: textPos,
                            map:this.map,
                            style:{'background-color':'#29b6f6',
                            'border-color':'#e1f5fe',
                            'font-size':'12px'}
                        });
                        
                        text.setText('两点相距'+distance+'米');
                        text.setPosition(textPos);
                    }
                }

                this.map.setFitView();
            },

            onPointPre : function() {
                this.map.clearMap();
                this.addMarker(this.currentPointArray, self.showLine,self.showMarkerLabel);
            },

            onPointNext : function() {
                this.map.clearMap();
                this.addMarker(this.currentPointArray, self.showLine,self.showMarkerLabel);
            },

            onScreenDistance : function() {

                var distanceMin = $('#distance-input').val();

                if(distanceMin !== undefined) {
                    this.map.clearMap();
                    var filterArray = this.filterPoint(window.mapObject.listP, parseInt(distanceMin));
                    this.addMarker(filterArray, self.showLine,self.showMarkerLabel);
                }
            },

            onShowLine : function() {
                this.map.clearMap();
                self.showLine = true;
                this.addMarker(this.currentPointArray, self.showLine,self.showMarkerLabel);
            },

            onHideLine : function() {
                this.map.clearMap();
                self.showLine = false;
                this.addMarker(this.currentPointArray, self.showLine,self.showMarkerLabel);
            },

            onShowMarkerLabel : function(){
                this.map.clearMap();
                self.showMarkerLabel = true;
                this.addMarker(this.currentPointArray, self.showLine,self.showMarkerLabel);
            },

            onHideMarkerLabel : function(){
                this.map.clearMap();
                self.showMarkerLabel = false;
                this.addMarker(this.currentPointArray, self.showLine,self.showMarkerLabel);
            }
        });
    }())
}());
