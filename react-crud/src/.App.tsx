import Home from "./components/Home";
import { Routes, Route } from "react-router-dom";

function App() {
  const padding = {
    padding: 5
  }

  return (
    <Routes>
        <Route path="/playground/:library" element={"yolo"} />
        <Route path="/" element={<Home />} />
        <Route path="*" element={"Not found"} />
    </Routes>
  );
}

export default App;
