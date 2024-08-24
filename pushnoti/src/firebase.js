// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getMessaging } from "firebase/messaging";
// import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyASDEjOtX1PRo-vXvNT5-FahxTj3RHl5Js",
  authDomain: "pushnoti-ba1a5.firebaseapp.com",
  projectId: "pushnoti-ba1a5",
  storageBucket: "pushnoti-ba1a5.appspot.com",
  messagingSenderId: "1043719834581",
  appId: "1:1043719834581:web:c9ddf75a66699a4380cb5c",
  measurementId: "G-SYG8ELTG7L"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
export const messaging = getMessaging(app);