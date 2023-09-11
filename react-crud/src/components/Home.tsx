import { useNavigate } from "react-router-dom";

const Home = () => {
    const navigate = useNavigate()

    const handler = (page : string) => {
        navigate(`/playground/${page}`)
    }
  return (
    <div>
        <div className="banner">CRUD App</div>
        <button onClick={() => handler('psycopg2')}>Click me to go to Psycopg2 usage</button>
        <button onClick={() => handler('sqlalchemy')}>Click me to go to SQLAlchemy usage</button>
    </div>
  )  
};

export default Home; 