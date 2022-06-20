import { BrowserRouter, Routes, Route } from "react-router-dom";
import AuthPage from "./pages/AuthPage";
import AuthResult from "./pages/AuthResult.js";
// import AxiosTest from "./pages/AxiosTest";
import BalancePage from "./pages/BalancePage";
import MainPage from "./pages/MainPage";
// import NewsApiPage from "./pages/NewsApiPage";
// import QrCodePage from "./pages/QrCodePage";
// import QrCodeReaderPage from "./pages/QrCodeReaderPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<AuthPage />}></Route>
      </Routes>
      <Routes>
        <Route path="/authResult" element={<AuthResult />}></Route>
      </Routes>
      <Routes>
        <Route path="/main" element={<MainPage />}></Route>
      </Routes>
      <Routes>
        <Route path="/balance" element={<BalancePage />}></Route>
      </Routes>
      <Routes>
        <Route path="/qr" element={<QrCodePage />}></Route>
      </Routes>
      <Routes>
        <Route path="/qrreader" element={<QrCodeReaderPage />}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
