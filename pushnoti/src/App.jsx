import { useState } from 'react'
import {messaging} from './firebase'
import {getToken} from 'firebase/messaging'

import { useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  async function requestPermission(params) {
    const permission=await Notification.requestPermission();
    if(permission==='granted'){
      const token=await getToken(messaging,{vapidKey:'BGjURhnMY2kKvqnTuhx1OsT_6LgvM6DpJkom0QZr857qzNogDE8Y_oweNZSCjWTMx3mAbERe6E7TvFQM5e7-v34'})
        // messaging.app
    }else{
      alert("You Denied");
    }
  }
  useEffect(()=>{
    requestPermission();
  },[]);
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
