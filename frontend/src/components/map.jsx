import "./map.css"

function Map(){

    return(
        // return map here
        <div className="map-section">
        <iframe
            src="./../mumbai_population_map_with_elevation.html"
            title="Mumbai Population Map"
            width={"100%"}
            height={"100%"}
      />
        </div>
    )
}

export default Map