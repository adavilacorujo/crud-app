import axios from 'axios'
// const baseUrl = 'http://backend:8000'
// const baseUrl = '/api'
const baseUrl = "http://0.0.0.0:6969/api"

const getAll = library => {
    // return fetch(`${baseUrl}/${library}/getData`).then(response => response.data)
    return axios.get(`${baseUrl}/${library}/getData`).then(response => response.data)
}

const createComment = (library, newObject) => {
    return axios.post(`${baseUrl}/${library}/addData`, newObject).then(response => response.data)
}

const updateComment = (id, newObject, library) => {
    return axios.put(`${baseUrl}/${library}/updateData/${id}`, newObject).then(response => response.data)
}

const deleteComment = (id, library) => {
    return axios.get(`${baseUrl}/${library}/deleteData/${id}`).then(response => response.data)
}

export default { getAll, createComment, updateComment, deleteComment}