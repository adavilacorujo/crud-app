import DisplayData from "../components/manipulators/DisplayData";
import AddData from "../components/manipulators/AddData";
import UpdateData from "../components/manipulators/UpdateData";
import DeleteData from "../components/manipulators/DeleteData";



const displaySelector = ({display, library} : any) => {
    switch(display) {
      case 'view':
        return <DisplayData library={library} />
      case 'add':
          return <AddData library={library}/>

      case 'update':
          return <UpdateData library={library} />
          
      case 'delete':
          return <DeleteData library={library} />

      default:
        return <DisplayData library={library} />
    }
}

export default displaySelector