d3.csv("cr-cw-list.csv") 
.then(function(data) {
    // get csv headers for info if Live = Collection or War Day
    var headerNames = d3.keys(data[0]);
    var warMode = (headerNames.indexOf("LiveCol") == -1 ? "LiveWar" : "LiveCol");

    function getRowType(item) {
        // item exists not in column[1] -> row 0 (Name, Wins, ...)
        if (columns[1].indexOf(item) == -1) return 0;
        // item exists not in column[0] -> row 1 (Live, #1, #2, ...)
        else if (columns[0].indexOf(item) == -1) return 1;
        else return -1;
    }

    function getColSpan(name) {
        switch(name) {
            case 'Name': case 'Wins': return 4;
            case 'Cards': return 3;
            default: return 1;
        }
    }

    function deleteUnwantedProps(obj, arr) {
        Object.keys(obj).forEach(function(item){
            found = false;
            for (var i= 0; i < arr.length; i++)
                if (item == arr[i]) found = true;
            if (!found) delete obj[item];
        });
    }

    // the columns you'd like to display
    var columns = [2];
    columns[0] = ["Name", "Wins", "Cards"];
    columns[1] = ["Live", "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10"];

    var table = d3.select("#container").append("table"),
        thead = table.append("thead"),
        tbody = table.append("tbody");


    // split each row from the data object in two (two "header" rows)
    var sumWins = 0;
    var sumBattles = 0;
    var avgCards = 0;

    for (var i = data.length -1; i >= 0; i--) {
        // replace column [LiveC/W] with [Live]
        data[i]["Live"] = data[i][warMode];
        delete data[i][warMode];

        data[2*i] = data[i]
        data[2*i+1] = Object.assign({}, data[i]); 

        // some Math Calcs
        sumWins += Number(data[2*i]['Wins']);
        sumBattles += Number(data[2*i]['Battles']);
        avgCards += Number(data[2*i]['Cards']);
        winRate = Math.round(data[2*i]['Wins'] / data[2*i]['Battles'] * 100 * 100) / 100;
        data[2*i]['Wins'] += "/" + data[2*i]['Battles'] + " (" + (isNaN(winRate) ? 0 : winRate)  + "%)";

        // Delete unwanted columns of rows
        deleteUnwantedProps(data[2*i], columns[0]);
        deleteUnwantedProps(data[2*i+1], columns[1]);
    }

    // Calc average cards amount
    avgCards = Math.round(avgCards / (data.length / 2));

    // append the 1st header row
    thead.append("tr").selectAll("th").data(columns[0]).enter().append("th")
        .text(function(column) { 
            switch (column) {
                case "Wins": return column + " (Ø " + Math.round(sumWins / sumBattles * 100 * 100) / 100 + "%)";
                case "Cards": return column + " (Ø " + avgCards + ")";
            }
            return column; })
        .attr("colspan", function(column) { return getColSpan(column) });                 

    // append the 2nd header row
    thead.append("tr").selectAll("th").data(columns[1]).enter().append("th").text(function(column) { return column; });

    // create a row for each object in the data
    var rows = tbody.selectAll("tr").data(data).enter().append("tr");

    // create a cell in each row for each column
    var cells = rows.selectAll("td")
        .data(function(row) {
            return columns[getRowType(Object.keys(row)[0])].map(function(column) {
                return {column: column, value: row[column]};                       
            }); 
        })
        .enter()
        .append("td")
        .attr("colspan", function(d) { return getColSpan(d.column) })
        .attr("class", function(d) {
            if(getRowType(d.column) == 1) {
                columnValue = d.value.split(";");
                // not participated
                if (columnValue[1] === "" && columnValue[2] === "") return "grey";
                // collection day live column -> purple
                else if (warMode == "LiveCol" && d.column == "Live") return "purple";
                // battles == 0 -> blue
                else if (columnValue[2] == 0) return "blue";
                // battles > 0 and wins > 0 and wins != battles (e.g. 1/2) -> orange
                else if (columnValue[2] > 1 && columnValue[1] > 0 && columnValue[1] != columnValue[2]) return "orange";
                // battles > 0 and wins != battles -> red
                else if (columnValue[2] > 0 && columnValue[1] != columnValue[2]) return "red";
                // battles > 0 and wins == battles -> green
                else if (columnValue[2] > 0 && columnValue[1] == columnValue[2]) return "green";
            } else if (d.column == "Name") {
                return "name";
            }
        })
        .text(function(d) {
            if(getRowType(d.column) == 1) {
                columnValue = d.value.split(";");
                return (columnValue[0] == "") ? "-" : columnValue[0] + " (" + columnValue[1] + "/" + columnValue[2] +")";
            } else {
                 return d.value;
            }
        });
});