import Playground from "./components/Playground";
import Home from "./components/Home";
import { Routes, Route, useMatch} from "react-router-dom";



const App = () => {
    return (
        <Routes>
            <Route path="/playground/:library" element={<Playground />} />
            <Route path="/" element={<Home />} />
            <Route path="*" element={"Not found"} />
        </Routes>
    )
  }

export default App;
