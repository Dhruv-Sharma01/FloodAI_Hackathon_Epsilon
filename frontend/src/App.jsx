import {useState , useEffect} from 'react'
import './App.css'
import Navbar from './components/navbar'
import Map from './components/map'
import SafeZone from './components/SafeZones'
import Footer from './components/footer'
import MModal from './components/modal'  

function App() {

  const [coordinates, setCoordinates] = useState({ latitude: null, longitude: null });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Function to get the user's location
    const getLocation = () => {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            setCoordinates({
              latitude: position.coords.latitude,
              longitude: position.coords.longitude,
            });
            setLoading(false);
          },
          (err) => {
            setError('Failed to retrieve location');
            setLoading(false);
          }
        );
      } else {
        setError('Geolocation is not supported by this browser');
        setLoading(false);
      }
    };

    // Get location when component mounts
    getLocation();
  }, []);

  return (
    <div className='app'>
      <Navbar />
      <MModal />
      <div className="main-content">
        <Map />
        <SafeZone />
      </div>
      <Footer />
    </div>
    
  )
}

export default App
