import { useNavigate } from "react-router-dom";

const Home = () => {
    const navigate = useNavigate()

    const handler = (page : string) => {
        navigate(`/playground/${page}`)
    }
  return (
    <>
    <div className="banner"> CRUD App</div>
      <div className="content">
        <button onClick={() => handler('psycopg2')} className="button">Take me to Psycopg2 usage</button>
        <button onClick={() => handler('sqlalchemy')} className="button">Take me to SQLAlchemy usage</button>
      </div>
    </>
  )  
};

export default Home; 