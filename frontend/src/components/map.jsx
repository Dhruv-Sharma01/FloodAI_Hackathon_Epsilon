import "./map.css"

function Map(){

    return(
        // return map here
        <div className="map-section">
        <iframe
            src="./../flood_risk_map_with_clusters12.html"
            title="Mumbai Population Map"
            width={"100%"}
            height={"100%"}
      />
        </div>
    )
}

export default Map