const Option = ({ data } : any) => {
    const optionPrefix = 'option_select_'
    return (
    <>
        <option key={`${optionPrefix}${data.id}`} value={data.id}>{data.id}. {data.content}</option>
    </>
    )
  }
  
  export default Option