const Data = ({ data } : any) => {
    return (
    <>
        <th>{data.id}</th>
        <th>{data.owner}</th>
        <th>{data.content}</th>
        <th>{data.created_date}</th>
        <th>{data.important ? 'True' : 'False'}</th>
    </>
    )
  }
  
  export default Data